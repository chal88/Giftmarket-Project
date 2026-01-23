# Giftmarket – Django eCommerce Application

## Description
Giftmarket is a Django-based eCommerce application that supports both buyers and vendors.
Vendors can create stores and manage products, while buyers can browse products, place
orders, and leave reviews. The project also exposes a RESTful Web API built with
Django REST Framework.

---

## Planning & System Design

This project includes formal planning documentation and system design
artifacts as required by the task specification.

### Planning Documents
All planning files are located in the `Planning/` directory and include:
- Project overview
- Requirements analysis
- UI layout planning
- Security considerations
- Failure and risk planning

### API Sequence Diagrams
API request–response flows are documented using sequence diagrams.

The diagrams are located in the following directory:


These diagrams visually describe:
- Buyer actions (browse products, add to cart, checkout)
- Vendor actions (create store, add/edit/delete products)
- API request and response flow
- Database interactions

Each diagram uses arrows to clearly show the order of interactions
between the Client, Django Views, API endpoints, and Database.

## Features

### Marketplace
- Buyer and Vendor registration
- Vendor profiles and stores
- Product listings and product detail pages
- Shopping cart and checkout
- Order history
- Product reviews (verified purchases)
- Vendor dashboard for managing products

### Web API
- RESTful API using Django REST Framework
- Public read-only endpoints
- Vendor-protected endpoints
- JSON responses via DRF serializers
- Browsable API interface

---

## Technologies Used
- Python 3.13
- Django 6.0
- Django REST Framework
- MySQL / MariaDB
- Bootstrap 5

---

## Known Limitations
- Twitter (X) API posting is disabled if API credentials are not configured.
- Image uploads require correct MEDIA settings.

## Project Structure (High-Level)

