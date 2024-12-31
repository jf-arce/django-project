# Proyecto Django - [Consultorio Médico]

Este es un proyecto Django para practicar.

## Requisitos

- Python 3.x
- Pip
- Git

## Pasos para ejecutar el proyecto

### 1. Clonar el repositorio

### 2. Crear un entorno virtual y activarlo

```bash
python -m venv venv
```

- En Windows:  
  ```bash
  venv\Scripts\activate
  ```

- En macOS/Linux:  
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto y agrega tus variables de entorno (por ejemplo, `SECRET_KEY`, `DB_NAME`, etc.). No subas este archivo a GitHub.

### 5. Realizar migraciones

```bash
python manage.py migrate
```

### 6. Cargar los datos iniciales de la base de datos

Para cargar los datos de ejemplo en la base de datos (si los tienes en un archivo `fixtures` o como datos iniciales), puedes hacerlo ejecutando el siguiente comando:

```bash
python manage.py loaddata nombre_del_archivo_fixture.json
```

Si no tienes un archivo `fixture`, puedes crear uno utilizando el siguiente comando:

```bash
python manage.py dumpdata app_name.ModelName --output=nombre_del_archivo_fixture.json
```

Este comando generará un archivo con los datos actuales de la base de datos para que puedas compartirlos con otros.

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`.
