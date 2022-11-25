## Homework 20
This application was created with the purpose is to try different pytest functions like mocks and fixtures. The main part of the application is almost the same as provided in previous repository. 

There're some test classes realized in the application:

 - TestMovieService - the class tests a MovieService class of the app
 - TestGenreService - the class tests a GenreService class of the app
 - TestDirectorService - the class tests a DirectorService class of the app
 There are fixtures and mocks to provide test data for the classes in the files containing the classes.
 ---
The project's structure: 
 - dao - DAOs to work with different tables
 - tests - a python package with all tests described above
 - service- classes provided a business logic
 - views - there are CBVs to work with different routes
 - implemented- there're DAO and Service classes' instances
 - config - configuration class with different settings 
 - requirements.txt - file with the project's dependencies
 - app.py - a main file to start the application
 - setup_db - a file with SQLAlchemy instance
 - movies.db - a database with tables described above
 - README.md - this file with app info
 ---
 The project was created in 25 November 2022 by Aleksey Mavrin
