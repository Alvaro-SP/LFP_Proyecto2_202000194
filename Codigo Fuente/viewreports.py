import os
class viewreports():

    def openTokensHTML(self):
        try:
            os.startfile(r"Reporte_Tokens\Reporte_TOKENS.html")
            print("\033[1;32m"+"\nSe ha ABIERTO el HTML con éxito... \n"+'\033[0;m')
            
        except Exception:
            print("\033[1;31m"+"\nUps... No se puede abrir el archivo, talvez no lo ha generado :( \n"+'\033[0;m')     
            return False

    def openErroresHTML(self): 
        try:
            os.startfile(r"Reporte_Errores\Reporte_ERRORES.html")
            print("\033[1;32m"+"\nSe ha ABIERTO el HTML con éxito... \n"+'\033[0;m')
            
        except Exception:
            print("\033[1;31m"+"\nUps... No se puede abrir el archivo, talvez no lo ha generado :( \n"+'\033[0;m')     
            return False