INSTRUCCIONES PARA CORRER PRUEBAS

1. Esta debe ser la estructura de archivos
   tareas/
   │
   ├── features/
   | └── tarea.feature
   └── steps/
   └── tarea.py

2. Crear un ambiente virtual en la carpeta raíz (tareas)

   python -m venv venv

3. Activar ambiente virtual

   venv\Scripts\activate

4. Instalar dependencias necesarias

   pip install behave selenium

5. Desde la carpeta raíz (tareas) ejecutar

   behave
