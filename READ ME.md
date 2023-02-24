starwarAPI
PROJECT STRUCTURE
starwarsAPI (project root directory)

  - task_one.py 
  - task_two.py
  - requirements.txt
  - README.md 
  - venv  
  - utils
      - __init__.py
      - fetch_data.py
      - randgen.py
      - timing.py
  - models
      - __init__.py
      - datamodels
          - __init__.py
          - films.py
          - planets.py 
          - spacies.py
          - starships.py
          - vehicles.py
Project Creations STEPS
Open Pycharm
Open Project
Choose desired directory for project (project destination)
Choose project name (project root directory)
Go with default selections and click on "create" button
Pycharm will automatically create 1 directory (venv), 1 file (main.py)
Delete main.py file.
NOTE -

README.md is a file typically found under most Python projects.
This file represents documentation about the project.
https://pypi.org/ (external packages)

Web portal that hosts authorized libraries (authorized by Python.org)
Index URL (repository host)
How to find any third party library?
https://pypi.org/

search
Library naming convention
https://pypi.org/project/requests/

requests 2.28.2

Software release versioning
MAJOR
MINOR
PATCH
android 6.1.1

Who has created libraries that are under pypi.org?
Python users (Developers)
Web Application = Backend (API) + FrontEnd

API - Application Programming Interface

A software without any front-end
Software that can communicate with other software.
API is an application to which only other applications can interact
Web API -

So any API that understands and can treat HTTP request and response are called as web APIs.

https://www.google.com/
http://<domain.com>
What is HTTP?
HyperText Transfer Protocol
Deaf & Mute - sign language

What is requests?
Requests is an elegant and simple HTTP library for Python, built for human beings.

What are the HTTP methods?
https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

Server (application) <---> Client (user) data + code

HTTP Methods (most important HTTP methods)
POST
GET
PATCH
PUT
DELETE
NOTE - http methods are also called http verbs

Install postman
postman is a tool that allows us to send HTTP requests to web apis.
Terminology
source code :: code of the project/ library
open source :: free to use and free to distribute (free is not in terms of cost but freedom)
CRUD :: Create, Retrieve, Update, Delete
API documentation
documentation / information about how to use API is called API docuemtation

PROJECT - starwarsAPI
----------------------
PROBLEM STATEMENT
----------------------


The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.

HTTP vs HTTPs
HTTP without security
HTTPs with security (encryption)
What is URL?
Uniform Resource Locator
https://swapi.dev/api/people/1/

Domain name:

HOME URL - https://swapi.dev relative URL - /api/people/1/

Resources on starwars
people

PLURAL (https://swapi.dev/api/people)
SINGULAR (https://swapi.dev/api/people/1)
film

PLURAL (https://swapi.dev/api/films)
SINGULAR (https://swapi.dev/api/films/1)
starships

vehicles