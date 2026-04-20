# Elite Estates - Luxury Real Estate Management

[cite_start]**Elite Estates** is a premium web application built with **Django 4.2**, designed for high-end real estate management[cite: 4, 19]. [cite_start]The project features a sophisticated property catalog, client-agent interactions, and a custom appointment booking system[cite: 4].

## 🌐 Live Demo
[cite_start]The project is deployed and live at: [https://elite-estates.onrender.com](https://elite-estates.onrender.com) [cite: 64, 65]

## 🚀 Advanced Features (Retake Exam Updates)
To meet the production-ready standards of the retake exam, the following advanced features have been implemented:

* [cite_start]**Asynchronous Task Processing (Celery & Redis):** Background tasks are integrated to improve performance, such as handling confirmation emails for property viewings[cite: 57, 101].
* [cite_start]**Dynamic Review System:** A full CRUD system for property reviews and ratings, managed by owners[cite: 42]. [cite_start]This includes model-level and form-level validators like `MinValueValidator` and `MaxValueValidator`[cite: 25, 27].
* [cite_start]**RESTful API Endpoints:** Two distinct API services built with Django REST Framework (DRF) for external integrations[cite: 37, 102].
* [cite_start]**Comprehensive Testing:** The application includes a suite of **20+ Unit Tests** covering models, forms, views, and API functionality[cite: 63, 104].
* [cite_start]**Role-Based Access Control:** Defined **Agents** and **Clients** groups in the admin site with distinct permissions and access levels[cite: 16, 97].
* [cite_start]**Custom User Model:** The built-in Django User model has been extended to support specific project requirements[cite: 17].

## 🛠️ Technical Stack
* [cite_start]**Backend:** Django 4.2 & Django REST Framework [cite: 19]
* [cite_start]**Asynchronous Processing:** Celery + Redis (Broker) [cite: 57, 101]
* [cite_start]**Database:** PostgreSQL (Hosted on Render) [cite: 61, 64]
* [cite_start]**Static & Media Storage:** WhiteNoise for static files and Cloudinary for persistent media storage[cite: 62].
* [cite_start]**Frontend:** Responsive web design using custom CSS and Bootstrap[cite: 51].

## 💻 Local Setup and Installation

1.  [cite_start]**Clone the repository:** [cite: 10]
    ```bash
    git clone [https://github.com/sibelyazadzhieva/elite-estates.git](https://github.com/sibelyazadzhieva/elite-estates.git)
    ```

2.  [cite_start]**Setup Virtual Environment:** [cite: 10]
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  [cite_start]**Install Dependencies:** [cite: 10, 11]
    ```bash
    pip install -r requirements.txt
    ```

4.  [cite_start]**Configure Environment Variables (.env):** [cite: 12, 73]
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

5.  [cite_start]**Run Migrations and Launch:** [cite: 11]
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

6.  [cite_start]**Start Celery Worker (In a separate terminal):** [cite: 57]
    ```bash
    celery -A elite_estates worker --loglevel=info
    ```

## 🧪 Testing
[cite_start]The project includes automated tests for custom logic, views, and user-related functionality[cite: 63, 104]. [cite_start]To run the suite of **20+ tests**, use the following command: [cite: 63]

```bash
python manage.py test

## 📄 API Documentation
The application provides at least two RESTful API endpoints using appropriate serializers and permissions:

* `GET /properties/api/` - Returns a list of all available property listings.
* `GET /reviews/api/list/` - Returns a list of all user reviews.я