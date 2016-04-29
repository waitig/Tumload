# -*- coding: utf-8 -*-
# coding=utf-8
from PyQt4.QtGui import *
import time
import pyqt_rc


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QPixmap(':/tumload.png'))  # 启动程序的图片

    # 效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def effect(self):
        print 'In effect'
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() + 0.02  # 设置淡入
            if newOpacity > 1:
                break

            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.01)
        self.setWindowOpacity(1)
        self.show()
        print 'end effect'
