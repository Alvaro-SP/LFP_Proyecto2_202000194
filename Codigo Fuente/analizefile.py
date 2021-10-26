from loadfile import *
import re
from Token import *
from Error import *
from loadfile import *
import mensaje
import os
listaErrores=[]
contarchivos=0
nametable=""
class analizefile():
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.listTokens = []
        self.listClaves=[]
        self.listRegistros=[]
        self.tabla=[]
        self.textoconsola=""
        self.canproces=None
        self.Arbol=""
        self.Arbol_claves=""
        self.cont=0
        self.contreg2=0
        self.contreg=0
        self.contvalreg=0
        self.impr=0
        self.clavetxt=0
        self.imprln=0
        self.conteotxt=0
        self.promtxt=0
        self.contarsitxt=0
        self.datostxt=0
        self.sumartxt=0
        self.maxtxt=0
        self.mintxt=0
        self.exportxt=0
        self.contarchivos=1
        self.listinsttxt=0
        self.listinsttxt2=0
        self.instxt=0

    def analizar(self, file):
        global contarchivos
        global listaErrores
        self.listaTokens = []
        self.listTokens = []
        self.listaErrores = listaErrores
        self.listClaves=[]
        self.listRegistros=[]
        self.tabla=[]
        self.textoconsola=""
        self.canproces=None
        self.Arbol=""
        self.Arbol_claves=""
        self.cont=0
        self.contreg2=0
        self.contreg=0
        self.impr=0
        self.regtxt=0
        self.contvalreg=0
        self.imprln=0
        self.conteotxt=0
        self.promtxt=0
        self.contarsitxt=0
        self.datostxt=0
        self.sumartxt=0
        self.maxtxt=0
        self.mintxt=0
        self.exportxt=0
        self.listinsttxt=0
        self.listinsttxt2=0
        self.instxt=0
        file=file.lower()
        #*inicializar atributos
        linea = 1
        columna = 1
        buffer = ''
        centinela = '$'
        estado = 0
        file += centinela
        #*Automata
        i=0
        while i < len(file):
            c=file[i]
            if   estado == 0:
                if c == '=':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'igual', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '{':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llavea', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '}':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llavec', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corchetea', linea, columna))
                    self.listTokens.append([buffer, 'corchetea', linea, columna])
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corchetec', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '(':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'parena', linea, columna))
                    self.listTokens.append([buffer, 'parena', linea, columna])
                    buffer = ''
                    columna += 1
                elif c == ')':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'parenc', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '#':
                    buffer += c
                    columna +=1
                    estado=5
                elif c == '.':
                    buffer += c
                    columna +=1
                    estado=11
                elif c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 1
                elif re.search(r'\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                elif re.search(r'[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                elif c == '\n':
                    pass
                    linea += 1
                    columna = 1
                elif c == re.search(r'[\t]', c):
                    columna += 1
                elif c == '\r':
                    pass
                elif re.search(r'[\r]', c):
                    pass
                elif re.search(r'\s', c):
                    columna += 1
                elif c == centinela:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    # if buffer != ' ':
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 1:
                if c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 6
                elif c == r'[\n]':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == [r'\r']:
                    buffer += c
                else:
                    buffer += c
                    columna += 1
                    estado=10
            elif estado == 2:
                if re.search(r'[\d]', c):
                    buffer += c
                    columna += 1
                elif c == '.':
                    buffer += c
                    columna +=1
                    estado=11
                else:
                    self.listaTokens.append(Token(buffer, 'entero', linea, columna))
                    self.listTokens.append([buffer, 'entero', linea, columna])
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado ==11:
                if re.search(r'[\d]', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'decimal', linea, columna))
                    self.listTokens.append([buffer, 'decimal', linea, columna])
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 3:
                if re.search('[a-z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'claves':
                        self.listaTokens.append(Token(buffer, 'claves', linea, columna))
                        self.listTokens.append([buffer, 'claves', linea, columna])
                    elif buffer == 'registros':
                        self.listaTokens.append(Token(buffer, 'registros', linea, columna))
                        self.listTokens.append([buffer, 'registros', linea, columna])
                    elif buffer == 'imprimir':
                        self.listaTokens.append(Token(buffer, 'imprimir', linea, columna))
                        self.listTokens.append([buffer, 'imprimir', linea, columna])
                    elif buffer == 'imprimirln':
                        self.listaTokens.append(Token(buffer, 'imprimirln', linea, columna))
                        self.listTokens.append([buffer, 'imprimirln', linea, columna])
                    elif buffer == 'conteo':
                        self.listaTokens.append(Token(buffer, 'conteo', linea, columna))
                        self.listTokens.append([buffer, 'conteo', linea, columna])
                    elif buffer == 'promedio':
                        self.listaTokens.append(Token(buffer, 'promedio', linea, columna))
                        self.listTokens.append([buffer, 'promedio', linea, columna])
                    elif buffer == 'contarsi':
                        self.listaTokens.append(Token(buffer, 'contarsi', linea, columna))
                        self.listTokens.append([buffer, 'contarsi', linea, columna])
                    elif buffer == 'datos':
                        self.listaTokens.append(Token(buffer, 'datos', linea, columna))
                        self.listTokens.append([buffer, 'datos', linea, columna])
                    elif buffer == 'sumar':
                        self.listaTokens.append(Token(buffer, 'sumar', linea, columna))
                        self.listTokens.append([buffer, 'sumar', linea, columna])
                    elif buffer == 'max':
                        self.listaTokens.append(Token(buffer, 'max', linea, columna))
                        self.listTokens.append([buffer, 'max', linea, columna])
                    elif buffer == 'min':
                        self.listaTokens.append(Token(buffer, 'min', linea, columna))
                        self.listTokens.append([buffer, 'min', linea, columna])
                    elif buffer == 'exportarreporte':
                        self.listaTokens.append(Token(buffer, 'exportarreporte', linea, columna))
                        self.listTokens.append([buffer, 'exportarreporte', linea, columna])
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 5:
                if c!='\n'  :
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'comentariosimple', linea, columna))
                    # self.listTokens.append([buffer, 'colorHexadecimal', linea, columna])                    
                    buffer = ''
                    i -=1
                    estado = 0
            elif estado == 6:
                if c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 7
                elif c == r'[\n]':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == [r'\r']:
                    buffer += c
                else:
                    buffer += c
                    columna += 1
                    estado=0
            elif estado == 7:
                if c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 8
                elif c == r'[\n]':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == [r'\r']:
                    buffer += c
                else:
                    buffer += c
                    columna += 1
            elif estado == 8:
                if c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 9
                else:
                    buffer += c
                    columna += 1
                    estado=0
            elif estado == 9:
                if c == '\'' or c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'comentariomultilinea', linea, columna))
                    # self.listTokens.append([buffer, 'cadena', linea, columna])
                    buffer = ''
                    columna += 1
                    estado = 0
                else:
                    buffer += c
                    columna += 1
                    estado=0
            elif estado == 10:
                if c == '\'' or c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'cadena', linea, columna))
                    # self.listTokens.append([buffer, 'cadena', linea, columna])
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == r'[\n]':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == [r'\r']:
                    buffer += c
                else:
                    buffer += c
                    columna += 1
            i += 1
        indicetoken=0
        a=mensaje.App()
        a.initUI("SE HA REALIZADO EL ANALISIS LEXICO ")
        self.textoconsola+="*****  Fin del Análisis Léxico  *****\n"
        self.Arbol=""" 
            digraph G {
            layout=dot   
            fontcolor="black" 
            label="ARBOL DE DERIVACIÓN"    
            labelloc = "t"
            bgcolor="orange:red"    
            edge [weight=1000 style=radial color=black ]
            node [shape=ellipse style="filled"  color="green:lightblue" gradientangle="315"]
            ___INICIO___[shape=ellipse color=green fontcolor=black]  \n"""
        self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES__\" ]"
        self.listinsttxt=self.cont
        self.cont+=1
        self.Arbol_claves+=f"\n___INICIO___ -> {self.listinsttxt} "
        self.Sintactic_analize(indicetoken)
        if self.canproces != False :
            self.textoconsola+="*****  Fin del Análisis Sintáctico  *****\n"
            self.Procesar(0)

            self.Arbol+="\n }"
            try:                
                file=open('Graficos_generados/Grafico_Arbol_Derivacion'+str(self.contarchivos)+'.dot','w')
                file.write(self.Arbol)
                file.close()
                os.system('dot -Tpng Graficos_generados/Grafico_Arbol_Derivacion'+str(self.contarchivos)+'.dot -o Graficos_generados/graficoimagen_Arbol_Derivacion'+str(self.contarchivos)+'.png')
                os.startfile(r"Graficos_generados\graficoimagen_Arbol_Derivacion"+str(self.contarchivos)+".png")
                print("\033[1;32m"+"\nSe ha generado el gráfico Arbol_Derivacion con éxito... \n"+'\033[0;m')
                contarchivos=self.contarchivos
                self.contarchivos+=1
            except Exception:
                print("\033[1;31m"+"\nUps... algo salió mal :( podria haber un error, intentelo nevamente\n"+'\033[0;m')     
                return False
            print("ANALISIS SINTÁCTICO REALIZADO CON ÉXITO")
        else:
            print("Algo salio mal pudo deberse al analisis SINTÁCTICO")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        # print("CANPROCESS  ", canproces)
        a=mensaje.App()
        a.initUI("SE HA REALIZADO EL ANALISIS SINTÁCTICO ")
        listaErrores=self.listaErrores
        return self.textoconsola

    #!  'claves'
    def clave4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='coma':
            
            return self.clave3(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='corchetec':
            
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba una , o ] y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una COMA o un CORCHETE ] y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def clave3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            return self.clave4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            self.listaErrores.append(Error(f'Se esperaba una CADENA  y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            return False, indicetoken
    def clave2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='corchetea':return self.clave3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba un Corchetea [ y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un CORCHETE [ y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def clave1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='igual':
            return self.clave2(indicetoken+1)
            
        else:
            print(f"Error sintáctico: Se esperaba un un signo IGUAL = y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba un signo IGUAL = y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un signo IGUAL = y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'registros'
    def registro6(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='corchetec':
            return True, indicetoken
        elif self.listaTokens[indicetoken].tipo=='llavea':
            return self.registro4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba un Corchetec o llavea y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un CORCHETE ] o una LLAVE QUE ABRE y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def registro5(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='coma':
            return self.registro4(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='llavec':
            return self.registro6(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba una coma y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una COMA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def registro4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena' or self.listaTokens[indicetoken].tipo=='decimal' or self.listaTokens[indicetoken].tipo=='entero':
            
            return self.registro5(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba una cadena, entero o decimal y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA, DECIMAL O ENTERO y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def registro3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='llavea':
            return self.registro4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba un llavea y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una LLAVE QUE ABRE y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def registro2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='corchetea':
            return self.registro3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba corchetea y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba  un CORCHETE [ y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def registro1(self, indicetoken):
        
        if self.listaTokens[indicetoken].tipo=='igual':
            return self.registro2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un signo IGUAL = y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba signoigual y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un signo IGUAL = y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'imprimir' y 'imprimirln' y 'promedio' y 'sumar' y 'max' y 'min' y 'exportarreporte'
    def imprimir4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba puntoycoma y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def imprimir3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            return self.imprimir4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba parentesisc y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def imprimir2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            return self.imprimir3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba cadena y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def imprimir1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            return self.imprimir2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba parentesisa y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'conteo'  y   'datos'
    def conteo3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba puntoycoma y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba  un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def conteo2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            return self.conteo3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba parentesisc y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def conteo1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            return self.conteo2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba parentesisa y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'contarsi'
    def contarsi6(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un PUNTO Y COMA y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba puntoycoma y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba PUNTO Y COMA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def contarsi5(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            return self.contarsi6(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba parentesisc y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def contarsi4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='entero' or self.listaTokens[indicetoken].tipo=='decimal':
            return self.contarsi5(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un ENTERO o decimal y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba entero y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un entero y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def contarsi3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='coma':
            return self.contarsi4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba una COMA y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba coma y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una COMA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def contarsi2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            return self.contarsi3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba una cadena y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba cadena y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def contarsi1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            return self.contarsi2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.listaErrores.append(Error(f'Se esperaba parentesisa y se recibió: ({self.listaTokens[indicetoken].tipo})', 'Sintáctico', self.listaTokens[indicetoken].linea, self.listaTokens[indicetoken].columna))
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  ANALISIS SINTACTICO DEL LENGUAJE
    def Sintactic_analizer(self, indicetoken):

        if self.listaTokens[indicetoken].tipo=='claves':
            return self.clave1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='registros':            
            return self.registro1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='imprimir':            
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='imprimirln':
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='conteo':
            return self.conteo1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='promedio':
            # self.Arbol_promedio+="\n___INICIO___ -> __PROMEDIO__ "
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='contarsi':
            # self.Arbol_claves+="\n___INICIO___ -> __CONTARSI__ "
            return self.contarsi1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='datos':
            # self.Arbol_claves+="\n___INICIO___ -> __DATOS__ "
            return self.conteo1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='sumar':
            # self.Arbol_claves+="\n___INICIO___ -> __SUMAR__ "
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='max':
            # self.Arbol_claves+="\n___INICIO___ -> __MAX__ "
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='min':
            # self.Arbol_claves+="\n___INICIO___ -> __MIN__ "
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='exportarreporte':
            # self.Arbol_claves+="\n___INICIO___ -> __EXPORTARREPORTE__ "
            return self.imprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='comentariosimple' or self.listaTokens[indicetoken].tipo=='comentariomultilinea':
            # self.Arbol_claves+="\n___INICIO___ -> __COMENTARIOSIMPLE__ "
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def fracaso(self):
        self.canproces=False
    def Sintactic_analize(self, indicetoken):
        analisis, indicetoken = self.Sintactic_analizer(indicetoken)
        
        if analisis :
            if indicetoken+1<len(self.listaTokens):
                self.Sintactic_analize(indicetoken+1)
        else:
            print('El analisis fracasó: ', analisis)
            self.fracaso()
        # if indicetoken+1==len(self.listaTokens):
        #     return True


    #!EJECUTANDO EL ARCHIVO▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    #!  'claves'
    def Sclave4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='coma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\",\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n__LISTACLAVES__ -> {temp} "
            return self.Sclave3(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='corchetec':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"]\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.clavetxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            # self.tabla.append(self.listClaves)
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una COMA o un CORCHETE ] y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sclave3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            self.Arbol_claves+=f"\n__LISTACLAVES__ -> {  tempstring  } "            
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace('\'','')
            self.listClaves.append(tempstring)
            return self.Sclave4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sclave2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='corchetea':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"[\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.clavetxt} -> {temp} "
            self.Arbol_claves+=f"\n{self.clavetxt} -> __LISTACLAVES__ "
            
            return self.Sclave3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un CORCHETE [ y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sclave1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='igual':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"=\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.clavetxt} -> {temp} "
            return self.Sclave2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un signo IGUAL = y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un signo IGUAL = y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'registros'
    def Sregistro6(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='corchetec':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"]\" ]"
            corchetecont=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.regtxt} -> {corchetecont}"
            self.Arbol+=self.Arbol_claves
            return True, indicetoken
        elif self.listaTokens[indicetoken].tipo=='llavea':
            cortemp="{"
            self.Arbol_claves+=f"\n{self.cont} [ label=\" {cortemp} \" ]"
            llaveacont=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTAREGISTROS2__\" ]"
            self.contreg2=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTAVALREG__\" ]"
            self.contvalreg=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n__LISTAREGISTROS__ -> {self.contreg2} "
            self.Arbol_claves+=f"\n{self.contreg2} -> {llaveacont} "
            self.Arbol_claves+=f"\n{self.contreg2} -> {self.contvalreg} "

            return self.Sregistro4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un CORCHETE ] o una LLAVE QUE ABRE y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sregistro5(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='coma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\",\" ] "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contvalreg} -> \"{temp}\" "
            return self.Sregistro4(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='llavec':
            cortemp="}"
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{cortemp}\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contreg2} -> \"{temp}\" "
            self.tabla.append(self.listRegistros)
            self.listRegistros=[]
            return self.Sregistro6(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una COMA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sregistro4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena' or self.listaTokens[indicetoken].tipo=='decimal' or self.listaTokens[indicetoken].tipo=='entero':
            
            if self.listaTokens[indicetoken].tipo=='cadena':
                tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
                tempstring=tempstring.replace("\\",'')
                tempstring=tempstring.replace("/",'')
                tempstring=tempstring.replace('\'','')
                self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
                temp1=self.cont
                self.cont+=1
                self.Arbol_claves+=f"\n{self.contvalreg} -> {temp1}"
                
                self.listRegistros.append(tempstring)
            else:
                self.Arbol_claves+=f"\n{self.cont} [ label=\"{self.listaTokens[indicetoken].lexema}\" ]"
                temp=self.cont
                self.cont+=1
                self.Arbol_claves+=f"\n{self.contvalreg} -> {temp}"
                self.listRegistros.append(self.listaTokens[indicetoken].lexema)
            return self.Sregistro5(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA, DECIMAL O ENTERO y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sregistro3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='llavea':
            cortemp="{"
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{cortemp}\" ]"
            llaveacont=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTAREGISTROS2__\" ]"
            self.contreg2=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTAVALREG__\" ]"
            self.contvalreg=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n__LISTAREGISTROS__ -> {self.contreg2} "
            self.Arbol_claves+=f"\n{self.contreg2} -> {llaveacont} "
            self.Arbol_claves+=f"\n{self.contreg2} -> {self.contvalreg} "
            return self.Sregistro4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una LLAVE QUE ABRE y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sregistro2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='corchetea':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"[\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.regtxt}  -> {temp} "
            self.Arbol_claves+=f"\n{self.regtxt}  -> \"__LISTAREGISTROS__ \" "
            return self.Sregistro3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba  un CORCHETE [ y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sregistro1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='igual':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"=\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.regtxt}  -> {temp} "
            return self.Sregistro2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un signo IGUAL = y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un signo IGUAL = y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'imprimir' y 'imprimirln' y 'promedio' y 'sumar' y 'max' y 'min' y 'exportarreporte'
    def Simprimir4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.impr} -> {temp} "
            self.Arbol+=self.Arbol_claves
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Simprimir3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.impr} -> {temp} "
            return self.Simprimir4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Simprimir2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.impr} -> {temp} "
            
            self.textoconsola+=f"{tempstring}\n"
            return self.Simprimir3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Simprimir1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.impr} -> {temp} "
            return self.Simprimir2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'imprimirln'
    def Simprimirln4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.imprln} -> {temp} "
            self.Arbol+=self.Arbol_claves
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Simprimirln3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.imprln} -> {temp} "
            
            return self.Simprimirln4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Simprimirln2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.imprln} -> {temp} "
            
            
            self.textoconsola+=f"{tempstring}"
            return self.Simprimirln3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Simprimirln1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.imprln} -> {temp} "
            return self.Simprimirln2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!   'promedio'
    def Spromedio4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.promtxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Spromedio3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.promtxt} -> {temp} "
            return self.Spromedio4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Spromedio2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.promtxt} -> {temp} "
            
            
            try:
                i=self.listClaves.index(tempstring)
                prom=0
                try:
                    for w in range(len(self.tabla)):
                        prom+=float(self.tabla[w][i])
                    self.textoconsola+=f"El promedio es: {(prom/len(self.tabla)):.3f}\n"
                except:
                    self.textoconsola+=f"Los valores no son enteros, no se puede promediar.\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
            return self.Spromedio3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Spromedio1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.promtxt} -> {temp} "
            
            return self.Spromedio2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!'conteo'  
    def Sconteo3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.conteotxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba  un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sconteo2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.conteotxt} -> {temp} "
            return self.Sconteo3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sconteo1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.conteotxt} -> {temp} "
            try:
                self.textoconsola+=f"\n{len(self.tabla)}\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
            return self.Sconteo2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!'datos'
    def Sdatos3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.datostxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba  un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sdatos2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.datostxt} -> {temp} "
            return self.Sdatos3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sdatos1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.datostxt} -> {temp} "
            try:
                self.textoconsola+=f"\n"
                for w in (self.listClaves):
                    self.textoconsola+=f"{w:15}"
                self.textoconsola+=f"\n"
                for x in range(len(self.tabla)):
                    self.textoconsola+=f"  "
                    for y in range(len(self.listClaves)):
                        self.textoconsola+=f"{self.tabla[x][y]:15}"
                    self.textoconsola+=f"\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
            return self.Sdatos2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'contarsi'
    def Scontarsi6(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contarsitxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un PUNTO Y COMA y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba PUNTO Y COMA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Scontarsi5(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contarsitxt} -> {temp} "
            
            return self.Scontarsi6(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Scontarsi4(self, indicetoken, clavecont):
        if self.listaTokens[indicetoken].tipo=='cadena' or self.listaTokens[indicetoken].tipo=='entero'  or self.listaTokens[indicetoken].tipo=='decimal':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{self.listaTokens[indicetoken].lexema}\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contarsitxt} -> {temp} "

            tempstring=clavecont.replace('"','')
            tempstring=tempstring.replace('\'','')
            try:
                i=self.listClaves.index(tempstring)
                cont=0
                for w in range(len(self.tabla)):
                    if self.tabla[w][i]==self.listaTokens[indicetoken].lexema:
                        cont+=1
                self.textoconsola+=f"\nCantidad de elementos encontrados en ({self.listaTokens[indicetoken].lexema}):{cont}\n"
            except:
                self.textoconsola+=f"(Contarsi) No existe una tabla previa o el valor no esta bien especificado.\n"
            return self.Scontarsi5(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un ENTERO y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba ({self.listaTokens[indicetoken].tipo}) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Scontarsi3(self, indicetoken, clavecont):
        if self.listaTokens[indicetoken].tipo=='coma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\",\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contarsitxt} -> {temp} "

            return self.Scontarsi4(indicetoken+1, clavecont)
        else:
            print(f"Error sintáctico: Se esperaba una COMA y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una COMA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Scontarsi2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena' or self.listaTokens[indicetoken].tipo=='decimal' or self.listaTokens[indicetoken].tipo=='entero':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            self.Arbol_claves+=f"\n{self.cont} [ label={ tempstring } ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contarsitxt} -> {temp} "
            
            return self.Scontarsi3(indicetoken+1, tempstring)
        else:
            print(f"Error sintáctico: Se esperaba una cadena y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Scontarsi1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.contarsitxt} -> {temp} "
            
            return self.Scontarsi2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    
    #!  'sumar'
    def Sumar4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.sumartxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sumar3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.sumartxt} -> {temp} "
            
            return self.Sumar4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sumar2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.sumartxt} -> {temp} "
            
            
            try:
                i=self.listClaves.index(tempstring)
                prom=0
                try:
                    for w in range(len(self.tabla)):
                        prom+=float(self.tabla[w][i])
                    self.textoconsola+=f"\nLa suma es: {prom}\n"
                except:
                    self.textoconsola+=f"Los valores no son enteros, no se puede calcular.\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
                
            return self.Sumar3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Sumar1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.sumartxt} -> {temp} "
            
            return self.Sumar2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'max'
    def max4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.maxtxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def max3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.maxtxt} -> {temp} "
            
            return self.max4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def max2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.maxtxt} -> {temp} "
            
            
            try:
                i=self.listClaves.index(tempstring)
                listtemp=[]
                try:
                    for w in range(len(self.tabla)):
                        listtemp.append(float(self.tabla[w][i]))
                    prom=max(listtemp)
                    self.textoconsola+=f"\nEl valor máximo es: {prom}\n"
                except:
                    self.textoconsola+=f"Los valores no son enteros, no se puede calcular.\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
            return self.max3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def max1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.maxtxt} -> {temp} "
            
            return self.max2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!  'min'
    def min4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.mintxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def min3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.mintxt} -> {temp} "
            
            return self.min4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def min2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.mintxt} -> {temp} "
            
            
            try:
                i=self.listClaves.index(tempstring)
                listtemp=[]
                try:
                    for w in range(len(self.tabla)):
                        listtemp.append(float(self.tabla[w][i]))
                    prom=min(listtemp)
                    self.textoconsola+=f"\nEl valor mínimo es: {prom}\n"
                except:
                    self.textoconsola+=f"Los valores no son enteros, no se puede calcular.\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
            
            return self.min3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def min1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.mintxt} -> {temp} "
            
            return self.min2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #!   'exportarreporte'
    def crearHTML(self,name):
        global nametable
        contenido = ''
        namel=name.replace(" ","")
        namel=namel.replace("\"","")
        namel=namel.replace("\'","")
        
        htmFile = open("TablaGenerada/Tabla_Exportada_" +str(namel)+ ".html", "w", encoding='utf-8')
        htmFile.write("""<!DOCTYPE html><html lang="en" ><head><meta charset="UTF-8"><title>&lt;Tabla&gt; Reporte</title><link rel="stylesheet" href="./style.css"></head><body><!-- partial:index.partial.html --><h1><span class="blue">&lt;</span>Reporte Tabla<span class="blue">&gt;</span> <span class="yellow"> de Registros</pan></h1><h2>  <a href="https://github.com/Alvaro-SP" target="_blank">"""+name+"""</a></h2>
        <table class="container">
        <thead>
        <tr>""")
        for z in self.listClaves:
            htmFile.write(f"<th>{z}</th>")        
        htmFile.write("""</tr>
        </thead>
        <tbody>""")
        for x in range(len(self.tabla)):
            htmFile.write("<tr>")
            for y in range(len(self.listClaves)):
                htmFile.write(f"<td>{self.tabla[x][y]}</td>")
            htmFile.write("</tr>")
        htmFile.write(contenido)
        htmFile.write("""\n</tbody>\n</table>\n<!-- partial -->\n<script  src="./script.js"></script>\n</body>\n</html>""")
        htmFile.close
        try:
            os.startfile(r"TablaGenerada\Tabla_Exportada_" +str(namel)+ r".html")
            nametable=namel
            print("\033[1;32m"+"\nSe ha ABIERTO el HTML con éxito... \n"+'\033[0;m')
            
        except Exception:
            print("\033[1;31m"+"\nUps... No se puede abrir el archivo, talvez no lo ha generado :( \n"+'\033[0;m')     
            return False
    def exportarReporte4(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='puntocoma':
            self.Arbol_claves+=f"\n{self.cont} [ label=\";\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.exportxt} -> {temp} "
            self.Arbol+=self.Arbol_claves
            
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se esperaba un  un PUNTO Y COMA ; y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PUNTO Y COMA ; y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def exportarReporte3(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parenc':
            self.Arbol_claves+=f"\n{self.cont} [ label=\")\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.exportxt} -> {temp} "
            
            return self.exportarReporte4(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un un PARENTESIS ) y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ) y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def exportarReporte2(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='cadena':
            tempstring=(self.listaTokens[indicetoken].lexema).replace('"','')
            tempstring=tempstring.replace("\\",'')
            tempstring=tempstring.replace("/",'')
            tempstring=tempstring.replace('\'','')
            self.Arbol_claves+=f"\n{self.cont} [ label=\"{  tempstring  }\" ]  "
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.exportxt} -> {temp} "
            
            
            try:
                self.crearHTML(tempstring)
                self.textoconsola+=f"\nReporte Exportado Exitosamente\n"
            except:
                self.textoconsola+=f"No existe una tabla previa.\n"
            return self.exportarReporte3(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un {self.listaTokens[indicetoken].tipo} y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba una CADENA y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def exportarReporte1(self, indicetoken):
        if self.listaTokens[indicetoken].tipo=='parena':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"(\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.exportxt} -> {temp} "
            
            return self.exportarReporte2(indicetoken+1)
        else:
            print(f"Error sintáctico: Se esperaba un Paréntesis (  y se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se esperaba un PARENTESIS ( y se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken

    #! PROCESAMIENTO USANDO RECURSIVIDAD
    def CargarListas(self, indicetoken):
        self.Arbol_claves=""
        if self.listaTokens[indicetoken].tipo=='claves':
            
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__CLAVES__\" ]"
            self.clavetxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.clavetxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp

            return self.Sclave1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='registros':
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__REGISTROS__\" ]"
            self.regtxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.regtxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp

            return self.Sregistro1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='imprimir':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__IMPRIMIR__\" ]"
            # self.impr=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.impr} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__IMPRIMIR__\" ]"
            self.impr=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.impr} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.Simprimir1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='imprimirln':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__IMPRIMIRLN__\" ]"
            # self.imprln=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.imprln} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__IMPRIMIRLN__\" ]"
            self.imprln=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.imprln} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp

            return self.Simprimirln1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='conteo':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__CONTEO__\" ]"
            # self.conteotxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.conteotxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__CONTEO__\" ]"
            self.conteotxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.conteotxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.Sconteo1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='promedio':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__PROMEDIO__\" ]"
            # self.promtxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.promtxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__PROMEDIO__\" ]"
            self.promtxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.promtxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.Spromedio1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='contarsi':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__CONTARSI__\" ]"
            # self.contarsitxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.contarsitxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__CONTARSI__\" ]"
            self.contarsitxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.contarsitxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.Scontarsi1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='datos':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__DATOS__\" ]"
            # self.datostxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.datostxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__DATOS__\" ]"
            self.datostxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.datostxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.Sdatos1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='sumar':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__SUMAR__\" ]"
            # self.sumartxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.sumartxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__SUMAR__\" ]"
            self.sumartxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.sumartxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.Sumar1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='max':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__MAX__\" ]"
            # self.maxtxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.maxtxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__MAX__\" ]"
            self.maxtxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.maxtxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.max1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='min':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__MIN__\" ]"
            # self.mintxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.mintxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__MIN__\" ]"
            self.mintxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.mintxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp
            return self.min1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='exportarreporte':
            # self.Arbol_claves+=f"\n{self.cont} [ label=\"__EXPORTARREPORTE__\" ]"
            # self.exportxt=self.cont
            # self.cont+=1
            # self.Arbol_claves+=f"\n___INICIO___ -> {self.exportxt} "
            self.Arbol_claves+=f"\n{self.cont} [ label=\"__EXPORTARREPORTE__\" ]"
            self.exportxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__INSTRUCCION__\" ]"
            self.instxt=self.cont
            self.cont+=1

            self.Arbol_claves+=f"\n{self.listinsttxt} -> {self.instxt} "

            self.Arbol_claves+=f"\n{self.instxt} -> {self.exportxt} "

            self.Arbol_claves+=f"\n{self.cont} [ label=\"__LISTA_INSTRUCCIONES2__\" ]"
            temp=self.cont
            self.cont+=1
            self.Arbol_claves+=f"\n{self.listinsttxt} -> {temp} "
            self.listinsttxt=temp

            return self.exportarReporte1(indicetoken+1)
        elif self.listaTokens[indicetoken].tipo=='comentariosimple' or self.listaTokens[indicetoken].tipo=='comentariomultilinea':
            # self.Arbol_claves+="\n___INICIO___ -> __COMENTARIOS__ "
            return True, indicetoken
        else:
            print(f"Error sintáctico: Se recibió: {self.listaTokens[indicetoken].tipo} en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}")
            self.textoconsola+=f"\nTraceback (most recent call last):\nError sintáctico: Se recibió: ({self.listaTokens[indicetoken].tipo}) en la Línea: {self.listaTokens[indicetoken].linea} y Columna: {self.listaTokens[indicetoken].columna}"
            return False, indicetoken
    def Procesar(self, indicetoken):
        analisis, indicetoken = self.CargarListas(indicetoken)
        
        if analisis :
            if indicetoken+1<len(self.listaTokens):
                self.Procesar(indicetoken+1)
        else:
            print('El analisis fracasó: ', analisis)
        # if indicetoken+1==len(self.listaTokens):
        #     return True
    def impTokens(self):
        for t in self.listaTokens:
            t.impToken()
    def impErrores(self):
        if len(self.listaErrores) == 0:
            print('No hubo errores')
        else:
            for e in self.listaErrores:
                e.impError()
    def generarHTMLTokens(self):
        contenido = ''
        acum=1
        htmFile = open("Reporte_Tokens/Reporte_TOKENS" + ".html", "w", encoding='utf-8')
        htmFile.write("""<!DOCTYPE html><html lang="en" ><head><meta charset="UTF-8"><title>CodePen - &lt;Table&gt; Responsive</title><link rel="stylesheet" href="./style.css"></head><body><!-- partial:index.partial.html --><h1><span class="blue">&lt;</span>Reporte<span class="blue">&gt;</span> <span class="yellow"> de Tokens</pan></h1><h2>  <a href="https://github.com/Alvaro-SP" target="_blank">Lista de Tokens</a></h2><table class="container"><thead><tr><th>No.</th><th>Lexema</th><th>Tipo</th><th>Fila</th><th>Columna</th></tr></thead><tbody>""")
        for t in self.listaTokens:
            contenido+=t.impHTMLToken(acum)
            acum+=1
        htmFile.write(contenido)
        htmFile.write("""\n</tbody>\n</table>\n<!-- partial -->\n<script  src="./script.js"></script>\n</body>\n</html>""")
        htmFile.close
    def generarHTMLErrores(self):
        contenido = ''
        acum=1
        htmFile = open("Reporte_Errores/Reporte_ERRORES" + ".html", "w", encoding='utf-8')
        htmFile.write("""
        <!DOCTYPE html>
        <html lang="en" >
        <head>
        <meta charset="UTF-8">
        <title>CodePen - &lt;Table&gt; Responsive</title>
        <link rel="stylesheet" href="./style.css">
        </head>
        <body>
        <!-- partial:index.partial.html -->
        <h1><span class="blue">&lt;</span>Reporte<span class="blue">&gt;</span> <span class="yellow"> de Errores</pan></h1>
        <h2>  <a href="https://github.com/Alvaro-SP" target="_blank">Lista de Errores</a></h2>
        <table class="container">
        <thead>
        <tr>
        <th>No.</th>
        <th>Descripción</th>
        <th>Tipo</th>
        <th>Fila</th>
        <th>Columna</th>
        </tr>
        </thead>
        <tbody>
        """)
        for t in self.listaErrores:
            contenido+=t.impHTMLError(acum)
            acum+=1
        htmFile.write(contenido)
        htmFile.write("""
        </tbody>\n</table>\n<!-- partial -->\n<script  src="./script.js"></script>\n</body>\n</html>""")
        htmFile.close


            
            
