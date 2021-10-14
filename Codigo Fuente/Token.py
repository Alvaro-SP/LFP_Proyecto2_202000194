
class Token:
    def __init__(self,  lexema, tipo,  linea, columna):
        self.lexema = lexema
        self.tipo = tipo        
        self.linea = linea 
        self.columna = columna 

    def impToken(self):
        print("LEXEMA:      ",self.lexema,"     TIPO:  ", self.tipo,"       lÍNEA:  ", self.linea," COLUMNA:  ", self.columna)

    def impHTMLToken(self, acum):
        cont=""
        cont+= """ <tr>
                    <td>""" + str(acum) + """</td>
                    <td>""" + str(self.lexema) + """</td>
                    <td>""" + str(self.tipo) + """</td>
                    <td>""" + str(self.linea) + """</td>
                    <td>""" + str(self.columna) + """</td>
                    </tr>"""
        return cont
    
    def savedata(self):
        return self.tipo
