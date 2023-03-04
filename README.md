# Football Events Web Application
This is a Flask web application that displays football events and games details from a SQLite database. To run this application, please follow the steps below.

## Installation
Before running the application, you need to install Flask. You can install Flask by running the following command in your terminal:

        pip install flask
## Setup
1.Clone this repository to your local machine or to your Codio workspace by running the following command:

        git clone <github-url>

2.Navigate to the project directory by running the following command:

        cd Football_assignment

3.Set the Flask environment variables by running the following commands:

        export FLASK_APP=football.py
        export FLASK_ENV=development
4.Run the application by running the following command:

        python -m flask run -h 0.0.0.0

This will start the Flask development server.

5.Open the "Box Info" option under the "Project" menu in Codio. Find the web URL under "WEB: Static Content" and append "-5000" to the end of the URL to access the application.

## Database Setup
The application uses a SQLite database to store football events and game details. To set up the database, run the following commands:

        python set_up.py

This will create a events_football.db file and populate it with data from the event.csv and ginf.csv files in the archive directory.

## Files
football.py - The main Flask application file that contains the routes and logic for rendering templates and querying the database.
set_up.py - The script that sets up the database and populates it with data from CSV files.
templates/ - The directory containing the HTML templates for the application.
static/ - The directory containing the static files (CSS, JS) for the application.
archive/ - The directory containing the CSV files that are used to populate the database.


