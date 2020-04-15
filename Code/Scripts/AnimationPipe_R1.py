#-*- coding:utf-8 -*-

"""
    [1]https://www.cnblogs.com/meteoric_cry/p/7987548.html 平面旋转
"""
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import Rectangle,PathPatch
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import sys
import os
from math import sin,cos
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""
    Rectangle location handle 
"""
class RectangleUpdate():
    def __init__(self,width=20,height=20,centerpoint=[0,0]):
        self.width = width
        self.height = height
        self.StartEdgePoint = []
        self.centerPoint = centerpoint
        self.centerArray = [(self.centerPoint[0] , self.centerPoint[1]), # left button
            (self.centerPoint[0] , self.centerPoint[1]),# left top
            (self.centerPoint[0] , self.centerPoint[1]),# right top 
            (self.centerPoint[0] , self.centerPoint[1] )#right button
            ]
        
        self.RectanglePoint = [(- width/2, - height/2), # left button
            (- width/2,  height/2),# left top
            ( width/2,  height/2),# right top 
            ( width/2, - height/2)#right button
            ]

        # calculate start edge point
        ceter_temp = np.array(self.centerArray)
        rectangle_temp = np.array(self.RectanglePoint)
        point_temp = ceter_temp + rectangle_temp
        point_temp = np.matrix.tolist(point_temp)
        
        for i in range(len(point_temp)):
            self.StartEdgePoint.append(tuple(point_temp[i]))
        # self.StartEdgePoint = [(self.centerPoint[0] - width/2, self.centerPoint[1] - height/2), # left button
        #     (self.centerPoint[0] - width/2, self.centerPoint[1] + height/2),# left top
        #     (self.centerPoint[0] + width/2, self.centerPoint[1] + height/2),# right top 
        #     (self.centerPoint[0] + width/2, self.centerPoint[1] - height/2),#right button
        #     ]
        self.MoveEdgePoint = self.StartEdgePoint

    def RectangleRotate(self,xita,centerpoint=[0,0]):
        # receptor format [(),(),(),()]
        if not centerpoint == self.centerPoint:
            self.centerPoint = centerpoint
            startEp = self.StartEdgePoint
            startEp = np.array(startEp)
            #[left button,left top,right top ,right button]
            self.centerArray = [
                (self.centerPoint[0] , self.centerPoint[1]),
                (self.centerPoint[0] , self.centerPoint[1]), 
                (self.centerPoint[0] , self.centerPoint[1]), 
                (self.centerPoint[0] , self.centerPoint[1])
                ]

            self.RectanglePoint = [
                (- width/2, - height/2),
                (- width/2,  height/2),
                ( width/2,  height/2),
                ( width/2, - height/2)
                ]

            # calculate start edge point
            ceter_temp = np.array(self.centerArray)
            rectangle_temp = np.array(self.RectanglePoint)
            point_temp = ceter_temp + rectangle_temp
            point_temp = np.matrix.tolist(point_temp)
            
            temp = list()
            for i in range(len(point_temp)):
                temp.append(tuple(point_temp[i]))
            self.StartEdgePoint = temp
        
        # self.RotatePoint
        self.rotateAngle = xita   # rotate angle
        # transition matrix
        rotateMatrix = [
            (cos(self.rotateAngle),sin(self.rotateAngle)),
            (-sin(self.rotateAngle),cos(self.rotateAngle))]
        rotateMatrix = np.array(rotateMatrix)
        cnt = 0
        for i in self.StartEdgePoint:
            self.MoveEdgePoint[cnt] = tuple(np.matrix.tolist(np.dot(np.array(i),rotateMatrix)))
            cnt += 1
        ret = (self.MoveEdgePoint)
        # ret.append((0,0))
        return ret
    
    def RectangleReset(self):
        ret = self.StartEdgePoint
        # ret.append((0,0))
        return ret

"""
    trapzoid location handle
    performance of nozzle
    follow_height = 5  # 跟随高度 mm
    height_nozzle = 15 # 喷嘴长度 mm
    angle_nozzle = 80  # 斜面角度 °
    r = 2              # 喷嘴出光口直径 mm
    default :NozzlePara = [5,width/3,80,width/5]
