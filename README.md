# ShopPharma E-commerce Application
## Introduction
ShopPharma is an **E-Commerce** **Python/Django** application made for pharmaceutical sale businesses. It has features such as authentication,drug lists, carts, coupons, make orders and payments, view order history.

## Tech Stack
- Python as the server language
- Django Framework as the server framework
- PostgreSQL as the database.
- HTML, CSS, JavaScripts with Bootstrap 4 for the application's frontend.

## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── manage.py *** the main driver of the app. 
                    "python manage.py runserver" to run after installing dependences
  ├── Authentication *** Authentication application
        ├── static
        │   ├── css
        │   ├── bootstrap
        │   ├── fonts
        │   ├── images
        │   └── js
        └── templates
            ├── authentications
            └── base.html
        ├── admin.py *** admin app for the authentication
        ├── forms.py *** forms for rendering on registration and login pages.
        ├── models.py *** Models for authentication
        ├── urls.py *** URLS for the authentication application
        └── views.py *** View functions for the authentication app
  ├── cart *** Cart application
  ├── coupons *** Coupon system application
  ├── orders *** Orders application
  ├── shop *** Products applications
  ├── Shoppharm *** Project folder
  │     ├── settings
  │     │   ├── base.py *** settings of the project
  │     │   ├── development.py *** setting for development environment
  │     │   └── production.py  *** setting for production environment
        └── url.py *** main urls.py file
  └── requirements.txt 
  
  ```


## Features
- Users can signup and login to the e-commerce platform.
- Users can reset their passwords.
- Users can view all listings of drugs on the platform marked as available by the admin.
- Admin can post products on the platform.
- Users can choose to **Create, Read, Update, Delete** a drug to their cart and checkout to make payment.
- Users that make orders will recieve emails confirming their orders have been recieved by the admin.
- Users can view history of all their purchases.
- Admin can view all orders created and can print PDF of the invoices.
- Admin can download orders as csv file for Data Analysis or other purposes.

## Authentication
Users can signup onto the system with details such as First Name, Last Name, Email Addresse, Telephone, Password.

Users will be authenticated using only their **Email Address** and **Password**.



## Development Setup
To start and run the local development server,
Clone the repository, run the virtual environment and install all requirements.



1. Initialize and activate a virtualenv:
```bash
  git clone https://github.com/Emmanuel-Okyere/shoppharma.git
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate --linux
  for windows run
  venv/Scripts/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
  ```

4. Navigate to Home page [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Preview
You can access the live application using the provided link below.

[Live Preview](https://shoppharm.herokuapp.com/)


## Visuals
### Home Page
![Home Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/1-Product%20Home.png?raw=true)
### Product Details Page
![Product Details Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/2-%20Product%20details.png?raw=true)
### Cart Page
![Cart Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/3-Product%20Cart.png?raw=true)
### Checkout Page
![Checkout Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/4-Product%20Checkout.png?raw=true)
### Order Payment Page
![Order Payment Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/6-Order%20Payment.png?raw=true)
### Payment Success Page
![Payment Success Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/7-Order%20Payment%20Success.png?raw=true)

### Order History Page
![Order History Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/5-Order%20History.png?raw=true)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Project status
This project is still under development. 
