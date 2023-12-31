# Halloween Party - Ticket Manager

This project uses Django Rest Framework to manage ticket purchase and QR codes for a Halloween party. It allows users to register, receive QR codes via email, and verify the authenticity of tickets by scanning QR codes.

## Prerequisites

Make sure you have the following tools installed before getting started:

- Python 3.8
- pip (Python package manager)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/halloween-party.git
    cd halloween-party
    ```

2. **Set Up the Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Unix-based systems
    ```

    ```powershell
    .\venv\Scripts\activate  # On Windows PowerShell
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Database**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Optional, for Django Admin Site)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

1. **TIcket registration**

    To register the ticket holder and accompanying guests, make a POST request to the `/api/tickets/` endpoint.

2. **QR generation and email sending**

    After the admin checks the ticket as paid, users will receive an email with a QR code after making a payment.

3. **Verify Tickets**

    Use the QR code scanning functionality to check if a guest has paid and identify them. This qr will redirect to /api/tickets/<id>.
