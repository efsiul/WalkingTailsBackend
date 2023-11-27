# **Walking Tails Backend System**

A comprehensive Walking tails backend system built using FastAPI and PostgreSQL.

Project Structure
Describe the main components of your project here:

* app/main: Contains the main FastAPI application, models, routers, schemas, etc.
* app/tests: Contains unit, integration, and end-to-end tests.
* db: Alembic configuration and database migration scripts.

## 1. Three-Tier Architecture

```bash
/walkingTailsBackend
|-- /app
|   |-- /main
|   |   |-- __init__.py
|   |   |-- /models
|   |   |   |-- __init__.py
|   |   |   |-- duenoMascota.py
|   |   |   |-- enfermeria.py
|   |   |   |-- estilizado.py
|   |   |   |-- mascota.py
|   |   |   |-- paseador.py
|   |   |   |-- paseo.py
|   |   |   |-- servicio.py
|   |   |-- /schemas
|   |   |   |-- __init__.py
|   |   |   |-- duenoMascota.py
|   |   |   |-- enfermeria.py
|   |   |   |-- estilizado.py
|   |   |   |-- mascota.py
|   |   |   |-- paseador.py
|   |   |   |-- paseo.py
|   |   |   |-- servicio.py
|   |   |-- /routers
|   |   |   |-- __init__.py
|   |   |   |-- duenoMascota.py
|   |   |   |-- enfermeria.py
|   |   |   |-- estilizado.py
|   |   |   |-- mascota.py
|   |   |   |-- paseador.py
|   |   |   |-- paseo.py
|   |   |   |-- servicio.py
|   |   |-- /dependencies
|   |   |-- /utils
|   |   |-- main.py  (FastAPI main application)
|   |-- /tests
|   |   |-- /unit
|   |   |-- /integration
|   |   |-- /end_to_end
|-- /db
|   |-- alembic.ini
|   |-- database.py
|   |-- env.py
|   |-- /versions (migration scripts)
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## **Common Features for Both Architectures:**

1. app/main : Houses the main FastAPI application, models (ORM models), schemas (Pydantic models), routers (API routes), and other utility modules.

2. app/tests :

    * unit        : Contains unit tests.
    * integration : Contains tests that might involve database operations, third-party services, etc.
    * end_to_end  : End-to-end or functional tests for the API.

3. db : Contains database migration related files using Alembic.
4. Dockerfile : Contains instructions to containerize the application.
5. docker-compose.yml : Contains instructions for running the app and its dependencies (like a database) in Docker containers.
6. requirements.txt : List of Python dependencies.
7. README.md : Documentation for setting up and running the project.

## **Setting Up Development Environment**

1. Clone the Repository:

    ```bash
        git clone git@github.com:Hospital-General-de-Medellin/WalkingTailsBackend.git
    ```

2. Navigate to the Project Directory:

    ```bash
        cd WalkingTailsBackend
    ```

3. Set Up Virtual Environment:

    ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

4. Install Dependencies:

    ```bash
        pip install -r requirements.txt
    ```

5. Run the Application:

    ```bash
        uvicorn app.main.main:app --reload
    ```

## Database Migrations

Instructions on setting up the database, running migrations, etc.

## Testing

Describe how to run tests:

```bash
    #Run all tests
    pytest app/tests
```

## Deployment

Instructions or links to guides on deploying the application.

## Contributing

Guidelines for contributing to the project, if applicable.

## License

Your license info here, if any.
