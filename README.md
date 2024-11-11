# API Map My World

Este proyecto proporciona una API para gestionar ubicaciones, categorías y recomendaciones. Utiliza FastAPI, SQLAlchemy y Alembic para la gestión de la base de datos, y Docker para la ejecución y despliegue.

## Requisitos Previos

- Docker
- Docker Compose
- Python 3.x (opcional, si prefieres ejecutarlo sin Docker)

## Instalación

### Iniciar el Contenedor

Para iniciar el contenedor y construir la aplicación, ejecuta el siguiente comando en tu terminal:

```bash
docker-compose up -d --build
```

Este comando descargará las imágenes necesarias (si aún no están presentes), construirá el contenedor y lo ejecutará en segundo plano (-d).

## Ejecutar Migraciones

Una vez que el contenedor esté en ejecución, ejecuta las migraciones de Alembic para crear las tablas en la base de datos:

```bash
docker-compose exec web alembic upgrade head
```

Este comando aplicará las migraciones a la base de datos y asegurará que esté actualizada con los últimos cambios de esquema.

## Documentación
La documentación interactiva de la API está disponible mediante Swagger UI. Para acceder a ella, abre tu navegador y dirígete a la siguiente URL:

http://localhost:8000/docs#/

![alt text](image.png)

Aquí puedes ver todos los endpoints disponibles, con descripciones y la capacidad de probarlos directamente desde la interfaz.

## Endpoints Principales
* **GET** `/locations`: Obtener una lista de todas las ubicaciones.
* **POST** `/locations`:  Crear una nueva ubicación.
* **GET** `/categories`: Obtener una lista de todas las categorías.
* **POST** `/categories`:Crear una nueva categoría.
* **GET** `/recommendations/review`: Obtener las recomendaciones que han sido revisadas.
* **POST** `/recommendations/review`: Agregar una nueva revisión de recomendación.
* **GET** `/recommendations/not-reviewed`: Obtener combinaciones de recomendaciones que no han sido revisadas.