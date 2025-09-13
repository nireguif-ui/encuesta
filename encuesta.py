for i in range(1,10):
    class Encuesta:
        def __init__(self, preguntas, respuestas):
            self.respuestas = respuestas
            self.preguntas = preguntas
        def ideaproyecto(self):
            self.respuesta1 = input("¿Cuál es tu idea de proyecto para POO?")
        def tiempo(self):
            self.respuesta2 = input ("¿Tienes un tiempo flexible o rigido?" )
        def limitaciones(self):
            self.respuesta3 = input ("¿Cuentas con como trabajar en casa?")
        def muestra_encuesta(self):
            print("Idea proyecto", self.respuesta1)
            print("Tiempo", self.respuesta2)
            print("Limitaciones", self.respuesta3)
        
    respuestas="a"
    preguntas="b"
    encuesta = Encuesta(preguntas, respuestas)
    encuesta.ideaproyecto()
    encuesta.tiempo()
    encuesta.limitaciones()