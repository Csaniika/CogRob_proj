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

# Tartalomjegyzék
1. [Bevezető](#1-bevezető)  
    1.1. [PahntomX Mark III Hexapod](#pahntomx-mark-iii-hexapod)
2. [Telepítés](#telepítés)  


# 1. Bevezető

Jelen projektfeladat a [Kognitív robotika](https://github.com/MOGI-ROS/Week-1-8-Cognitive-robotics) (BMEGEMINMKR) tárgy labor részéhez készült. A laborgyakorlatok célja a ROS-al való megbarátkozás volt, így ez a munka is, ahogyan a labor feladatok, [ROS Noetic](http://wiki.ros.org/noetic/Installation)-et használ. 

A munka során egy hatlábú robot implementálására, majd annak egy részben önszerveződő modellel való vezérlésére került sor.

## 1.1. PahntomX Mark III Hexapod

A szimuláció, egy a valóságban is létező ([PhantomX Mark III Hexapod](https://www.trossenrobotics.com/phantomx-ax-hexapod.aspx)), hatlábú lépkedő robotot használ. Ez egy kutatási célokra kifejlesztett robot, a hat láb mindegyike három csuklóval rendelkezik, melyek közül eggyel csatlakozik
a robot testéhez, így a teljes robot 18 csuklóval bír. 

A szimulációhoz használt virtuális robot modellje [URDF fájlként érhető el.](https://github.com/HumaRobotics/phantomx_description)

<img src = "./figures/phantomx.jpg" height = "150" />
<img src = "./figures/phantomx_simu.png" height = "150" />

# 2. Telepítés

A projekt kipróbálásához ezt a git repot kell lehúzni, valamint pár ROS csomag telepítése is szükséges. Ezek a következőek:

1. [ROS Control](http://wiki.ros.org/ros_control)

    A csuklók mozgatásához szükséges, a következő paranccsal lehetséges telepíteni:

    ```console
    sudo apt-get install ros-noetic-ros-control 
    ```
2. [ROS Position Controllers](http://wiki.ros.org/position_controllers)

    A csuklókat pozíció szerint vezéreljük (az eredeti, robotot leíró URDF-ben, effort controller van). Ez a csomag a `position_controllers/JointGroupPositionController` típus használata miatt szükséges, így 1 kontrollerben lehet kezelni az összes csuklót. Telepítése:
    ```console
    sudo apt-get install ros-noetic-position-controllers
    ```
http://wiki.ros.org/simulator_gazebo/Tutorials/SpawningObjectInSimulation




roslaunch phantomx_gazebo phantomx_gazebo.launch

rostopic info /legs_controller/command 

# A feladat részei

## PhantomX URDF

## ROS control - csomag

## A csuklókat vezérlő node

### Taszító Kuramoto-modell

# Eredmények

# Hivatkozások
### [1] [Robotrendszerek (BMEGEMINMRL) tárgy 9.-10. heti anyaga](https://github.com/MOGI-ROS/Week-9-10-Simple-arm)

### [2] Harkó Csanád, "Hatlábú robot kísérleti tanulmányozása: önszerveződő dinamika csatolt neuronok által", 2022
