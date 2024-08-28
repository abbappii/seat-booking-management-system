# Seat Booking Management System

## Overview

This is a Django-based backend system for managing seat bookings in a venue. The system handles venues, events, seats, and bookings. It supports creating, updating, and managing seat reservations with validation to prevent double bookings.

## Features

- **Venue Management**: Create and manage venues where events are held.
- **Seat Management**: Define seats within a venue and associate them with specific events.
- **Booking Management**: Book seats for events, with validation to prevent double bookings.
- **Event Management**: Create and manage events held in venues.
- **Seat Type**: Define different types of seats (e.g., VIP, Regular) with price multipliers.

## Setup

### Prerequisites

- Python 3.8+
- Django 3.2+
- PostgreSQL
- `pip` for managing Python packages

### Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:abbappii/seat-booking-management-system.git (ssh)
    cd seat-booking-system
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup the database:**
    - **For SqLite:**
   ```
     username: bappi
     password: bappi
   ```  
      
    - **For PostgreSQL:**
        Update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials. Here is an example configuration:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Then, apply migrations:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Admin Dashboard:**

    Open your browser and go to `http://127.0.0.1:8000/admin/` to log in with the superuser credentials.

## API Endpoints

All API endpoints are prefixed with `api/v1/`.

### Venue Endpoints

- **List Venues**: `GET /api/v1/venues/`
- **Create Venue**: `POST /api/v1/venues/`
- **Retrieve Venue**: `GET /api/v1/venues/{id}/`
- **Update Venue**: `PUT /api/v1/venues/{id}/`
- **Delete Venue**: `DELETE /api/v1/venues/{id}/`

### Event Endpoints

- **List Events**: `GET /api/v1/events/`
- **Create Event**: `POST /api/v1/events/`
- **Retrieve Event**: `GET /api/v1/events/{id}/`
- **Update Event**: `PUT /api/v1/events/{id}/`
- **Delete Event**: `DELETE /api/v1/events/{id}/`

### SeatType Endpoints

- **List SeatType**: `GET /api/v1/seats/type/`
- **Create SeatType**: `POST /api/v1/seats/type/`
- **Retrieve SeatType**: `GET /api/v1/seats/type/{id}/`
- **Update SeatType**: `PUT /api/v1/seats/type/{id}/`
- **Delete SeatType**: `DELETE /api/v1/seats/type/{id}/`

  
### Seat Endpoints

- **List Seats**: `GET /api/v1/seats/`
- **Create Seat**: `POST /api/v1/seats/`
- **Retrieve Seat**: `GET /api/v1/seats/{id}/`
- **Update Seat**: `PUT /api/v1/seats/{id}/`
- **Delete Seat**: `DELETE /api/v1/seats/{id}/`

### Booking Endpoints

- **List Bookings**: `GET /api/v1/bookings/`
- **Create Booking**: `POST /api/v1/bookings/`
- **Retrieve Booking**: `GET /api/v1/bookings/{id}/`
- **Update Booking**: `PUT /api/v1/bookings/{id}/`
- **Delete Booking**: `DELETE /api/v1/bookings/{id}/`

## Running Tests

You can run tests using Django's test runner:

```bash
python manage.py test
