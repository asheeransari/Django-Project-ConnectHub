# ConnectHub

ConnectHub is a simple social media web application built with Django. It was created as a practical project to learn and apply Django concepts while building a real working application.

The project includes user authentication, posts, images, likes, comments, profiles, database relationships, logging, and performance monitoring.

## Features

- User signup, login and logout
- User profile page
- Home feed with posts sorted by newest first
- Create posts with text and optional images
- Like and unlike posts
- Add comments to posts
- Edit and delete own posts
- Django admin panel
- PostgreSQL database
- Generic relationships for likes, comments and images
- Application and error logging
- Request and view performance logging
- Static file handling with WhiteNoise

## Tech Stack

- Python 3.13
- Django 6.1
- PostgreSQL
- Django ORM
- Django Template Language (DTL)
- HTML / CSS
- python-dotenv
- Psycopg 3
- Pillow
- WhiteNoise
- Uvicorn

The project uses Django's built-in authentication, sessions, messages, admin and ContentType framework.

## Project Structure

```text
ConnectHub/
│
├── ConnectHub/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── forms.py
│   ├── middleware.py
│   ├── performance.py
│   ├── urls.py
│   └── views.py
│
├── posts/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
├── static/
├── media/
├── logs/
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Main Django Concepts Used

### MVT Architecture

ConnectHub follows Django's MVT pattern:

- **Model** - Defines database structure and relationships.
- **View** - Handles requests and application logic.
- **Template** - Displays the HTML pages to the user.

### Class-Based Views

The project uses Django generic class-based views such as:

- `ListView`
- `FormView`
- `DetailView`
- `CreateView`
- `UpdateView`
- `DeleteView`
- `LoginView`
- `LogoutView`

`LoginRequiredMixin` is used where authentication is required.

### Forms

Django Forms and ModelForms are used for:

- User signup
- Post creation
- Post editing
- Comment handling

### Database Relationships

The project uses Django ORM relationships, including `ForeignKey`.

Posts are connected to users through:

```python
author = models.ForeignKey(User, on_delete=models.CASCADE)
```

### Generic Relationships

One of the main concepts used in ConnectHub is Django's ContentType framework.

Likes, comments and images use:

- `ContentType`
- `GenericForeignKey`
- `GenericRelation`

This allows these models to be connected to different models without creating separate relationship tables for every possible model.

For example, a like can point to a specific post using:

```text
content_type + object_id
```

This makes the system reusable if features such as Stories or other content types are added later.

### Migrations

Database changes are managed through Django migrations.

Common commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

Migration files should be committed to Git because they describe the database schema changes required to run the project.

## Logging and Performance Monitoring

ConnectHub includes custom logging to make debugging and monitoring easier.

The project uses:

- Python logging
- Custom loggers
- File and console handlers
- Rotating log files
- Error logging
- Performance logging middleware
- A performance decorator for individual views

The performance middleware records information such as request method, URL, response status and execution time.

Logs are stored in:

```text
logs/app.log
logs/errors.log
```

## Static and Media Files

Static files such as CSS are stored in the `static/` directory.

User-uploaded images are stored under `media/`.

Important settings include:

```python
STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles/"
MEDIA_URL = "/media/"
MEDIA_ROOT = "media/"
```

For production, static files are collected using:

```bash
python manage.py collectstatic
```

WhiteNoise is configured to help serve static files in production.

## Environment Variables

Database credentials and other secrets should not be stored directly in the source code.

Create a local environment file such as:

```text
.env.postgres
```

Example:

```env
SECRET_KEY=your-secret-key
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

Keep the real environment file out of Git.

A `.env.example` file can be committed with placeholder values so other developers know which variables are required.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ConnectHub
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scriptsctivate
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env.postgres` in the project root and add your PostgreSQL credentials.

### 5. Create the PostgreSQL database

Create a PostgreSQL database and user, then use those credentials in `.env.postgres`.

The project uses PostgreSQL on the default port `5432`.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create an admin user

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Useful Django Commands

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py createsuperuser
python manage.py collectstatic
python manage.py shell
```

## Git and Security Notes

The following should not be committed to Git:

- `.env.postgres`
- `.env`
- Secret keys
- Database passwords
- `venv/` or `.venv/`
- `media/`
- `logs/`
- `staticfiles/`
- Local database files
- SQL database dumps

Migration files **should** be committed.

Before pushing the project to GitHub, make sure no real secret or database password is present in the repository.

## Documentation

A detailed project documentation PDF is included separately in this repository:

```text
ConnectHub_Django_Documentation.pdf
```

The PDF contains the detailed explanation of the Django concepts, project structure, models, views, forms, authentication, ContentType relationships, migrations, logging, middleware, static/media files, and deployment preparation used while building ConnectHub.

## Current Project Status

The main Django development for ConnectHub is complete as a learning project. The project can be used locally with PostgreSQL and provides a good base for adding more social-media features in the future.

Before a real production deployment, review security settings such as `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, email configuration, media storage, and production database configuration.

## Learning Outcome

This project helped build practical understanding of Django from project setup to a working application, including:

- Django project and app structure
- MVT architecture
- URLs and request flow
- Models and Django ORM
- Forms and validation
- CRUD operations
- Authentication and authorization
- Class-Based Views
- PostgreSQL integration
- Migrations
- Generic relationships and ContentType
- File uploads
- Static and media files
- Middleware
- Logging
- Performance monitoring
- Basic production preparation
