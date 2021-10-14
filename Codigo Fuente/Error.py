
class Error:
    def __init__(self, descripcion, tipo, linea, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def impError(self):
        print(" DESCRIPCIÓN: ",self.descripcion, " TIPO: ",self.tipo, " LINEA: ",self.linea, " COLUMNA: ",self.columna)

    def impHTMLError(self, acum):
        cont=""
        cont+= """ <tr>
                    <td>""" + str(acum) + """</td>
                    <td>""" + str(self.descripcion) + """</td>
                    <td>""" + str(self.tipo) + """</td>
                    <td>""" + str(self.linea) + """</td>
                    <td>""" + str(self.columna) + """</td>
                    </tr>"""
        return cont