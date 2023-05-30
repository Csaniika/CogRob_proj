#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray
import time

rospy.init_node('send_joint_angles')

pub = rospy.Publisher('/legs_controller/command', Float64MultiArray, queue_size=1)

NR = 6 #nr of rotators (legs)
w = -0.2 #weight
tau = 0.9 #time constant
a = 0.3
dt = 0.1

#tripod
K = [[0, 1, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 0],
     [1, 0, 0, 1, 1, 0],
     [0, 1, 1, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 0, 0, 1, 1, 0]]
'''
#first two block
K = [[0, 1, 0, 1, 1, 0],
     [1, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 1, 0],
     [1, 0, 1, 0, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 1, 0]]

K = [[0, 1, 1, 0, 1, 1],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 1, 0],
     [0, 1, 1, 0, 1, 1],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 1, 0]]
'''

controller_name = "legs_controller"
joint_names = rospy.get_param("/%s/joints" % controller_name)
rospy.loginfo("Joint names: %s" % joint_names)

rate = rospy.Rate(40)
#j_c1_lf,  j_c1_rf, j_c1_lm, j_c1_rm, j_c1_lr, j_c1_rr, 
#j_thigh_lf, j_thigh_rf, j_thigh_lm, j_thigh_rm, j_thigh_lr, j_thigh_rr, j_tibia_lf, 
#j_tibia_rf, j_tibia_lm, j_tibia_rm, j_tibia_lr, j_tibia_rr,
 
joint_positions_0 = [   np.pi/6, -np.pi/6, 0.0, 0.0, -np.pi/6, np.pi/6,
                        -np.pi/4, -np.pi/4, -np.pi/4, -np.pi/4, -np.pi/4, -np.pi/4,
                        -np.pi/4, -np.pi/4, -np.pi/4, -np.pi/4, -np.pi/4, -np.pi/4]

joint_positions_max = joint_positions_0 + np.ones(18) * np.pi/10
joint_positions_min = joint_positions_0 - np.ones(18) * np.pi/10

#one side mirorring coxas, 
joint_positions_max[:6:2] = joint_positions_max[:6:2] - 2 *  np.ones(3) * np.pi/10
joint_positions_min[:6:2] = joint_positions_min[:6:2] + 2 *  np.ones(3) * np.pi/10

def Phi_0values(): #rotator's phase
    Phi = np.zeros(6)
    for i in range(NR):
        Phi[i] = np.arccos(2 * (joint_positions_0[i]-joint_positions_min[i]) / np.abs(joint_positions_max[i] - joint_positions_min[i])) 
    return Phi

def equation(i): #see readme
    global K,Phi
    part1 = 1 + a * np.cos(Phi[i])
    part2 = 0
    for j in range(NR):
        if i != j:
            part2 += w * K[i][j] * np.sin(Phi[j] - Phi[i])

    return (part1 + part2) / tau

def euler(dt, i): #simple euler method
    dPhi = dt * equation(i)
    return dPhi

def phase2rad(i, shift): #convert phases to min max interval
    if i < 6:
        if i%2 == 0: #coxa where min>max
            return joint_positions_min[i] - (1 + np.cos(Phi[i] + shift)) * np.abs(joint_positions_min[i]-joint_positions_max[i]) / 2    
        else: #coxa where min<max
            return joint_positions_min[i] + (1 + np.cos(Phi[i] + shift)) * np.abs(joint_positions_max[i]-joint_positions_min[i]) / 2    
    else:
        return joint_positions_min[i] + (1 + np.cos(Phi[i%6] + shift)) * np.abs(joint_positions_max[i]-joint_positions_min[i]) / 2    

Phi = Phi_0values()

'''
t_end = time.time() + 1
while time.time() < t_end:
    pub.publish(Float64MultiArray(data=joint_positions_min))
t_end = time.time() + 1
while time.time() < t_end:
    pub.publish(Float64MultiArray(data=joint_positions_max))
'''
t_end = time.time() + 5
while time.time() < t_end:
    pub.publish(Float64MultiArray(data=joint_positions_0))

joint_positions_next = joint_positions_0

while not rospy.is_shutdown():
    for i in range(NR):
        Phi[i] += euler(dt, i)
        #print(Phi)
    for i in range(NR):
        joint_positions_next[i] = phase2rad(i, -3*np.pi/2)
        joint_positions_next[i+NR] = phase2rad(i+NR, 0)
        #joint_positions_next[i+2*NR] = phase2rad(i, 6*np.pi/4)
    pub.publish(Float64MultiArray(data=joint_positions_next))
    rate.sleep()