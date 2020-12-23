# HyperCar Django Application
Web application that simulates the workings of a car service shop.
 
## This project makes use of the following:
* Django Framework
* DTL
* HTML / CSS

## Application Features
* Run with python manage.py runserver to start server on localhost:8000.
* /menu path creates customer tickets for services: Change Oil, Inflate Tires, Diagnostic.
* /processing path is a view for the operator, contains number of people in queue for each service and has a button to call next client ticket to get served.
* Upon ticket creation, customer is redirected to the page of his unique ticket number, that also contains an approximate waiting time (according to project algorithm).
* /next path simulates the screen that calls the next customer to get served.

--------------------
This project is part of the <b>JetBrains Academy Python Developer Plan</b>
