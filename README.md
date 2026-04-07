# Elite Estates - Luxury Real Estate Management

**Elite Estates** is a premium web application built with **Django 4.2** designed for high-end real estate management. The project features a sophisticated property catalog, client-agent interactions, and a custom appointment booking system.

## Live Demo
The project is deployed and live at: [https://elite-estates.onrender.com](https://elite-estates.onrender.com)

## Key Features
- **Monaco Property Catalog:** A curated selection of elite properties in Monte Carlo and surrounding districts.
- **Dynamic Search:** Filter and search through luxury listings by keywords or location.
- **Appointment System:** Integrated booking for property viewings with custom status management.
- **Role-Based Access:** Dedicated groups for Agents and Clients with specific permissions.
- **Security & Performance:** Production-ready settings with PostgreSQL and WhiteNoise for static files.

## Tech Stack
- **Backend:** Django 4.2 (Python 3.12)
- **Database:** PostgreSQL (Hosted on Render)
- **Frontend:** HTML5, CSS3 (Custom responsive design)
- **Server:** Gunicorn / WSGI
- **Deployment:** Render.com with Gunicorn

## How to Run Locally
1. **Clone the repository:**
   git clone https://github.com/sibelyazadzhieva/elite-estates.git

2. **Setup Virtual Environment:**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Environment Variables:**
   Create a .env file in the root directory and configure:
   - SECRET_KEY=your_secure_key
   - DEBUG=True
   - DATABASE_URL=your_database_url

5. **Run Migrations & Launch:**
   python manage.py migrate
   python manage.py runserver