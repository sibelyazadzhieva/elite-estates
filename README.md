# Elite Estates - Luxury Real Estate Management

**Elite Estates** is a premium web application built with **Django 4.2**, designed for high-end real estate management. The project features a sophisticated property catalog, client-agent interactions, and a custom appointment booking system.

## 🌐 Live Demo
The project is deployed and live at: [https://elite-estates.onrender.com](https://elite-estates.onrender.com)

## 🚀 Advanced Features
To meet the production-ready standards, the following advanced features have been implemented:

* **Asynchronous Task Processing (Celery & Redis):** Background tasks are integrated to improve performance, such as handling confirmation emails for property viewings.
* **Dynamic Review System:** A full CRUD system for property reviews and ratings, managed by owners. This includes model-level and form-level validators like `MinValueValidator` and `MaxValueValidator`.
* **RESTful API Endpoints:** Two distinct API services built with Django REST Framework (DRF) for external integrations.
* **Comprehensive Testing:** The application includes a suite of **20+ Unit Tests** covering models, forms, views, and API functionality.
* **Role-Based Access Control:** Defined **Agents** and **Clients** groups in the admin site with distinct permissions and access levels.
* **Custom User Model:** The built-in Django User model has been extended to support specific project requirements.

## 🛠️ Technical Stack
* **Backend:** Django 4.2 & Django REST Framework 
* **Asynchronous Processing:** Celery + Redis (Broker)
* **Database:** PostgreSQL (Hosted on Render) 
* **Static & Media Storage:** WhiteNoise for static files and Cloudinary for persistent media storage.
* **Frontend:** Responsive web design using custom CSS and Bootstrap.

## 💻 Local Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sibelyazadzhieva/elite-estates.git](https://github.com/sibelyazadzhieva/elite-estates.git)
    ```

2.  **Setup Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:** 
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables (.env):** 
    Create a `.env` file in the root directory and configure the following required credentials:
    ```env
    SECRET_KEY=your_secure_django_key
    DEBUG=True
    DATABASE_URL=your_postgresql_database_url
    CELERY_BROKER_URL=redis://localhost:6379/0
    CLOUDINARY_CLOUD_NAME=your_cloud_name
    CLOUDINARY_API_KEY=your_api_key
    CLOUDINARY_API_SECRET=your_api_secret
    ```

5.  **Run Migrations and Launch:** 
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

6.  **Start Celery Worker (In a separate terminal):** 
    ```bash
    celery -A elite_estates worker --loglevel=info
    ```

## 🧪 Testing
The project includes automated tests for custom logic, views, and user-related functionality. To run the suite of **20+ tests**, use the following command: 

```bash
python manage.py test
```

## 📄 API Documentation
The application provides at least two RESTful API endpoints using appropriate serializers and permissions:

* `GET /properties/api/catalog/` - Returns a list of all available property listings.
* `GET /reviews/api/list/` - Returns a list of all user reviews.