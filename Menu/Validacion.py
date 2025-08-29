
class Validacion:

    @staticmethod
    def leer_entero(mensaje, minimo=None, maximo=None):
        while True:
            try:
                valor = int(input(mensaje))
                if minimo is not None and valor < minimo:
                    print(f" El número debe ser mayor o igual a {minimo}.")
                    continue
                if maximo is not None and valor > maximo:
                    print(f" El número debe ser menor o igual a {maximo}.")
                    continue
                return valor
            except ValueError:
                print(" Debes ingresar un número válido.")

    @staticmethod
    def leer_flotante(mensaje, minimo=None, maximo=None):
        while True:
            try:
                valor = float(input(mensaje))
                if minimo is not None and valor < minimo:
                    print(f" El número debe ser mayor o igual a {minimo}.")
                    continue
                if maximo is not None and valor > maximo:
                    print(f" El número debe ser menor o igual a {maximo}.")
                    continue
                return valor
            except ValueError:
                print(" Debes ingresar un número decimal válido.")

    @staticmethod
    def leer_texto(mensaje):
        while True:
            valor = input(mensaje).strip()
            if valor == "":
                print("⚠️ No puedes dejar este campo vacío.")
            elif any(char.isdigit() for char in valor):
                print("⚠️ El nombre no debe contener números.")
            else:
                return valor
