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
    #-------------------------------------------------------------------------------------------
#                    self.hileraPorLetras = letras #[a,b,c,d]
#                    print(self.hileraPorLetras)   
#                    self.reglasBeforeArrow      #["βx", "xβ" , "x"]  

    #HACER QUE X = ABCDEFGHI...
    #--------------------READY TO RUMBLEEEEEEEEE,  FALTA VERIFICAR IF VARIABLES SON SIMBOLOS, x=a----------------------
#            self.hileraPorLetras = [word[0] for word in self.hileraUsuario]#abcd = 
#            paso = 1
#            quedoEn = 0
#            reglasUso = []
#            letraAGuardar = []
#            for i in range(0, len(self.reglasBeforeArrow)): #xBx
#                separado = [word[0] for word in self.reglasBeforeArrow[i]]
#                for k in range(0, len(separado)): #[x,B] , vars wxyz->abcdefg...
#                    if paso == 2:
#                        for nuevo in range(quedoEn, len(self.hileraPorLetras)): #bcd
#                            if self.hileraPorLetras[nuevo] == separado[k]: 
#                                quedoEn = nuevo
#                                self.reglasQueUsa.append(separado[k])
#                                reglasUso.append(separado[k])
#                                letraAGuardar.append(self.hileraPorLetras[n]) 
#                                break
#                    if paso == 1:   
#                        for n in range(0, len(self.hileraPorLetras)): #aBc
#                            if self.hileraPorLetras[n] == separado[k]: #B=x for,B=x for, a=x if
#                                quedoEn = n
#                                paso = 2
#                                self.reglasQueUsa.append(separado[k]) #x
#                                reglasUso.append(separado[k])
#                                letraAGuardar.append(self.hileraPorLetras[n]) #ab
#                                #guardar self.hileraPorLetras[n] en variable =LETRA
#                                #y posicion =pos
#                                break
        #-------------------LO DEL REMPLAZO ESTA EN PSEUDOCODIGO, TENGO QUE PASARLO A PYTHON-----------------
                #HACER REMPLAZO AQUI
                #for k de self.reglasBeforeArrow
                    #if reglasUso == self.reglasBeforeArrow[k] #
                        #lo que agarro arriba LETRA = a
                        #lo que agarro arriba pos = 0
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
                        

if __name__ == "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
      
    sys.exit(app.exec_())
    
    
    
