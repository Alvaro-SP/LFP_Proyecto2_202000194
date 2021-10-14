import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
file=""
class loadfile(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'SELECCIONAR ARCHIVO'
        self.left = 400
        self.top = 150
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()

        # self.show()

    def openFileNameDialog(self):
        global file
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _= QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","lfp Files (*.lfp);;All Files (*)", options=options)

            # fileName=r"C:\Users\Sr. C\Google Drive\C U A R T O  S E M E S T R E\L F P  B+\LAB  LFP  B\PROYECTO 1\Codigo Fuente\TEST_FILE.pxla"
            # fileName=r"C:\Users\Sr. C\Desktop\archivoEntrada.pxla"
            # fileName=r"C:\Users\Sr. C\Google Drive\C U A R T O  S E M E S T R E\L F P  B+\LAB  LFP  B\PROYECTO 1\Archivos de Prueba\proyecto1v2.pxla"
            # fileName=r"C:\Users\Sr. C\Google Drive\C U A R T O  S E M E S T R E\L F P  B+\LAB  LFP  B\PROYECTO 1\prueba.pxla"

            if fileName:
                file=self.leerArchivo(str(fileName))
                # with open(fileName) as f_obj:
                #     lines = f_obj.readlines()
                    
                #     for line in lines:
                #         file.append(line.strip('\n'))
                
        except:
            print("ERROR POR FAVOR SELECCIONE UNO CORRECTO")
    
    def devolverfile(self):
        global file
        # print(file)
        return file

    def leerArchivo(self, ruta):
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        archivo.close()
        print(type(contenido))
        contenido=contenido
        # print(contenido)
        return contenido
        

    # def openFileNamesDialog(self): 
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)
 
    # def saveFileDialog(self):    
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         print(fileName)
 
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = loadfile()
#     sys.exit(app.exec_())
