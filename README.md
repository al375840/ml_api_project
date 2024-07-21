# ML API Project

## Description

This project is an API for training and predicting machine learning models using the Iris dataset. The API is built with FastAPI and allows storing and retrieving models in MongoDB.

## Installation

### Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

### Project Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/al375840/ml_api_project.git
    cd ml_api_project
    ```

2. Install dependencies:
    ```sh
    poetry install
    ```

3. Activate the virtual environment:
    ```sh
    poetry shell
    ```

4. Start the server:
    ```sh
    uvicorn app.main:app --reload
    ```

5. Access the API documentation in your browser:
    ```sh
    http://127.0.0.1:8000/docs
    ```

5. There user is adrian and the password is leon to get the token