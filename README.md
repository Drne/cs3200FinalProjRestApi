# cs3200RestApi
The rest api for a database design final project

## Team - "Database Design 2"
Andrew Colgin - colgin.a@northeastern.edu - 1:35 T/F

## The Project
"Recipe Share" is a web app service for users to get access to incredible recipes directly from working chefs.
The system allows customers to form cookbooks of their favorite recipes, to subscribe to their favorite chefs when
they publish new recipes, and for chefs to easily add new recipes to their existing ones.

## Database UML
![UML] (https://ibb.co/6ZhrrkJ)

## User Data Models
There are three user data models used in this project (Customer, Chef, Admin), which all inherit from 
the User table. 

All Users have: 
* id - PK, int
* first_name - string
* last_name - string
* username - string
* password - string
* email - string

Chefs have:
* cuisine_specialty - from the 'cuisine' table as a portable enum

The primary key of a Chef, Admin, and Customer are foreign keys to Users

## Domain Data Models

### Recipes
The recipe table holds recipes created by chefs.
All recipes contain the following:
* id - PK, int
* author - FK(chef)
* name - string
* instructions - string
* cuisine - FK(cuisine)

### Ingredients

Recipes are made up of Ingredients.
Ingredients have the following:
* id - PK, int
* description - string
* amount - float
* unit - string
* recipe_id - FK(recipe)

### Cuisine
cuisine is a table representing a portable enumeration.
The current possible values of cuisine are as follows:
* AMERICAN
* CHINESE

## User Interface Requirements
The UI is running on a JS React webserver

These requirements can also be seen in the repositories package.json:
```
    "@material-ui/core": "^4.11.3",
    "@material-ui/icons": "^4.11.2",
    "@testing-library/jest-dom": "^5.11.10",
    "@testing-library/react": "^11.2.6",
    "@testing-library/user-event": "^12.8.3",
    "axios": "^0.21.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.2.0",
    "react-scripts": "4.0.3",
    "web-vitals": "^1.1.1"
```

## Rest Api Requirements 
The rest api supporting the UI is a flask server

These requirements can also be seen in the api repositories requirements.txt:
```
Flask~=1.1.2
Flask-Cors~=3.0.10
Flask-RESTful~=0.3.8
Flask_SQLAlchemy~=2.5.1
flask-marshmallow~=0.14.0
marshmallow-sqalchemy~=0.24.2
```