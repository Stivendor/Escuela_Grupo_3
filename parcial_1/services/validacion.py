class Validacion:
    @staticmethod
    def validar_nombre(nombre):
        """Valida que el nombre no esté vacío y solo contenga letras y espacios"""
        if not nombre or not nombre.strip():
            return False, "El nombre no puede estar vacío"
        
        if not all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
            return False, "El nombre solo puede contener letras y espacios"
        
        if len(nombre.strip()) < 2:
            return False, "El nombre debe tener al menos 2 caracteres"
            
        return True, ""

    @staticmethod
    def validar_edad(edad_str):
        """Valida que la edad sea un número entre 15 y 100"""
        try:
            edad = int(edad_str)
            if edad < 15:
                return False, "La edad mínima es 15 años"
            if edad > 100:
                return False, "La edad máxima es 100 años"
            return True, edad
        except ValueError:
            return False, "La edad debe ser un número entero"

    @staticmethod
    def validar_matricula(matricula):
        """Valida el formato de la matrícula"""
        if not matricula or not matricula.strip():
            return False, "La matrícula no puede estar vacía"
        
        if len(matricula.strip()) < 5:
            return False, "La matrícula debe tener al menos 5 caracteres"
            
        return True, ""

    @staticmethod
    def validar_materia(materia):
        """Valida que la materia no esté vacía"""
        if not materia or not materia.strip():
            return False, "La materia no puede estar vacía"
        
        if len(materia.strip()) < 2:
            return False, "La materia debe tener al menos 2 caracteres"
            
        return True, ""

    @staticmethod
    def validar_nota(nota_str):
        """Valida que la nota sea un número entre 1 y 5"""
        try:
            nota = float(nota_str)
            if nota < 1:
                return False, "La nota no puede ser menor a 1"
            if nota > 5:
                return False, "La nota no puede ser mayor a 5"
            return True, nota
        except ValueError:
            return False, "La nota debe ser un número"

    @staticmethod
    def validar_opcion_menu(opcion, opciones_validas):
        """Valida que la opción del menú sea válida"""
        if opcion not in opciones_validas:
            return False, f"Opción no válida. Las opciones válidas son: {', '.join(opciones_validas)}"
        return True, ""