# My Django App

## Overview

This is a simple Django app that demonstrates how to build and run a Django app using venv and Docker.

## Prerequisites

- Python latest/3.11
- pip
- virtualenv (for running with venv)
- Docker (for running with Docker)

## Running with venv

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd my-django-app`
3. Create a virtual environment: `virtualenv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the development server: `python manage.py runserver`

## Running with Docker

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd my-django-app`
3. Build the Docker image: `docker build -t my-django-app .`
4. Run a container from the image: `docker run -p 8000:8000 my-django-app`
