class  Ojo(object):
    color="rojo"
    tamaño=""
    forma=""
class  Pelo(object):
    color="Amarillo"
    textura=""
class  Antena(object):
    color=""
    longitud=""
class  Insecto():
        color="azul"
        tamaño=""
        aspecto=""
        antenas=Antena()
        ojos=Ojo()
        pelos=Pelo()
        def imprimir(self, valor, valor2):
            print(valor," ;", valor2)
        
class  Persona(Pelo):
        peso=""
        ojo=Ojo()
    
