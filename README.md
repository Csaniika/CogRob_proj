# Kognitív robotika projekt feladat 
<p align = "center">
<img src = "./figures/bme_logo_kicsi.jpg" width = "300" />
</p>

<h1 align="center" style="margin-top: 0px;">Budapesti Műszaki és Gazdaságtudományi Egyetem </h1>

<h2 align="center" style="margin-top: 0px;">Gépészmérnöki Kar</h2>
<h3 align="center" style="margin-top: 0px;">Mechatronika, Optika és Gépészeti Informatika Tanszék</h3>

<br/><br/>

<h2 align="center" style="margin-top: 0px;">Harkó Csanád - BE35IY</h2>

<br/><br/><br/>

<p align = "center">2023. május 24.</p>
<br/><br/><br/>
</p>

## Tartalomjegyzék
1. [Bevezető](# )  
2. [Telepítés](# )  
sudo apt-get install ros-noetic-effort-controllers

sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers

http://wiki.ros.org/simulator_gazebo/Tutorials/SpawningObjectInSimulation


roslaunch phantomx_gazebo phantomx_gazebo.launch

sudo apt install ros-$(rosversion -d)-joint-trajectory-controller

rostopic info /j_c1_lf_position_controller/command 
Type: trajectory_msgs/JointTrajectoryPoint
