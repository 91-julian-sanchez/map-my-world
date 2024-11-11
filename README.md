# API Map My World

This project provides an API to manage locations, categories, and recommendations. It uses FastAPI, SQLAlchemy, and Alembic for database management, and Docker for deployment and execution.

## Prerequisites

- Docker
- Docker Compose
- Python 3.x (optional, if you prefer to run without Docker)

## Installation

### Start the container

To start the container and build the application, run the following command in your terminal:

```bash
docker-compose up -d --build
```

This command will download the necessary images (if not already present), build the container, and run it in the background (-d).

## Run migrations

Once the container is running, execute the Alembic migrations to create the tables in the database:

```bash
docker-compose exec web alembic upgrade head
```

This command will apply the migrations to the database and ensure it's up to date with the latest schema changes.

## Documentation
The interactive API documentation is available via Swagger UI. To access it, open your browser and navigate to the following URL:

http://localhost:8000/docs#/

Here you can view all the available endpoints, with descriptions and the ability to test them directly from the interface.

## Main Endpoints
* **GET** `/locations`: Get a list of all locations.
* **POST** `/locations`: Create a new location.
* **GET** `/categories`: Get a list of all categories.
* **POST** `/categories`: Create a new category.
* **GET** `/recommendations/review`: Get the recommendations that have been reviewed.
* **POST** `/recommendations/review`: Add a new recommendation review.
* **GET** `/recommendations/not-reviewed`: Get combinations of recommendations that have not been reviewed.