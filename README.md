# Sistema de Biblioteca en Python

Este repositorio contiene un sistema de biblioteca simple desarrollado en Python. El sistema utiliza archivos de texto como base de datos para almacenar información sobre eventos, libros, miembros y préstamos.

## Estructura de archivos

- **eventos.txt**: Almacena información sobre eventos relacionados con la biblioteca.
- **libros.txt**: Contiene detalles sobre los libros disponibles en la biblioteca.
- **miembros.txt**: Registra información de los miembros de la biblioteca.
- **prestamos.txt**: Guarda registros de los préstamos realizados por los miembros.

## Funcionamiento del sistema

### 1. Ejecución del programa

El programa principal se encuentra en el archivo `biblioteca.py`. Puedes ejecutarlo usando el siguiente comando:

```bash
python biblioteca.py
```

### 2. Menú de opciones

El sistema ofrece un menú interactivo con las siguientes opciones:

- **1. Gestionar Libros**: Permite agregar, editar o eliminar libros de la biblioteca.
- **2. Gestionar Miembros**: Permite agregar, editar o eliminar miembros de la biblioteca.
- **3. Gestionar Eventos**: Permite agregar, editar o eliminar eventos relacionados con la biblioteca.
- **4. Realizar Préstamo**: Permite a los miembros realizar préstamos de libros.
- **5. Ver Préstamos**: Muestra los préstamos actuales.
- **6. Salir**: Cierra el programa.

### 3. Almacenamiento de datos

La información se guarda y recupera de los archivos de texto mencionados anteriormente. Cada tipo de dato (libros, miembros, eventos, préstamos) tiene su propio formato de archivo para facilitar la lectura y escritura.

## Clonar el Repositorio

Para clonar este repositorio, ejecuta el siguiente comando en tu terminal:

```bash
git clone https://github.com/RodrigoCG1306/Biblioteca.git
```

Recuerda reemplazar `RodrigoCG1306` con tu nombre de usuario de GitHub si es necesario.

## Requisitos

Asegúrate de tener Python instalado en tu sistema. Puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

¡Listo! Ahora puedes explorar y utilizar este sistema de biblioteca en Python. Si tienes alguna pregunta o encuentras problemas, no dudes en abrir un problema en el repositorio.

¡Disfruta gestionando tu biblioteca con este sistema en Python!
