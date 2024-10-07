# Superheroes and Powers API

## Table of Contents

- [Superheroes and Powers API](#superheroes-and-powers-api)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [API Endpoints](#api-endpoints)
    - [Heroes](#heroes)
    - [Powers](#powers)
    - [Hero\_Powers](#hero_powers)
  - [Running the Application](#running-the-application)
  - [Testing](#testing)

---

## Project Description

The **Superheroes and Powers API** is a RESTful API built using Flask. It allows tracking superheroes and their powers, modeling relationships between heroes and powers through an intermediary `HeroPower` model. This API supports CRUD operations for heroes, powers, and hero-powers, with validation and error handling to ensure the correctness of the data.

This API is ideal for applications that need to manage superheroes, their abilities, and relationships between them.

---

## Features

- Create and manage superheroes.
- Manage superhero powers.
- Associate heroes with powers through hero-powers.
- Validations for data (e.g., hero power strength and power descriptions).
- Handles error responses for invalid or non-existent resources.
- Follows RESTful conventions and returns appropriate JSON responses.

---

## Technologies Used

- **Python**
- **Flask**: A lightweight web framework.
- **Flask-SQLAlchemy**: ORM for managing database interactions.
- **Flask-Migrate**: Handles database migrations.
- **SQLite**: Database used for development purposes.
- **Pipenv**: For dependency management and virtual environment.
- **SQLAlchemy-Serializer**: Used for converting SQLAlchemy models to JSON with custom field inclusion and exclusion.

---

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KoryrKoryr/Superheroes
   cd Superheroes
   ```
2. **Install Pipenv**:
   If you don't have Pipenv installed, install it via pip:

   ```bash
   pip install pipenv

   ```

3. **Install dependencies**:
   Use Pipenv to install project dependencies:

   ```bash
   pipenv install
   ```

4. **Activate the virtual environment**:
   After installing dependencies, activate the Pipenv environment:

   ```bash
   pipenv shell
   ```

---

## Database Setup

1. **Initialize the database**:
   Set up the database using Flask-Migrate:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade head
   ```

2. **Seed the database**:
   To add initial data to the database for testing, run the provided seed script:

   ```bash
   python seed.py
   ```

---

## API Endpoints

Here are the available API endpoints:

### Heroes

**GET /heroes**: Retrieve all heroes.
Example response:

```
[
    {
        "id": 1,
        "name": "Kamala Khan",
        "super_name": "Ms. Marvel"
    },
    {
        "id": 2,
        "name": "Doreen Green",
        "super_name": "Squirrel Girl"
    },
    {
        "id": 3,
        "name": "Gwen Stacy",
        "super_name": "Spider-Gwen"
    },
    {
        "id": 4,
        "name": "Janet Van Dyne",
        "super_name": "The Wasp"
    },
    {
        "id": 5,
        "name": "Wanda Maximoff",
        "super_name": "Scarlet Witch"
    },
    {
        "id": 6,
        "name": "Carol Danvers",
        "super_name": "Captain Marvel"
    },
    {
        "id": 7,
        "name": "Jean Grey",
        "super_name": "Dark Phoenix"
    },
    {
        "id": 8,
        "name": "Ororo Munroe",
        "super_name": "Storm"
    },
    {
        "id": 9,
        "name": "Kitty Pryde",
        "super_name": "Shadowcat"
    },
    {
        "id": 10,
        "name": "Elektra Natchios",
        "super_name": "Elektra"
    }
]
```

**GET /heroes/**: Retrieve a specific hero by ID, including the associated powers.
Example response:

```
{
    "hero_powers": [
        {
            "hero_id": 1,
            "id": 1,
            "power": {
                "description": "allows the wielder to use her senses at a super-human level",
                "id": 3,
                "name": "super human senses"
            },
            "power_id": 3,
            "strength": "Average"
        }
    ],
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
}
```

### Powers

**GET /powers**: Retrieve all powers.
Example response:

```
[
    {
        "description": "Obtain strength that is beyond human level.",
        "id": 1,
        "name": "super strength"
    },
    {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
    },
    {
        "description": "allows the wielder to use her senses at a super-human level",
        "id": 3,
        "name": "super human senses"
    },
    {
        "description": "can stretch the human body to extreme lengths",
        "id": 4,
        "name": "elasticity"
    }
]
```

**GET /powers/**: Retrieve a specific power by ID.
Example response:

```

{
    "description": "Obtain strength that is beyond human",
    "id": 1,
    "name": "super strength"
}

```

**PATCH /powers/**: Update a power's description.
Example request:

```

{
  "description": "Obtain strength that is beyond human level."
}

```

Example response:

```

{
    "description": "Obtain strength that is beyond human level.",
    "id": 1,
    "name": "super strength"
}

```

### Hero_Powers

**POST /hero_powers**: Create a new hero-power association.
Example request:

```
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 3
}
```

Example response:

```
{
    "hero": {
        "id": 3,
        "name": "Gwen Stacy",
        "super_name": "Spider-Gwen"
    },
    "hero_id": 3,
    "id": 12,
    "power": {
        "description": "Obtain strength that is beyond human",
        "id": 1,
        "name": "super strength"
    },
    "power_id": 1,
    "strength": "Strong"
}
```

---

## Running the Application

To run the application locally:

1.  **Activate the virtual environment**:

    ```bash
    pipenv shell
    ```

2.  **Select Flask app**

    ```bash
    FLASK_APP=app.py
    ```

3.  **Run the Flask development server**:

    ```bash
    flask run
    ```

4.  **Access the API**:
    The Flask application will be available at http://127.0.0.1:5000 or http://localhost:5000.

---

## Testing

To test the API, you can use Postman or curl to make requests to the following endpoints:

**GET /heroes**
**GET /heroes/**
**GET /powers**
**PATCH /powers/**
**POST /hero_powers**

Additionally, you can import the provided Postman collection (challenge-2-superheroes.postman_collection.json) to test all routes.

---
