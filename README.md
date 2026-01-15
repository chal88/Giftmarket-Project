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

```text
Giftmarket/
├── README.md
├── manage.py
├── Planning/
├── sequence_api_diagram/
├── Giftmarket/
├── shop/
├── media/
├── static/
└── venv/


## Installation & Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd GiftmarketProject

## Planning & Design

This project includes planning documentation in the form of a sequence diagram
that explains how the main API endpoints interact.

- File: `sequence_api_diagram.md`
- Covers cart, checkout, and vendor product management flows
