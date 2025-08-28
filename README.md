# Escuela — Examen POO (Python) + Git/GitHub

Sistema de consola para gestionar una **escuela** con **estudiantes, profesores y materias**.  
Permite **registrar notas**, **calcular promedios** y **listar estudiantes**, aplicando **herencia, polimorfismo y encapsulamiento** en Python y un **flujo de colaboración** con Git/GitHub usando ramas protegidas.

---

## 🗂 Tabla de contenido

1. [Objetivo del proyecto](#-objetivo-del-proyecto)  
2. [Requisitos](#-requisitos)  
3. [Estructura del proyecto](#-estructura-del-proyecto)  
4. [Paso a paso: ejecución local](#-paso-a-paso-ejecución-local)  
5. [Paso a paso: flujo de trabajo en Git/GitHub](#-paso-a-paso-flujo-de-trabajo-en-gitgithub)  
6. [Diseño de POO](#-diseño-de-poo)  
7. [Menú de consola y operaciones](#-menú-de-consola-y-operaciones)  
8. [Ejemplo de uso](#-ejemplo-de-uso)  
9. [Distribución del trabajo (3 integrantes)](#-distribución-del-trabajo-3-integrantes)  
10. [Convenciones de ramas y commits](#-convenciones-de-ramas-y-commits)  
11. [Checklist de evaluación](#-checklist-de-evaluación)  
12. [Mejoras futuras (opcional)](#-mejoras-futuras-opcional)

---

## Objetivo del proyecto

- Implementar una aplicación mínima que resuelva las operaciones del tema **Escuela**.  
- Demostrar **POO en Python**: **herencia**, **polimorfismo** y **encapsulamiento**.  
- Evidenciar el **trabajo colaborativo** con **ramas protegidas**, **PRs** y **revisiones**.

---

## Requisitos

- **Python 3.10+**  
- **Git** y una cuenta de **GitHub**  
- (Opcional) **venv** para entorno virtual

---

## Estructura del proyecto

escuela/
├── main.py # Punto de entrada: menú de consola
├── models/ # Modelos de dominio (POO)
│ ├── persona.py # Clase base: Persona
│ ├── estudiante.py # Clase Estudiante (hereda de Persona)
│ ├── profesor.py # Clase Profesor (hereda de Persona)
│ └── materia.py # Clase Materia
├── services/ # Casos de uso / lógica de aplicación
│ ├── gestion_estudiantes.py # Altas/listados y consultas de estudiantes
│ └── gestion_notas.py # Registro de notas y cálculo de promedios
├── data/ (opcional) # Persistencia ligera
│ └── .gitkeep
└── README.md
---

##  Paso a paso: ejecución local

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Stivendor/Escuela.git
   cd escuela
Ejecutar el programa
   
   ```bash
   python main.py
   ```

Seguir las instrucciones del menú en consola

🔀 Paso a paso: flujo de trabajo en Git/GitHub
Ramas protegidas:

prod

qa

dev

Ramas de cada integrante:

feat:Angel David-clases

feat:Stiven-notas

feat:Julian-menu

🧩 Diseño de POO
Persona → clase base con atributos comunes (nombre, edad).

Estudiante → hereda de Persona, tiene notas y materias.

Profesor → hereda de Persona, dicta materias.

Materia → tiene nombre, código y relación con estudiantes.

Uso de:

Herencia: Estudiante y Profesor heredan de Persona.

Polimorfismo: Métodos sobrescritos (ej. mostrar información).

Encapsulamiento: Atributos privados con getters/setters.

📋 Menú de consola y operaciones
El main.py mostrará opciones como:

1. Registrar estudiante
2. Registrar profesor
3. Registrar materia
4. Registrar nota a estudiante
5. Calcular promedio de un estudiante
6. Listar estudiantes
7. Salir