.
├── create_default_image.py
├── generate_images.py
├── Giftmarket
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── settings.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   └── wsgi.cpython-313.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── static
│   │   └── test.css
│   ├── templates
│   │   └── home.html
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   └── products
│       ├── Blue_T-shirt-3_hheNW4y.png
│       ├── Blue_T-shirt-3.png
│       ├── Cotton_bag8_2pugDvK.png
│       ├── Cotton_bag8_aWGfJKM.png
│       ├── Cotton_bag8.png
│       ├── IMG_8813_wqe8ILZ.jpeg
│       ├── IMG_8813_zHV3Gy5.jpeg
│       ├── IMG_8813.jpeg
│       ├── Notebook-3_nfM3iHL.png
│       ├── Notebook-3_zRXyyxI.png
│       ├── Notebook-3.png
│       ├── product1_02f3amf.png
│       ├── product1_6BNQu3y.jpg
│       ├── product1_bIQIAz5.jpg
│       ├── product1_dhTNo9d.png
│       ├── product1.jpg
│       ├── product1.png
│       ├── product2_F0o3Lsc.png
│       ├── product2_kWvXYEd.jpg
│       ├── product2_qXI7Jdk.jpg
│       ├── product2_sv5hDYL.png
│       ├── product2.jpg
│       ├── product2.png
│       ├── product3_fC2hEDo.png
│       ├── product3_kVCtfn3.jpg
│       ├── product3.jpg
│       ├── product3.png
│       ├── Red_mug-3_b4j2cUQ.png
│       ├── Red_mug-3_XnV7Hdw.png
│       ├── Red_mug-3.png
│       ├── Untitled_design-5_3RyHqGN.png
│       ├── Untitled_design-5.png
│       ├── Untitled_design-6_usroDba.png
│       ├── Untitled_design-6.png
│       └── Untitled_design-8.png
├── myenv
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── Activate.ps1
│   │   ├── django-admin
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.13
│   │   ├── python -> python3.13
│   │   ├── python3 -> python3.13
│   │   ├── python3.13 -> /opt/homebrew/opt/python@3.13/bin/python3.13
│   │   └── sqlformat
│   ├── include
│   │   └── python3.13
│   ├── lib
│   │   └── python3.13
│   │       └── site-packages
│   │           ├── asgiref
│   │           ├── asgiref-3.11.0.dist-info
│   │           ├── django
│   │           ├── django-6.0.dist-info
│   │           ├── djangorestframework-3.16.1.dist-info
│   │           ├── mysql-0.0.3.dist-info
│   │           ├── mysqlclient-2.2.7.dist-info
│   │           ├── MySQLdb
│   │           ├── PIL
│   │           ├── pillow-12.0.0.dist-info
│   │           ├── pip
│   │           ├── pip-25.2.dist-info
│   │           ├── rest_framework
│   │           ├── sqlparse
│   │           └── sqlparse-0.5.4.dist-info
│   └── pyvenv.cfg
├── Planning
│   ├── failure_plan.md
│   ├── project_overview.md
│   ├── requirements.md
│   ├── security_plan.md
│   └── ui_layout.md
├── README.md
├── sequence_api_diagram
│   ├── eCommerce App 2 Sequence Diagram 2.png
│   ├── eCommerce App 2 Sequence Diagram 4.png
│   ├── eCommerce App 2 Sequence Diagram.png
│   └── eCommerce App Sequence Diagram 3.png
├── shop
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── admin.cpython-313.pyc
│   │   ├── api_urls.cpython-313.pyc
│   │   ├── api_views.cpython-313.pyc
│   │   ├── apps.cpython-313.pyc
│   │   ├── forms.cpython-313.pyc
│   │   ├── models.cpython-313.pyc
│   │   ├── permissions.cpython-313.pyc
│   │   ├── serializers.cpython-313.pyc
│   │   ├── tests.cpython-313.pyc
│   │   ├── twitter_service.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   └── views.cpython-313.pyc
│   ├── admin.py
│   ├── api_urls.py
│   ├── api_views.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── 0001_initial.cpython-313.pyc
│   │   │   ├── 0002_alter_product_image.cpython-313.pyc
│   │   │   └── 0002_rename_buyer_review_user_cartitem.cpython-313.pyc
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_product_image.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── templates
│   │   ├── registration
│   │   │   ├── login.html
│   │   │   ├── password_reset_complete.html
│   │   │   ├── password_reset_confirm.html
│   │   │   ├── password_reset_done.html
│   │   │   └── password_reset_form.html
│   │   └── shop
│   │       ├── add_product.html
│   │       ├── add_to_cart.html
│   │       ├── base.html
│   │       ├── buyer_signup.html
│   │       ├── cart.html
│   │       ├── checkout_success.html
│   │       ├── delete_product.html
│   │       ├── edit_product.html
│   │       ├── email_invoice.html
│   │       ├── home.html
│   │       ├── order_history.html
│   │       ├── product_detail.html
│   │       ├── product_list.html
│   │       ├── review_form.html
│   │       ├── vendor_dashboard.html
│   │       ├── vendor_orders.html
│   │       └── vendor_signup.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── shop_extras.cpython-313.pyc
│   │   └── shop_extras.py
│   ├── tests.py
│   ├── twitter_service.py
│   ├── urls.py
│   └── views.py
├── static
│   └── images
│       └── default.png
└── venv
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── Activate.ps1
    │   ├── django-admin
    │   ├── normalizer
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.13
    │   ├── python -> python3.13
    │   ├── python3 -> python3.13
    │   ├── python3.13 -> /opt/homebrew/opt/python@3.13/bin/python3.13
    │   └── sqlformat
    ├── include
    │   └── python3.13
    ├── lib
    │   └── python3.13
    │       └── site-packages
    │           ├── asgiref
    │           ├── asgiref-3.11.0.dist-info
    │           ├── certifi
    │           ├── certifi-2025.11.12.dist-info
    │           ├── charset_normalizer
    │           ├── charset_normalizer-3.4.4.dist-info
    │           ├── django
    │           ├── django-6.0.dist-info
    │           ├── djangorestframework-3.16.1.dist-info
    │           ├── idna
    │           ├── idna-3.11.dist-info
    │           ├── mysql-0.0.3.dist-info
    │           ├── mysqlclient-2.2.7.dist-info
    │           ├── MySQLdb
    │           ├── oauthlib
    │           ├── oauthlib-3.3.1.dist-info
    │           ├── PIL
    │           ├── pillow-12.0.0.dist-info
    │           ├── pip
    │           ├── pip-25.2.dist-info
    │           ├── requests
    │           ├── requests_oauthlib
    │           ├── requests_oauthlib-2.0.0.dist-info
    │           ├── requests-2.32.5.dist-info
    │           ├── rest_framework
    │           ├── sqlparse
    │           ├── sqlparse-0.5.5.dist-info
    │           ├── tweepy
    │           ├── tweepy-4.16.0.dist-info
    │           ├── urllib3
    │           └── urllib3-2.6.2.dist-info
    └── pyvenv.cfg


## Installation & Setup Instructions

### 1. Clone the repository
git clone <repository-url>
cd GiftmarketProject

## Planning & Design

This project includes planning documentation in the form of a sequence diagram
that explains how the main API endpoints interact.

- File: `sequence_api_diagram.md`
- Covers cart, checkout, and vendor product management flows

##### Note to mentor/lecturer
After amny attempts and mentor calls, I have tried correcting and finding solutions to fix the error with Mysql and I keep 
running into errors that link to what seems to be a broken file, trying multiple times to fix even after uninstalling Mysql
and re-installing. I cannot therefore test my task after making corrections.