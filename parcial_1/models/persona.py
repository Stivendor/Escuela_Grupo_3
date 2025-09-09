class Persona:
    #Constructor de la clase
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    #Getters y setters (encapsulamiento)
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

    def presentarse(self):
        return f"Soy {self.__nombre}, y tengo {self.__edad}."