# Flask Web Application with User Authentication and Registration
This is a Flask web application built with Python that provides user authentication and registration functionality. It uses a SQLite database to store user information and the Werkzeug library for password hashing.

## Routes
The application has the following routes:

/: Renders a login page where users can enter their username and password to authenticate.
/authenticate: Processes the user's login request and checks if the username and password match the ones stored in the database. If the user is authenticated, their user ID is stored in the session and they are redirected to the dashboard page.
/dashboard: Renders a dashboard page that shows the authenticated user's username. If the user is not authenticated, they are redirected to the login page.
/register: Renders a registration page where new users can enter their username and password to create an account. If the username already exists, the user is prompted to choose a different username. If the password and confirm password fields do not match, the user is prompted to re-enter their passwords.
/logout: Removes the user's ID from the session and redirects them to the login page.
## Templates
The application has four templates:

dashboard.html: Renders the authenticated user's dashboard, showing their username.
home.html: Renders the home page.
login.html: Renders the login page.
register.html: Renders the registration page.

## Jinja2

We use the Jinja in the html

## Models
The application uses the SQLAlchemy library to interact with a SQLite database. The models folder contains the code for defining the User model, which is used to store user information in the database.

### User Model
The User model has three attributes:

id: A primary key integer field that auto-increments for each new user.
username: A unique string field that stores the user's username. This field is indexed and cannot be null.
password: A string field that stores the user's hashed password. This field cannot be null.
The User model also has a __repr__ method that returns the string representation of a user object. This method is used for debugging and testing purposes.

When a new user is registered, their username and hashed password are stored in a new User object and added to the database. When a user logs in, their username and password are checked against the database to see if they match an existing User object. If they do, the user is authenticated and their user ID is stored in the session.