"""
class TrapzoidUpdate():
    def __init__(self,follow_height = 5,height = 5,angle = 80,botCenterpoint=[0,10],r = 2):
        # r - radius 
        self.follow_height = follow_height
        self.height = height
        self.angle = angle
        # bullshit 
        self.StartEdgePoint = list()
        self.botCenterpoint = botCenterpoint
        self.botCenterpoint[1] = botCenterpoint[1] + self.follow_height
        self.botcenterArray = [
            (self.botCenterpoint[0] , self.botCenterpoint[1]), 
            (self.botCenterpoint[0] , self.botCenterpoint[1]),
            (self.botCenterpoint[0] , self.botCenterpoint[1]),
            (self.botCenterpoint[0] , self.botCenterpoint[1])
            ]
        
        temp_1 = height/np.tan(angle*2*np.pi/360)
        self.TrapzoidPoint = [
            (- r/2, 0), 
            (- r/2 - temp_1,  height),
            ( r/2 + temp_1,  height),
            ( r/2, 0)
            ]

        # calculate start edge point
        ceter_temp = np.array(self.botcenterArray)
        Trapzoid_temp = np.array(self.TrapzoidPoint)
        point_temp = ceter_temp + Trapzoid_temp
        point_temp = np.matrix.tolist(point_temp)
        
        starttemp = []
        for i in range(len(point_temp)):
            starttemp.append(tuple(point_temp[i]))
        self.StartEdgePoint = starttemp
        self.MoveEdgePoint = self.StartEdgePoint

    def TrapzoidMove(self,botCenterpoint = [0,20]):
        b = self.StartEdgePoint
        # receptor format [(),(),(),()]
        if not botCenterpoint[1] + self.follow_height == self.botCenterpoint[1] and \
            not botCenterpoint[0] == self.botCenterpoint[0]:
            self.botCenterpoint = botCenterpoint
            startEp = self.StartEdgePoint
            startEp = np.array(startEp)
            self.botcenterArray = [
                (self.botCenterpoint[0] , self.botCenterpoint[1]),
                (self.botCenterpoint[0] , self.botCenterpoint[1]),
                (self.botCenterpoint[0] , self.botCenterpoint[1]),
                (self.botCenterpoint[0] , self.botCenterpoint[1])
            ]

            temp_1 = height/np.tan(angle*2*np.pi/360)
            self.TrapzoidPoint = [
                (- r/2, 0),
                (- r/2 - temp_1,  height),
                (r/2 + temp_1,  height),
                ( r/2, 0)
                ]
            # calculate start edge point
            ceter_temp = np.array(self.botcenterArray)
            Trapzoid_temp = np.array(self.TrapzoidPoint)
            point_temp = ceter_temp + Trapzoid_temp
            point_temp = np.matrix.tolist(point_temp)
            movetemp = []
            for i in range(len(point_temp)):
                movetemp.append(tuple(point_temp[i]))
            self.MoveEdgePoint = movetemp
        ret = self.MoveEdgePoint
        return ret
    
    def TrapzoidReset(self):
        ret = self.StartEdgePoint
        return ret


class QtSquare(QWidget):
    RectgBlock = RectangleUpdate()
    TrapBlock = TrapzoidUpdate()
    # program counter 
    cnt_1 = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rotation of magical love")
        self.rectangleCenterPoint = [0,0]
        self.trapzCenterPoint = [0,0]
        self.uistep()
        # self.UpdateBlocks()
        self.initTimers()
        self.initBlocks()

    def initTimers(self):
        print("start qtimer")
        # main timer of function 
        self.timer_1 = QTimer()
        self.timer_1.timeout.connect(self.updateplot_1)
        self.timer_1.timeout.connect(self.LocationUpdate)
        

    def uistep(self):
        mainlayout = QGridLayout()
        self.btn_start = QPushButton("start")
        self.btn_start.clicked.connect(self.startFun)
        self.btn_reset = QPushButton("clf")
        self.btn_reset.clicked.connect(self.stopFun)
        self.btn_pause = QPushButton("pause")
       
        # simulator show area
        self.simuArea = QWidget()
        simuAreaLayout = QGridLayout()
        self.monitor_1 = pg.PlotWidget(name='Plot1')
        self.monitor_2 = pg.PlotWidget(name='Plot2')
        self.monitor_3 = pg.PlotWidget(name='Plot3')

        self.monitor_1.p1 = self.monitor_3.plot()
        self.monitor_1.p1.setPen((32,205,255))
        
        #simulator motion show area
        self.MoveFigure = FigureCanvas(Figure(figsize=(6,4),dpi=100,facecolor='none'))
        self.MoveFigure.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.TubeAx = self.MoveFigure.figure.subplots()

        # add widget in area
        simuAreaLayout.addWidget(self.monitor_1,1,0)
        simuAreaLayout.addWidget(self.monitor_2,1,1)
        simuAreaLayout.addWidget(self.monitor_3,0,1)
        simuAreaLayout.addWidget(self.MoveFigure,0,0)
        self.simuArea.setLayout(simuAreaLayout)

        # add widget in area 
        mainlayout.addWidget(self.btn_start,0,0,1,1)
        mainlayout.addWidget(self.btn_pause,1,0,1,1)
        mainlayout.addWidget(self.btn_reset,2,0,1,1)
        mainlayout.addWidget(self.simuArea,0,1,20,20)

        self.setLayout(mainlayout)
        self.resize(800,600)

    # Initialization motion blocks of simulator
    def initBlocks(self):
        self.UpdateBlocks(self.RectgBlock.RectangleReset(),self.TrapBlock.TrapzoidReset())

    def LocationUpdate(self):
        # rotate_angle = np.random.randint(0,360,size=1,dtype=int)
        rotate_angle = int(self.cnt_1%360)
        self.UpdateBlocks(self.RectgBlock.RectangleRotate(xita = rotate_angle),self.TrapBlock.TrapzoidReset())

    def updateplot_1(self):
        xd = np.linspace(0,2*np.pi,num=100)
        # w =  10*np.random.rand()
        w = self.cnt_1%60
        yd = np.sin(w*xd)    
        self.monitor_1.p1.setData(y=yd,x=xd)
        if self.cnt_1 > 720000:
            self.cnt_1 = 0
        else:
            self.cnt_1 += 1

    def startFun(self):
        self.timer_1.start(100)

    def stopFun(self):
        self.timer_1.stop()

    # update motion blocks
    def UpdateBlocks(self,verts_block,verts_trapze):
        # matplotlib path patch property
        self.codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY
        ]
        # clear figure
        self.MoveFigure.figure.clf()
        # subplots , & add_subplot
        self.TubeAx = self.MoveFigure.figure.subplots()
        # set patch 
        verts_blockTemp = verts_block + [(0,0)]
        verts_trapzeTemp = verts_trapze + [(0,0)] 
        self.TubeRect = PathPatch(Path(verts_blockTemp,self.codes), \
            facecolor='#a7a7a7',edgecolor='#2b0201')
        self.TrapRect = PathPatch(Path(verts_trapzeTemp,self.codes), \
            facecolor='#a7a7a7',edgecolor='#2b0201')
        
        # set the figure axis
        self.TubeAx.set_xlim(-1*self.RectgBlock.width*1.5,self.RectgBlock.width*1.5)
        self.TubeAx.set_ylim(-1*self.RectgBlock.width*1.5,self.RectgBlock.width*1.5)
        self.TubeAx.set_aspect(1)
        
        # add patch of rectangle & trapzoid
        self.TubeAx.add_patch(self.TubeRect)
        self.TubeAx.add_patch(self.TrapRect)
        # update - figure 
        self.MoveFigure.figure.canvas.draw()


if __name__ == "__main__":
    if True:
        app = QApplication(sys.argv)
        ex = QtSquare()
        ex.show()
        sys.exit(app.exec_())
    # ex = RectangleUpdate()
    # ex.RectangleRotate(30)
    # debuga = 1