# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import loadfile
import analizefile
from viewreports import *
import mensaje
class Ui_SMARTWATCH_WINDOW(object):
    def setupUi(self, SMARTWATCH_WINDOW):
        SMARTWATCH_WINDOW.setObjectName("SMARTWATCH_WINDOW")
        SMARTWATCH_WINDOW.setWindowModality(QtCore.Qt.NonModal)
        SMARTWATCH_WINDOW.resize(1100, 608)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        SMARTWATCH_WINDOW.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../IPC2 E/LAB IPC2 E/Users/Sr. C/Users/Sr. C/Pictures/FACING.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SMARTWATCH_WINDOW.setWindowIcon(icon)
        SMARTWATCH_WINDOW.setLayoutDirection(QtCore.Qt.LeftToRight)
        SMARTWATCH_WINDOW.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(SMARTWATCH_WINDOW)
        self.centralwidget.setObjectName("centralwidget")
        self.LABEL_BACKGROUND = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_BACKGROUND.setGeometry(QtCore.QRect(0, -100, 1165, 771))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.LABEL_BACKGROUND.setFont(font)
        self.LABEL_BACKGROUND.setMidLineWidth(-1)
        self.LABEL_BACKGROUND.setText("")
        self.LABEL_BACKGROUND.setTextFormat(QtCore.Qt.AutoText)
        # self.LABEL_BACKGROUND.setPixmap(QtGui.QPixmap("images/giphy.gif"))
        self.LABEL_BACKGROUND.setScaledContents(True)
        self.LABEL_BACKGROUND.setObjectName("LABEL_BACKGROUND")
        self.movie2=QMovie("images/giphy.gif")
        self.LABEL_BACKGROUND.setMovie(self.movie2)
        self.movie2.start()

        self.lbl_myicon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_myicon.setGeometry(QtCore.QRect(1030, 475, 85, 85))
        self.lbl_myicon.setText("")
        self.lbl_myicon.setPixmap(QtGui.QPixmap("images/logo.gif"))
        self.lbl_myicon.setScaledContents(True)
        self.lbl_myicon.setObjectName("lbl_myicon")
        self.movie3=QMovie("images/logo.gif")
        self.lbl_myicon.setMovie(self.movie3)
        self.movie3.start()
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(850, 30, 141, 31))
        self.combo.setObjectName("combo")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../IPC2 E/LAB IPC2 E/PROYECTO 2/Codigo Fuente/Codigo Fuente/images/Gear1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo.addItem(icon1, "Reportes")
        self.combo.addItem(icon1, "Tokens")
        self.combo.addItem(icon1, "Errores")
        self.combo.activated[str].connect(self.onChanged)
        self.btn_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrir.setGeometry(QtCore.QRect(610, 30, 111, 31))
        self.btn_abrir.setStyleSheet("font: 81 14pt \"JetBrains Mono ExtraBold\";\n"
        "\n"
        "border-color: rgb(255, 226, 56);\n"
        "\n"
        "")
        self.btn_abrir.clicked.connect(self.seteareltexto)
        self.btn_abrir.setObjectName("btn_abrir")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(910, 150, 101, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../../IPC2 E/LAB IPC2 E/PROYECTO 2/Codigo Fuente/Codigo Fuente/images/Gear1.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lbl_SMARTWATCH = QtWidgets.QLabel(self.centralwidget)
        self.lbl_SMARTWATCH.setGeometry(QtCore.QRect(40, 30, 371, 71))
        self.lbl_SMARTWATCH.setText("")
        self.lbl_SMARTWATCH.setPixmap(QtGui.QPixmap("../../../../../IPC2 E/LAB IPC2 E/PROYECTO 2/Codigo Fuente/Codigo Fuente/images/cooltext392345411513032.gif"))
        self.lbl_SMARTWATCH.setScaledContents(True)
        self.lbl_SMARTWATCH.setObjectName("lbl_SMARTWATCH")
        self.lbl_BRAZOROBOTICO = QtWidgets.QLabel(self.centralwidget)
        self.lbl_BRAZOROBOTICO.setGeometry(QtCore.QRect(-90, 200, 361, 321))
        self.lbl_BRAZOROBOTICO.setText("")
        self.lbl_BRAZOROBOTICO.setPixmap(QtGui.QPixmap("../../../../../IPC2 E/LAB IPC2 E/PROYECTO 2/Codigo Fuente/Codigo Fuente/images/robot.gif"))
        self.lbl_BRAZOROBOTICO.setScaledContents(True)
        self.lbl_BRAZOROBOTICO.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_BRAZOROBOTICO.setObjectName("lbl_BRAZOROBOTICO")
        self.lbl_tittle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tittle.setGeometry(QtCore.QRect(10, 20, 501, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_tittle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_tittle.setFont(font)
        self.lbl_tittle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_tittle.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 20pt \"Snap ITC\";")
        self.lbl_tittle.setText("")
        self.lbl_tittle.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_tittle.setPixmap(QtGui.QPixmap("images/cooltext394206444786594.png"))
        self.lbl_tittle.setScaledContents(True)
        self.lbl_tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tittle.setWordWrap(False)
        self.lbl_tittle.setOpenExternalLinks(False)
        self.lbl_tittle.setObjectName("lbl_tittle")
        self.lbl_procesorealizado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_procesorealizado.setGeometry(QtCore.QRect(590, 500, 321, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_procesorealizado.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_procesorealizado.setFont(font)
        self.lbl_procesorealizado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_procesorealizado.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_procesorealizado.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_procesorealizado.setScaledContents(True)
        self.lbl_procesorealizado.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_procesorealizado.setWordWrap(False)
        self.lbl_procesorealizado.setOpenExternalLinks(False)
        self.lbl_procesorealizado.setObjectName("lbl_procesorealizado")
        self.btn_analizar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analizar.setGeometry(QtCore.QRect(730, 30, 111, 31))
        self.btn_analizar.setObjectName("btn_analizar")
        self.btn_analizar.clicked.connect(self.analizarfile)
        self.lbl_procesorealizado_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_procesorealizado_2.setGeometry(QtCore.QRect(110, 500, 321, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_procesorealizado_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_procesorealizado_2.setFont(font)
        self.lbl_procesorealizado_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_procesorealizado_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_procesorealizado_2.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_procesorealizado_2.setScaledContents(True)
        self.lbl_procesorealizado_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_procesorealizado_2.setWordWrap(False)
        self.lbl_procesorealizado_2.setOpenExternalLinks(False)
        self.lbl_procesorealizado_2.setObjectName("lbl_procesorealizado_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(60, 90, 431, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plaintext_editar = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plaintext_editar.setGeometry(QtCore.QRect(0, 0, 431, 391))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.plaintext_editar.setFont(font)
        self.plaintext_editar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        "font: 63 11pt \"Lucida Sans Typewriter\";\n"
        "color: rgb(82, 247, 0);")
        self.plaintext_editar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.plaintext_editar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.plaintext_editar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plaintext_editar.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plaintext_editar.setObjectName("plaintext_editar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(530, 90, 550, 391))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 429, 389))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.plaintext_console = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plaintext_console.setGeometry(QtCore.QRect(0, 0, 550, 391))
        self.plaintext_console.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        "font: 63 11pt \"Lucida Sans Typewriter\"; color: rgb(247, 255, 0);")
        self.plaintext_console.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.plaintext_console.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plaintext_console.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plaintext_console.setObjectName("plaintext_console")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.btn_cleartext = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cleartext.setGeometry(QtCore.QRect(1000, 480, 81, 31))
        self.btn_cleartext.setStyleSheet("font: 81 14pt \"JetBrains Mono ExtraBold\";\n"        
        "\n"
        "\n"
        "border-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
        "\n"
        "")
        self.btn_cleartext.setObjectName("btn_cleartext")
        self.btn_cleartext.clicked.connect(self.cleartext)

        self.btn_recompile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_recompile.setGeometry(QtCore.QRect(500, 480, 120, 31))
        self.btn_recompile.setStyleSheet("font: 81 14pt \"JetBrains Mono ExtraBold\";\n"        
        "\n"
        "\n"
        "border-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 255, 1);\n"
        "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
        "\n"
        "")
        self.btn_recompile.setObjectName("btn_recompile")
        self.btn_recompile.clicked.connect(self.recompilar)

        self.btn_clearconsole = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clearconsole.setGeometry(QtCore.QRect(60, 480, 81, 31))
        self.btn_clearconsole.setStyleSheet("font: 81 14pt \"JetBrains Mono ExtraBold\";\n"
        "\n"
        "\n"
        "border-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
        "\n"
        "")
        self.btn_clearconsole.setObjectName("btn_clearconsole")
        self.btn_clearconsole.clicked.connect(self.clearconsole)
        self.lbl_tittle_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_reporte = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tittle_2.setGeometry(QtCore.QRect(960, 470, 91, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_tittle_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_tittle_2.setFont(font)
        self.lbl_tittle_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_tittle_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 20pt \"Snap ITC\";")
        self.lbl_tittle_2.setText("")
        self.lbl_tittle_2.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_tittle_2.setPixmap(QtGui.QPixmap("../../../../../../../Pictures/oie_25212249BZ616093.gif"))
        self.lbl_tittle_2.setScaledContents(True)
        self.lbl_tittle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tittle_2.setWordWrap(False)
        self.lbl_tittle_2.setOpenExternalLinks(False)
        self.lbl_tittle_2.setObjectName("lbl_tittle_2")
        SMARTWATCH_WINDOW.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SMARTWATCH_WINDOW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuCARGAR_ARCHIVOS = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menuCARGAR_ARCHIVOS.setFont(font)
        self.menuCARGAR_ARCHIVOS.setObjectName("menuCARGAR_ARCHIVOS")
        self.menuREPORTES = QtWidgets.QMenu(self.menubar)
        self.menuREPORTES.setObjectName("menuREPORTES")
        self.menuAYUDA = QtWidgets.QMenu(self.menubar)
        self.menuAYUDA.setObjectName("menuAYUDA")
        self.menuSALIR = QtWidgets.QMenu(self.menubar)
        self.menuSALIR.setObjectName("menuSALIR")
        SMARTWATCH_WINDOW.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SMARTWATCH_WINDOW)
        self.statusbar.setObjectName("statusbar")
        SMARTWATCH_WINDOW.setStatusBar(self.statusbar)
        self.actionARCHIVO_DE_CONFIGURACI_N = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionARCHIVO_DE_CONFIGURACI_N.setFont(font)
        self.actionARCHIVO_DE_CONFIGURACI_N.setObjectName("actionARCHIVO_DE_CONFIGURACI_N")
        self.actionARCHIVO_DE_SIMULACI_N = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionARCHIVO_DE_SIMULACI_N.setFont(font)
        self.actionARCHIVO_DE_SIMULACI_N.setObjectName("actionARCHIVO_DE_SIMULACI_N")
        self.actionREPORTE_DE_SIMULACI_N = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionREPORTE_DE_SIMULACI_N.setFont(font)
        self.actionREPORTE_DE_SIMULACI_N.setObjectName("actionREPORTE_DE_SIMULACI_N")
        self.actionREPORTE_DE_COLA_DE_SECUENCIA = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionREPORTE_DE_COLA_DE_SECUENCIA.setFont(font)
        self.actionREPORTE_DE_COLA_DE_SECUENCIA.setObjectName("actionREPORTE_DE_COLA_DE_SECUENCIA")
        self.actionINFORMACI_N_PERSONAL = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionINFORMACI_N_PERSONAL.setFont(font)
        self.actionINFORMACI_N_PERSONAL.setObjectName("actionINFORMACI_N_PERSONAL")
        self.actionACERCA_DE = QtWidgets.QAction(SMARTWATCH_WINDOW)
        self.actionACERCA_DE.setCheckable(False)
        self.actionSALIR = QtWidgets.QAction(SMARTWATCH_WINDOW)
        self.actionSALIR.setCheckable(False)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionACERCA_DE.setFont(font)
        self.actionACERCA_DE.setObjectName("actionACERCA_DE")
        self.actionSALIR.setFont(font)
        self.actionSALIR.setObjectName("actionSALIR")
        self.menuCARGAR_ARCHIVOS.addAction(self.actionARCHIVO_DE_CONFIGURACI_N)
        self.menuCARGAR_ARCHIVOS.addSeparator()
        self.menuCARGAR_ARCHIVOS.addAction(self.actionARCHIVO_DE_SIMULACI_N)
        self.menuCARGAR_ARCHIVOS.addSeparator()
        self.menuREPORTES.addAction(self.actionREPORTE_DE_SIMULACI_N)
        self.menuREPORTES.addSeparator()
        self.menuREPORTES.addAction(self.actionREPORTE_DE_COLA_DE_SECUENCIA)
        self.menuREPORTES.addSeparator()
        self.menuAYUDA.addAction(self.actionINFORMACI_N_PERSONAL)
        self.menuAYUDA.addSeparator()
        self.menuSALIR.addAction(self.actionSALIR)
        self.menuAYUDA.addAction(self.actionACERCA_DE)
        self.menuAYUDA.addSeparator()
        self.menubar.addAction(self.menuCARGAR_ARCHIVOS.menuAction())
        self.menubar.addAction(self.menuREPORTES.menuAction())
        self.menubar.addAction(self.menuAYUDA.menuAction())
        self.menubar.addAction(self.menuSALIR.menuAction())

        self.retranslateUi(SMARTWATCH_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(SMARTWATCH_WINDOW)
    def retranslateUi(self, SMARTWATCH_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        SMARTWATCH_WINDOW.setWindowTitle(_translate("SMARTWATCH_WINDOW", "MainWindow"))
        self.combo.setItemText(0, _translate("SMARTWATCH_WINDOW", "Reportes"))
        self.combo.setItemText(1, _translate("SMARTWATCH_WINDOW", "Tokens"))
        self.combo.setItemText(2, _translate("SMARTWATCH_WINDOW", "Errores"))
        
        self.btn_abrir.setText(_translate("SMARTWATCH_WINDOW", "ABRIR"))
        self.lbl_procesorealizado.setText(_translate("SMARTWATCH_WINDOW", "Consola"))
        self.btn_analizar.setText(_translate("SMARTWATCH_WINDOW", "ANALIZAR"))
        self.lbl_procesorealizado_2.setText(_translate("SMARTWATCH_WINDOW", "Editor de Texto"))
        self.btn_cleartext.setText(_translate("SMARTWATCH_WINDOW", "Clear"))
        self.btn_recompile.setText(_translate("SMARTWATCH_WINDOW", "RECOMPILAR"))
        self.btn_clearconsole.setText(_translate("SMARTWATCH_WINDOW", "Clear"))
        self.menuCARGAR_ARCHIVOS.setTitle(_translate("SMARTWATCH_WINDOW", "ARCHIVO"))
        self.menuREPORTES.setTitle(_translate("SMARTWATCH_WINDOW", "EDITAR"))
        self.menuAYUDA.setTitle(_translate("SMARTWATCH_WINDOW", "AYUDA"))
        self.menuSALIR.setTitle(_translate("SMARTWATCH_WINDOW", "SALIR"))
        self.actionARCHIVO_DE_CONFIGURACI_N.setText(_translate("SMARTWATCH_WINDOW", "ARCHIVO DE CONFIGURACIÓN"))
        self.actionARCHIVO_DE_SIMULACI_N.setText(_translate("SMARTWATCH_WINDOW", "ARCHIVO DE SIMULACIÓN"))
        self.actionREPORTE_DE_SIMULACI_N.setText(_translate("SMARTWATCH_WINDOW", "REPORTE DE SIMULACIÓN"))
        self.actionREPORTE_DE_COLA_DE_SECUENCIA.setText(_translate("SMARTWATCH_WINDOW", "REPORTE DE COLA DE SECUENCIA"))
        self.actionINFORMACI_N_PERSONAL.setText(_translate("SMARTWATCH_WINDOW", "INFORMACIÓN PERSONAL"))
        self.actionACERCA_DE.setText(_translate("SMARTWATCH_WINDOW", "ACERCA DE"))
    def seteareltexto(self):
        a=loadfile.loadfile()
        self.plaintext_editar.setPlainText(loadfile.file)
    def startAnimation(self):
        self.movie.start()
    def cleartext(self):
        self.plaintext_console.setPlainText("")
    def clearconsole(self):
        self.plaintext_editar.setPlainText("")
    def view_reports(self):
        try:
            v=viewreports()
            v.openTokensHTML()
            # v.openErroresHTML()
            print("VIENDO LOS REPORTES DE TOKENS")
        except :
            return
    def view_reports2(self):
        try:
            v2=viewreports()
            v2.openErroresHTML()
            print("VIENDO LOS REPORTES DE ERRORES")
        except :
            return
    def analizarfile(self):
        try:
            a=analizefile.analizefile()
            textconsole = a.analizar(loadfile.file)
            self.plaintext_console.setPlainText(textconsole)
            a.impTokens()
            a.impErrores()
            a.generarHTMLTokens()
            a.generarHTMLErrores()
        except:
            a=mensaje.App()
            a.initUI("Algo ocurrió")
    def recompilar(self):
        print("probando")
        thisfile=str(self.plaintext_editar.toPlainText())
        print(thisfile)
        print(thisfile)
        if thisfile!="":
            a=analizefile.analizefile()
            textconsole = a.analizar(thisfile)
            self.plaintext_console.setPlainText(textconsole)
            a.impTokens()
            a.impErrores()
            a.generarHTMLTokens()
            a.generarHTMLErrores()
        else:
            a=mensaje.App()
            a.initUI("La consola esta vacía")
    def onChanged(self, text):
        if text == "Tokens":
            self.view_reports()
        elif text=='Errores':
            self.view_reports2()
    def exit():
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SMARTWATCH_WINDOW = QtWidgets.QMainWindow()
    ui = Ui_SMARTWATCH_WINDOW()
    ui.setupUi(SMARTWATCH_WINDOW)
    SMARTWATCH_WINDOW.show()
    sys.exit(app.exec_())
