from django.http import HttpResponse
import datetime

def saludo(request):
    texto = """
        <html>
            <body>
                <h1>Hola Mundo</h1>
            </body>
        </html>
        """
    return HttpResponse(texto)

def fecha(request):
    miFecha = datetime.datetime.now()
    texto2 = """
        <html>
            <body>
                <h2>Fecha y hora</h2>%s
            </body>
        </html>
        """%miFecha
    return HttpResponse(texto2)

def calcEdad(request, edadActual, year):    
    periodo = year - 2024
    edadFutura = edadActual + periodo
    documento ="<html><body><h2>En el año %s tendrás %s años</h2></body></html>"%(year, edadFutura)
    return HttpResponse(documento)