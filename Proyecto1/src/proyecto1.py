# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        
        #self.actionAbrir.clicked.connect(self.openFileNameDialog) #********************************************
        
        #self.openFileNameDialog()
        
        
        self.retranslateUi(MainWindow)
        self.actionCerrar.triggered.connect(MainWindow.close)
        self.actionAbrir.triggered.connect(self.openFileNameDialog)
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
        
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileNames()", " ","All Files (*)", options=options)
        #if fileName:
        #    print(fileName)
        
        if fileName:
            f = open(fileName, 'r')

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
            for i in range(0, len(lines)):
                letras = [word[0] for word in lines[i]]
                if letras[0] == "%": 
                                    self.comentarios.append(lines[i])
                elif letras[0] == "#": 
                                    primera = (lines[i].split(" "))
                                    #print(primera[0])
                                    if primera[0] == "#symbols":
                                        self.symbols = primera[1]
                                        print(self.symbols)
                                    if primera[0] == "#vars":
                                        self.var = primera[1]
                                        print(self.var)
                                    if primera[0] == "#markers":
                                        self.markers = primera[1]
                                        print(self.markers)
                                        #print(self.symbols) #primera[0] = #simbol   primera[1] = abcdefg
                                    #VERIFICAR SI ES UN SIMBOLO O MARKERS Y GUARDARLA EN UNA NUEVA VARIABLE "GLOBAL
                else:
                    if '>' in letras :
                        #print(lines[i]) #letras
                        #replace
                        sinEspacios = lines[i].replace(" ", "")
                        self.reglasSeparadasPorFlecha = (sinEspacios).split('->')
                        self.reglasBeforeArrow = self.reglasSeparadasPorFlecha[0] 
                        self.reglasAfterArrow = self.reglasSeparadasPorFlecha[1]
                        print(self.reglasBeforeArrow)
                    if '→' in letras :  
                        sinEspacios2 = lines[i].replace(" ", "")
                        self.reglasSeparadasPorFlecha = (sinEspacios2).split('→')
                        self.reglasBeforeArrow = self.reglasSeparadasPorFlecha[0] 
                        self.reglasAfterArrow = self.reglasSeparadasPorFlecha[1]
                        print(self.reglasBeforeArrow)
#                    self.hileraPorLetras = letras #[a,b,c,d]
#                    print(self.hileraPorLetras)   
#                    self.reglasBeforeArrow      #["βx", "xβ" , "x"]       
                                    
            
#                hileraPorLetras = (hilera.splitPorLetras) // [a,b,c,β,d]
#                //beforeArrow = ["βx", "xβ" , "x"]
#                paso=1
#                for(i , beforeArrow.length)  //3
#                separado = (beforeArrow[i].splitPorLetras)	//'β' y 'x'
#                        for(k , separado.length ) 	//['β' ,'x'] = ['β','d'] HILERA [abcβd]
#                                if (paso = 2) for nuevo in range(quedoEn , hileraPorLetras.length)
#                                                if (hileraPorLetras[nuevo] == separado[k]) //[a,b,c,β,d]
#                                                        quedoEn = nuevo
#                                                        reglaNueva = reglaNueva + separado[k] //x ->βx
#                                if(paso = 1) for n in range (0 , hileraPorLetras.length ) //[a,b,c,β,d]
#                                                if (hileraPorLetras[n] == separado[k])//β == β //abcβd-> β == β , == x
#                                                        quedoEn = n 	//3
#                                                        paso = 2
#                                                        reglaNueva = separado[k]//β
#                reglaNueva //βx		
                
                
                # self.symbols #tiene las varas separadas  abcdefghijklmnopqrstuvwxyz0123456789
#                self.var[0] #wxyz separados
#                for m in range(0,len(self.var))
#                    if(x == self.var[m]) #x es lo que ingresa el mae
                    #self.varsSepadaras 
                
                
#                if 0< notaAlumno <6:     print("Insuficiente") 
#                elif notaAlumno > 0 and notaAlumno<7:     print("Suficiente") 
#                elif notaAlumno > 0 and notaAlumno<8:     print("Bien") 
#                elif notaAlumno > 0 and notaAlumno<9:     print("Notable") 
#                else:     print("Sobresaliente")
            
#            for i in range( lines[0] ):
#                if(lines[0])
#            print("gola")
#            doc = self.campoIngresa.document()
#            block = doc.begin()
#            lines = [ block.text() ]
#            for i in range( 1, doc.blockCount() ):
#                block = block.next()
#                lines.append( block.text() 
                
            
            
	# data = campoIngresa.toPlainText()
	# print (data)
#    print('Selfsfd')
#    self.campoSalida.setText("Pla")
#    print('asd')
#    textboxValue = self.campoIngresa.toPlainText()
#    print('1122')
#    for pid in psutil.pids():  # Controlla se il processo è attivo
#        listapid = psutil.Process(pid)
#        if listapid.name() == textboxValue:
#            print('Processo trovato')
#    self.campoIngresa.clear()
#    self.campoIngresa.textCursor().insertHtml('normal text')    
  
        
        

if __name__ == "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
      
    sys.exit(app.exec_())
    
    
    