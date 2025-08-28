# Escuela — Examen POO (Python) + Git/GitHub

Sistema de consola para gestionar una **escuela** con **estudiantes, profesores y materias**.  
Permite **registrar notas**, **calcular promedios** y **listar estudiantes**, aplicando **herencia, polimorfismo y encapsulamiento** en Python y un **flujo de colaboración** con Git/GitHub usando ramas protegidas.

---

## 🗂 Tabla de contenido

1. [🎯 Objetivo del proyecto](#-objetivo-del-proyecto)  
2. [⚙️ Requisitos](#️-requisitos)  
3. [📂 Estructura del proyecto](#-estructura-del-proyecto)  
4. [▶️ Ejecución local](#️-ejecución-local)  
5. [🔀 Flujo de trabajo en Git/GitHub](#-flujo-de-trabajo-en-gitgithub)  
6. [👥 Distribución del trabajo (3 integrantes)](#-distribución-del-trabajo-3-integrantes)  
7. [🧩 Diseño de POO](#-diseño-de-poo)  
8. [📋 Menú de consola](#-menú-de-consola)  
9. [✅ Checklist de evaluación](#-checklist-de-evaluación)  

---

## 🎯 Objetivo del proyecto

- Implementar un sistema en consola para **gestionar estudiantes, profesores y materias**.  
- Aplicar correctamente los conceptos de **POO (herencia, polimorfismo, encapsulamiento)**.  
- Utilizar un **flujo de trabajo colaborativo en Git/GitHub** con ramas protegidas y PRs.  

---

## ⚙️ Requisitos

- **Python 3.10+**  
- **Git** y cuenta en **GitHub**  
- (Opcional) **venv** para entorno virtual  

---

## 📂 Estructura del proyecto

```bash
escuela/
├── main.py                  # Punto de entrada: menú de consola
├── models/                  # Modelos de dominio (POO)
│   ├── persona.py           # Clase base: Persona
│   ├── estudiante.py        # Clase Estudiante (hereda de Persona)
│   ├── profesor.py          # Clase Profesor (hereda de Persona)
│   └── materia.py           # Clase Materia
├── services/                # Casos de uso / lógica de aplicación
│   ├── gestion_estudiantes.py # Altas/listados y consultas de estudiantes
│   └── gestion_notas.py       # Registro de notas y cálculo de promedios
└── README.md
```

---

## ▶️ Ejecución local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/Escuela.git
   cd escuela
   ```

2. Ejecutar el programa:
   ```bash
   python main.py
   ```

3. Seguir las instrucciones del menú en consola.

---

## 🔀 Flujo de trabajo en Git/GitHub

### Ramas protegidas
- **`prod`** → Versión estable (producción).  
- **`qa`** → Testing/integración.  
- **`dev`** → Desarrollo principal.  

### Ramas de cada integrante
- **`feat/angel-clases`** → Manejo de clases y herencia.  
- **`feat/stiven-notas`** → Gestión de notas y promedios.  
- **`feat/julian-menu`** → Menú principal en consola.  

---

## 👥 Distribución del trabajo (3 integrantes)

### Integrante 1: Angel David (POO / Clases base)
- Crear clases en `models/`:
  - `Persona` (atributos comunes: nombre, edad).
  - `Estudiante` (hereda de Persona, incluye matrícula y notas).
  - `Profesor` (hereda de Persona, incluye especialidad).
  - `Materia` (nombre, código, relación con estudiantes/profesor).
- Implementar:
  - **Herencia**.
  - **Polimorfismo** (ej. sobrescribir `presentarse()`).
  - **Encapsulamiento**.

### Integrante 2: Stiven (Gestión de notas / Promedios)
- Implementar en `services/gestion_notas.py`:
  - Registrar notas para un estudiante en determinada materia.
  - Calcular promedio de notas de un estudiante.
  - Mostrar reportes de notas.
- Conectar estas funciones al menú (cuando se elija “registrar nota” o “calcular promedio”).

### Integrante 3: Julian (Menú principal / Conexión de servicios)
- Implementar en `main.py`:
  - Menú interactivo en consola con opciones:
    1. Registrar estudiante.
    2. Registrar profesor.
    3. Registrar materia.
    4. Registrar nota a estudiante.
    5. Calcular promedio de un estudiante.
    6. Listar estudiantes.
    7. Salir.
  - Llamar las funciones de `services` según la opción elegida.

---

## 🧩 Diseño de POO

- **Herencia** → `Estudiante` y `Profesor` heredan de `Persona`.  
- **Polimorfismo** → Cada clase sobrescribe métodos como `presentarse()`.  
- **Encapsulamiento** → Uso de atributos privados (`__atributo`) y getters/setters.  

---

## 📋 Menú de consola

Ejemplo esperado:

```text
===== MENÚ ESCUELA =====
1. Registrar estudiante
2. Registrar profesor
3. Registrar materia
4. Registrar nota a estudiante
5. Calcular promedio de un estudiante
6. Listar estudiantes
7. Salir
Seleccione una opción: _
```

---

## ✅ Checklist de evaluación

- [ ] Uso correcto de POO (herencia, polimorfismo, encapsulamiento).  
- [ ] Implementación de menú de consola.  
- [ ] Gestión de estudiantes, profesores y materias.  
- [ ] Registro de notas y promedios.  
- [ ] Flujo en Git/GitHub con ramas protegidas y PRs.  
- [ ] README completo y bien documentado.  