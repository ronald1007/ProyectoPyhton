# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #NUEVO---------------------------------------------
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 20, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 40, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 60, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 80, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 100, 31, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(700, 120, 31, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 140, 31, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 160, 31, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(700, 180, 31, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(700, 200, 31, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_10.setPalette(palette)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(700, 220, 31, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(700, 240, 31, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(730, 20, 31, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(730, 60, 31, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(730, 100, 31, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(730, 80, 31, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(730, 120, 31, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(730, 40, 31, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(730, 200, 31, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(730, 180, 31, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(730, 160, 31, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(730, 220, 31, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(730, 240, 31, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(730, 140, 31, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        
        
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(695, 10, 70, 261))
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.pushButton_16.raise_()
        self.pushButton_14.raise_()
        self.pushButton_21.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_8.raise_()
        self.pushButton_17.raise_()
        self.pushButton_24.raise_()
        self.pushButton_9.raise_()
        self.pushButton_12.raise_()
        self.pushButton_25.raise_()
        self.pushButton_19.raise_()
        self.pushButton_13.raise_()
        self.pushButton_20.raise_()
        self.pushButton.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_4.raise_()
        self.pushButton_18.raise_()
        self.pushButton_23.raise_()
        self.pushButton_5.raise_()
        self.pushButton_15.raise_()
        #--------------------------------------------------
        
        
        self.campoIngresa = QtWidgets.QTextEdit(self.centralwidget)
        self.campoIngresa.setGeometry(QtCore.QRect(30, 40, 661, 221))
        self.campoIngresa.setObjectName("campoIngresa")
        self.campoSalida = QtWidgets.QTextEdit(self.centralwidget)
        self.campoSalida.setGeometry(QtCore.QRect(30, 310, 661, 211))
        self.campoSalida.setObjectName("campoSalida")
        self.botonStart = QtWidgets.QPushButton(self.centralwidget)
        self.botonStart.setGeometry(QtCore.QRect(250, 0, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Documents/NetBeansProjects/ProyectoPyhton/pruebaPython/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonStart.setIcon(icon)
        self.botonStart.setObjectName("botonStart")
        self.botonDebug = QtWidgets.QPushButton(self.centralwidget)
        self.botonDebug.setGeometry(QtCore.QRect(350, 0, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Documents/NetBeansProjects/ProyectoPyhton/pruebaPython/debug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonDebug.setIcon(icon1)
        self.botonDebug.setObjectName("botonDebug")
        self.botonStep = QtWidgets.QPushButton(self.centralwidget)
        self.botonStep.setGeometry(QtCore.QRect(440, 0, 93, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Documents/NetBeansProjects/ProyectoPyhton/pruebaPython/foward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonStep.setIcon(icon2)
        self.botonStep.setObjectName("botonStep")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbrir_Archivo = QtWidgets.QMenu(self.menubar)
        self.menuAbrir_Archivo.setObjectName("menuAbrir_Archivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setIcon(icon)
        self.actionStart.setObjectName("actionStart")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setIcon(icon1)
        self.actionDebug.setObjectName("actionDebug")
        self.menuAbrir_Archivo.addAction(self.actionAbrir)
        self.menuAbrir_Archivo.addAction(self.actionGuardar)
        self.menuAbrir_Archivo.addAction(self.actionCerrar)
        self.menuEditar.addAction(self.actionStart)
        self.menuEditar.addAction(self.actionDebug)
        self.menubar.addAction(self.menuAbrir_Archivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        
        
        self.botonStart.clicked.connect(self.leerLineaPorLinea) #********************************************
        self.actionAbrir.triggered.connect(self.openFileNameDialog)
        self.actionGuardar.triggered.connect(self.guardarArchivoDeTexto)
        #self.actionAbrir.clicked.connect(self.openFileNameDialog) #********************************************
        
        #self.openFileNameDialog()
        
        
        self.retranslateUi(MainWindow)
        self.actionCerrar.triggered.connect(MainWindow.close)

        #self.actionAbrir.triggered.connect(self.openFileNamesDialog)
        #self.actionAbrir.triggered.connect(self.saveFileDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonStart.setText(_translate("MainWindow", "Start"))
        self.botonDebug.setText(_translate("MainWindow", "Debug"))
        self.botonStep.setText(_translate("MainWindow", "Step"))
        self.menuAbrir_Archivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionStart.setText(_translate("MainWindow", "Play"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
    
        #NUEVO----------------------------------------------------------
        self.pushButton.setText(_translate("MainWindow", "α"))
        self.pushButton_2.setText(_translate("MainWindow", "β"))
        self.pushButton_3.setText(_translate("MainWindow", "γ"))
        self.pushButton_4.setText(_translate("MainWindow", "δ"))
        self.pushButton_5.setText(_translate("MainWindow", "ε"))
        self.pushButton_6.setText(_translate("MainWindow", "ζ"))
        self.pushButton_7.setText(_translate("MainWindow", "η"))
        self.pushButton_8.setText(_translate("MainWindow", "θ"))
        self.pushButton_9.setText(_translate("MainWindow", "ι"))
        self.pushButton_10.setText(_translate("MainWindow", "κ"))
        self.pushButton_11.setText(_translate("MainWindow", "λ"))
        self.pushButton_12.setText(_translate("MainWindow", "μ"))
        self.pushButton_13.setText(_translate("MainWindow", "ν"))
        self.pushButton_14.setText(_translate("MainWindow", "ξ"))
        self.pushButton_15.setText(_translate("MainWindow", "ο"))
        self.pushButton_16.setText(_translate("MainWindow", "π"))
        self.pushButton_17.setText(_translate("MainWindow", "ρ"))
        self.pushButton_18.setText(_translate("MainWindow", "σ"))
        self.pushButton_19.setText(_translate("MainWindow", "τ"))
        self.pushButton_20.setText(_translate("MainWindow", "υ"))
        self.pushButton_21.setText(_translate("MainWindow", "φ"))
        self.pushButton_23.setText(_translate("MainWindow", "χ"))
        self.pushButton_24.setText(_translate("MainWindow", "ψ"))
        self.pushButton_25.setText(_translate("MainWindow", "ω"))
      
        #print(self.pushButton.text())
        #self.campoIngresa.clicked.connect(self.leerLineaPorLinea)
        self.pushButton.clicked.connect(self.imprimir1)
        self.pushButton_2.clicked.connect(self.imprimir2)
        self.pushButton_3.clicked.connect(self.imprimir3)
        self.pushButton_4.clicked.connect(self.imprimir4)
        self.pushButton_5.clicked.connect(self.imprimir5)
        self.pushButton_6.clicked.connect(self.imprimir6)
        self.pushButton_7.clicked.connect(self.imprimir7)
        self.pushButton_8.clicked.connect(self.imprimir8)
        self.pushButton_9.clicked.connect(self.imprimir9)
        self.pushButton_10.clicked.connect(self.imprimir10)
        self.pushButton_11.clicked.connect(self.imprimir11)
        self.pushButton_12.clicked.connect(self.imprimir12)
        self.pushButton_13.clicked.connect(self.imprimir13)
        self.pushButton_14.clicked.connect(self.imprimir14)
        self.pushButton_15.clicked.connect(self.imprimir15)
        self.pushButton_16.clicked.connect(self.imprimir16)
        self.pushButton_17.clicked.connect(self.imprimir17)
        self.pushButton_18.clicked.connect(self.imprimir18)
        self.pushButton_19.clicked.connect(self.imprimir19)
        self.pushButton_20.clicked.connect(self.imprimir20)
        self.pushButton_21.clicked.connect(self.imprimir21)
        self.pushButton_23.clicked.connect(self.imprimir22)
        self.pushButton_24.clicked.connect(self.imprimir23)
        self.pushButton_25.clicked.connect(self.imprimir24)
        
        self.botonStart.clicked.connect(self.leerLineaPorLinea)
        #-----------------------------
#    def openFileNameDialog(self):    
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        fileName, _ = QFileDialog.getOpenFileName(self,QFileDialog.getOpenFileName(), "","All Files (*);;Python Files (*.py)", options=options)
#        if fileName:
#            print(fileName)
        
#    def openFileNameDialog(self):
#        print("adjuntando")
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        fileName, _ = QFileDialog.getOpenFileName(self,QFileDialog.getOpenFileName(), "","Text Files (*.txt)", options=options)
#        if fileName:
#           print(fileName)

    def imprimir1(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton.text())
    def imprimir2(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_2.text())
    def imprimir3(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_3.text())
    def imprimir4(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_4.text())
    def imprimir5(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_5.text())
    def imprimir6(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_6.text())
    def imprimir7(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_7.text())
    def imprimir8(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_8.text())
    def imprimir9(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_9.text())
    def imprimir10(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_10.text())
    def imprimir11(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_11.text())
    def imprimir12(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_12.text())
    def imprimir13(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_13.text())
    def imprimir14(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_14.text())
    def imprimir15(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_15.text())
    def imprimir16(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_16.text())
    def imprimir17(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_17.text())
    def imprimir18(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_18.text())
    def imprimir19(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_19.text())
    def imprimir20(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_20.text())
    def imprimir21(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_21.text())
    def imprimir22(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_23.text())
    def imprimir23(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_24.text())
    def imprimir24(self):
        self.campoIngresa.setText(self.campoIngresa.toPlainText() + self.pushButton_25.text())


        
    
    def guardarArchivoDeTexto(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        encoding = 'utf8'
        fileName, _ = QFileDialog.getSaveFileName(None,"Guardar", " ","All Files (*)", options=options)
        #fileName, _ = QFileDialog.getSaveFileName(None,"Guardar", " ","All Files (*)").decode('utf-8')
        #if fileName:
        #    print(fileName)
        #print(fileName)
        #cadena = []
        if fileName:
            with open(fileName, 'w',encoding=encoding) as f:
                texto = self.campoSalida.toPlainText()
                #cadena.append(texto)
                #texto2 = texto.decode('utf-8', 'ignore')
                #print(texto2)
                #u = unicode(texto, "utf-8")
                #print(u)
                f.write(texto)
                #f.write(unicode_string.encode('utf8'))
                #f.write(self.text_edit.toPlainText())
        #print(cadena)
    
    
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        encoding = 'utf8'

        fileName, _ = QFileDialog.getOpenFileName(None,"Abrir", " ","All Files (*)", options=options)
            #if fileName:
            #    print(fileName)

        if fileName:
            f = open(fileName, 'r',encoding=encoding)

            with f:
                data = f.read()
                self.campoIngresa.setText(data)
                f.close()
        
    #dialog.getOpenFileName(None, "Window name", "", "CSV files (*.csv)")
    
    
    
    
    def openFileNamesDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
 
    def saveFileDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
  
    
    
    def leerLineaPorLinea(self):
            lines = (self.campoIngresa.toPlainText()).split('\n')
            
            #separaEspacios = (self.campoIngresa.toPlainText()).split(' ')
            #print(len(lines))
            self.comentarios = []
            self.symbols = []
            self.var = []
            self.markers = []
            
            self.simbolsSepadaras = []
            self.reglasSeparadasPorFlecha = []
            self.reglasBeforeArrow = []
            self.reglasAfterArrow = []
            
            self.hileraUsuario = [] #ir guardando en cada posicion la hilera nueva que se crea!
            self.reglasQueUsa = []
            
            for i in range(0, len(lines)):
                if lines[i]: #Si no es vacio el campo     if pone un enter en el texto
                    letras = [word[0] for word in lines[i]]
                    
                    if letras[0] == "%": 
                                        self.comentarios.append(lines[i])
                    elif letras[0] == "#": 
                                        primera = (lines[i].split(" "))
                                        #print(primera[0])
                                        if primera[0] == "#symbols":
                                            self.symbols = primera[1]
                                            #print(self.symbols)
                                        if primera[0] == "#vars":
                                            self.var = primera[1]
                                            #print(self.var[0])
                                        if primera[0] == "#markers":
                                            self.markers = primera[1]
                                            #print(self.markers)
                                            #print(self.symbols) #primera[0] = #simbol   primera[1] = abcdefg
                                        #VERIFICAR SI ES UN SIMBOLO O MARKERS Y GUARDARLA EN UNA NUEVA VARIABLE "GLOBAL

                    else:
                        
                        if '>' in letras :
                            banderaReglasConSentido = 0
                            reglasBuenasBA = 0
                            reglasBuenasAA = 0
                            banderaReglasConSentidoDespuesFlecha = 0
                            sinEspacios = lines[i].replace(" ", "")
                            self.reglasSeparadasPorFlecha = (sinEspacios).split('->')
                            verificaBA = self.reglasSeparadasPorFlecha[0]
                            verificaAA = self.reglasSeparadasPorFlecha[1]
                            for varRegl in range(0 , len(verificaBA)):      #verificaVarsBA = reglas antes de la flecha
                                                      #1 = 1
                                for v in range(0 , len(self.var)):              #total de vars, ejm: abdcefgh
                                    if verificaBA[varRegl] == self.var[v]:      #recorre todas las vars y verifica si esta ahi
                                        banderaReglasConSentido = banderaReglasConSentido+5
                                        reglasBuenasBA = reglasBuenasBA+1
                                    else:
                                        banderaReglasConSentido = banderaReglasConSentido+0

                                for s in range(0 , len(self.markers)):           #total de markers, ejm: BG
                                    if verificaBA[varRegl] == self.markers[s]:   #recorre todas las markers y verifica si esta ahi
                                        banderaReglasConSentido = banderaReglasConSentido+5
                                        reglasBuenasBA = reglasBuenasBA+1
                                    else:
                                        banderaReglasConSentido = banderaReglasConSentido+0
                                        
                            for varRegl in range(0 , len(verificaAA)):      #verificaVarsBA = reglas antes de la flecha

                                for v in range(0 , len(self.var)):              #total de vars, ejm: abdcefgh
                                    if verificaAA[varRegl] == self.var[v]:      #recorre todas las vars y verifica si esta ahi
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+5
                                        reglasBuenasAA = reglasBuenasAA+1
                                    else:
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+0

                                for s in range(0 , len(self.markers)):           #total de markers, ejm: BG
                                    if verificaAA[varRegl] == self.markers[s]:   #recorre todas las markers y verifica si esta ahi
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+5
                                        reglasBuenasAA = reglasBuenasAA+1
                                    else:
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+0   
                            if len(verificaBA) == reglasBuenasBA and len(verificaAA) == reglasBuenasAA:      
                                self.reglasBeforeArrow.append(self.reglasSeparadasPorFlecha[0])
                                self.reglasAfterArrow.append(self.reglasSeparadasPorFlecha[1])
                            else:
                                self.reglasBeforeArrow.append("INCORRECTO")
                                self.reglasAfterArrow.append("INCORRECTO")
                            #print(self.reglasBeforeArrow)
                        elif '?' in letras :   
                            print("reglasSeparadasPorFlecha")
                            banderaReglasConSentido = 0
                            reglasBuenasBA = 0
                            reglasBuenasAA = 0
                            sinEspacios2 = lines[i].replace(" ", "")
                            self.reglasSeparadasPorFlecha = (sinEspacios2).split('?')
                            verificaBA = self.reglasSeparadasPorFlecha[0]
                            verificaAA = self.reglasSeparadasPorFlecha[1]
                            print(reglasSeparadasPorFlecha)
                            for varRegl in range(0 , len(verificaBA)):      #verificaVarsBA = reglas antes de la flecha
                                                      #1 = 1
                                for v in range(0 , len(self.var)):              #total de vars, ejm: abdcefgh
                                    if verificaBA[varRegl] == self.var[v]:      #recorre todas las vars y verifica si esta ahi
                                        banderaReglasConSentido = banderaReglasConSentido+5
                                        reglasBuenasBA = reglasBuenasBA+1
                                    else:
                                        banderaReglasConSentido = banderaReglasConSentido+0

                                for s in range(0 , len(self.markers)):           #total de markers, ejm: BG
                                    if verificaBA[varRegl] == self.markers[s]:   #recorre todas las markers y verifica si esta ahi
                                        banderaReglasConSentido = banderaReglasConSentido+5
                                        reglasBuenasBA = reglasBuenasBA+1
                                    else:
                                        banderaReglasConSentido = banderaReglasConSentido+0
                                        
                            for varRegl in range(0 , len(verificaAA)):      #verificaVarsBA = reglas antes de la flecha

                                for v in range(0 , len(self.var)):              #total de vars, ejm: abdcefgh
                                    if verificaAA[varRegl] == self.var[v]:      #recorre todas las vars y verifica si esta ahi
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+5
                                        reglasBuenasAA = reglasBuenasAA+1
                                    else:
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+0

                                for s in range(0 , len(self.markers)):           #total de markers, ejm: BG
                                    if verificaAA[varRegl] == self.markers[s]:   #recorre todas las markers y verifica si esta ahi
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+5
                                        reglasBuenasAA = reglasBuenasAA+1
                                    else:
                                        banderaReglasConSentidoDespuesFlecha = banderaReglasConSentidoDespuesFlecha+0   
                            if len(verificaBA) == reglasBuenasBA and len(verificaAA) == reglasBuenasAA:      
                                self.reglasBeforeArrow.append(self.reglasSeparadasPorFlecha[0])
                                self.reglasAfterArrow.append(self.reglasSeparadasPorFlecha[1])
                            
                            else:
                                self.reglasBeforeArrow.append("INCORRECTO")
                                self.reglasAfterArrow.append("INCORRECTO")
                        else:
                            self.hileraUsuario = lines[i] # puede ir en el if de arriba, de la flecha
            print(self.reglasBeforeArrow ,"->", self.reglasAfterArrow , "hilera del Usuario:",self.hileraUsuario)    
            #fin del for que guarda todas variables
    #------------------------------------------------------------------------------------------------------------------
    #--------------------READY TO RUMBLEEEEEEEEE,  FALTA VERIFICAR IF VARIABLES SON SIMBOLOS, x=a----------------------
#            self.hileraPorLetras = [word[0] for word in self.hileraUsuario]#abcd = 
#            paso = 1
#            quedoEn = 0
#            reglasUso = []
#            letraAGuardar = []
#            pos = 0;
        #for gigante hasta el infito , hasta el terminal o While
            self.hileraPorLetras = [word[0] for word in self.hileraUsuario]#abcd = 
            for i in range(0, len(self.reglasBeforeArrow)): #xBx
                paso = 1
                quedoEn = 0
                reglasUso = []
                letraAGuardar = []
                datosARemplazar = []
                pos = 0;
                posicionesACambiar = []
                guardoVar = 0
                print("Reglas antrs flecha Todas: ",self.reglasBeforeArrow)
                separado = [word[0] for word in self.reglasBeforeArrow[i]]
                #print("Reglas de 0 separadas",separado)
                for k in range(0, len(separado)): #[x,B] , vars wxyz->abcdefg...
                    #print(separado[k])
                    if paso == 2:
                        for nuevo in range(quedoEn+1, len(self.hileraPorLetras)): #bcd
                            #for u in range(0, len(self.var)):   #var xyzw
                                if separado[k] in self.var :
                                    #print("var? paso2")
                                #if separado[k] == self.var[u]:   #x == x #solo verifica que este entre las variables
                                    for h in range(0, len(self.symbols)):    #recorre todo el abecedario
                                        if self.hileraPorLetras[nuevo] == self.symbols[h]:
                                            #print("entro a if de simbolos")
                                            quedoEn = nuevo
                                            paso = 2
                                            self.reglasQueUsa.append(separado[k]) #x
                                            reglasUso.append(separado[k])
                                            letraAGuardar.append(self.hileraPorLetras[nuevo]) #ab
                                            pos = nuevo
                                            posicionesACambiar.append(nuevo)
                                            break
                                    break        
                                else: #si es un marker
                                    #print("Markador? " ,separado[k],"Hilera: ",self.hileraPorLetras[nuevo])
                                    if self.hileraPorLetras[nuevo] == separado[k]: #a == a  for i sibolos, separado[i] == self.hileraPorLetras[n]
                                        quedoEn = nuevo
                                        paso = 2
                                        self.reglasQueUsa.append(separado[k]) #x
                                        reglasUso.append(separado[k])
                                        letraAGuardar.append(self.hileraPorLetras[nuevo]) #ab
                                        pos = nuevo
                                        posicionesACambiar.append(nuevo)
                                        break
                                    break
                    if paso == 1:   
                        for n in range(0, len(self.hileraPorLetras)): #aBc
                            #for u in range(0, len(self.var)): #var xyzw
                                #if separado[k] == self.var[u]:   #x == x #solo verifica que este entre las variables
                                #print(separado[k], "Hilera0:",self.hileraPorLetras[n])
                                if separado[k] in self.var :
                                    #print("entro a si en un var")
                                    #print(separado[k])
                                    for h in range(0, len(self.symbols)):    #recorre todo el abecedario
                                        if self.hileraPorLetras[n] == self.symbols[h]:
                                            #print("Entro a if")
                                            quedoEn = n
                                            paso = 2
                                            self.reglasQueUsa.append(separado[k]) #x
                                            reglasUso.append(separado[k])
                                            letraAGuardar.append(self.hileraPorLetras[n]) #ab
                                            pos = n
                                            posicionesACambiar.append(n)
                                            break
                                        #for    
                                    break
                                else: #si es un marker
                                    #print("Sirvio",self.hileraPorLetras[n])
                                    if self.hileraPorLetras[n] == separado[k]: #a == a  for i sibolos, separado[i] == self.hileraPorLetras[n]
                                        quedoEn = n
                                        paso = 2
                                        self.reglasQueUsa.append(separado[k]) #x
                                        reglasUso.append(separado[k])
                                        letraAGuardar.append(self.hileraPorLetras[n]) #ab
                                        pos = n
                                        posicionesACambiar.append(n)
                                        break
                                    break 
                                    
                separaRegla = [word[0] for word in self.reglasBeforeArrow[i]]
                print(separaRegla," == ",reglasUso)
                if separaRegla == reglasUso: #verifica la regla que se esta usando, para agarrar la after arrow de esa
                    print("Entra a reglas iguales")
                    for r in range(0, len(self.reglasAfterArrow[i])): #xB
                        guardoVar = 0
                        tuanis = self.reglasAfterArrow[i] #tuanis[i] = x
                        for f in range(0, len(self.var)):
                            if tuanis[r] == self.var[f]:
                                for y in range(0, len(letraAGuardar)):
                                    datosARemplazar = letraAGuardar[y]
                                    letraAGuardar.remove(letraAGuardar[y])
                                    guardoVar = 1
                                    print("AQUIII")  
                                    break
                        if guardoVar != 1 : #si es un marker
                            print(tuanis[r])
                            print(posicionesACambiar)
                            est=0
                            bande = 0
                            for s in range(0, len(posicionesACambiar)):
                                for e in range(est, len(tuanis)):
                                    print("Tamano",len(tuanis))
                                    print("Tuanis: ",tuanis[e])
                                    self.hileraPorLetras[posicionesACambiar[s]] = tuanis[e]  #Bx
                                    #print(hileraPorLetras)
                                    bande = 1
                                    est = est+1
                                    break
                                if bande == 1:
                                    del self.hileraPorLetras[posicionesACambiar[s]]
                                    
                                    #tuanis.remove(tuanis[e])
                                   
#                                    if len(tuanis)>1:
#                                        print("Sigue?")
#                                        self.hileraPorLetras[posicionesACambiar[s]] = tuanis[e]
#                                        est = est+1
#                                        #tuanis.remove(tuanis[e])
#                                        print("DEMENTE") 
#                                        #pass
#                                    else:
#                                        self.hileraPorLetras[posicionesACambiar[s]] = tuanis[e]
                                    #self.hileraPorLetras.remove(self.hileraPorLetras[s])
                                #aB
                                #a0 b1 c2 d3
                                #[aB]0 [b]1 [c]2 [c]3
                                print("FORANTSW")  
                            print("Sigue en for")  
                            #self.hileraPorLetras[posicionesACambiar[0]] = tuanis[r] # si es un marker = Beta,Alpha...
                    #print("Antes:",self.hileraPorLetras,"Pos: ",self.hileraPorLetras[pos])
                    #self.hileraPorLetras[pos] = datosARemplazar
                    print("Despues:",self.hileraPorLetras)          
                            
                        
                    #remplazo
                    #break
                #print(separaRegla, "Guardo: ",reglasUso)    
            
            print(letraAGuardar," reglasQueUsa:",self.reglasQueUsa)
        #-------------------LO DEL REMPLAZO ESTA EN PSEUDOCODIGO, TENGO QUE PASARLO A PYTHON-----------------
                #HACER REMPLAZO AQUI
                #for k de self.reglasBeforeArrow
                    #if reglasUso == self.reglasBeforeArrow[k] #
                        #lo que agarro arriba LETRA = a
                        #lo que agarro arriba pos = 0
                        #desde aqui------>
                        #for j de self.reglasAfterArrow[k]
                            #tuanis = self.reglasAfterArrow[k] # tuanis[j] = x
                            #for n de todas las variables, var
                                #if tuanis[j] = var[n] #si es una variable, osea xyz
                                    #for m de letraAGuardar
                                    #datosARemplazar = letraAGuardar[m]
                                    #letraAGuardar.remove(letraAGuardar[m])
                                    #CREOQUENAAAAHHH  hileraporletras[pos] = LETRA #a
                                    #guardoUnaVar = 1
                                    #break;
                            #if guardoUnaVar != 1 : #si es un marker
                                #hileraporletras[pos] = tuanis[j] # si es un marker = Beta,Alpha...
                        #hileraporletras[pos] = datosARemplazar #= aB
    #x->Bx  
    #abcd
    #
   #------------------------------------------------------------------------------------

                        

if __name__ == "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
      
    sys.exit(app.exec_())
    
    
    
