# -*- coding: utf-8 -*-
"""
@author: Houssem ADOUNI
"""

from API.converter import Point
from PyQt4 import QtCore, QtGui

class Layout_conv(QtGui.QWidget):
    def __init__(self,parent):
        super(Layout_conv,self).__init__(parent)
        self.buttonBox = QtGui.QDialogButtonBox()
        #self.buttonBox.setGeometry(QtCore.QRect(200, 480, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QtGui.QWidget()
        #self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 80, 291, 181))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line_2)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_5 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_6 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.clicked.connect(self.run)
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.setLayout(self.verticalLayout)
        self.home()
    def home(self):
        self.label.setText("votre point")
        self.label_2.setText(u"SRID du départ")
        self.label_3.setText(u"SRID du destination")
        self.pushButton.setText(u"convertir")
        self.lineEdit.setText("X")
        self.lineEdit_2.setText("Y")

    def get_values(self):
        l=[]
        try:
            l.append(float(str(self.lineEdit.text())))
            l.append(float(str(self.lineEdit_2.text())))
            l.append(int(str(self.lineEdit_5.text())))
            l.append(int(str(self.lineEdit_6.text())))
            return l
        except:
            return -1
    def run(self):
        L=self.get_values()
        print L
        p1=Point((L[0],L[1]),L[2])
        p2=p1.convert_to(L[3])
        self.lineEdit_3.setText(str(p2.get_x()))
        self.lineEdit_4.setText(str(p2.get_y()))