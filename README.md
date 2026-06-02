# Bindu Basini Government Boys' High School

A premium Django website for Bindu Basini Government Boys' High School, Tangail, Bangladesh — one of the oldest and most prestigious educational institutions in Bangladesh, established in 1880.

## Features

- **Home Page** — Hero banner with school stats, recent notices, teachers showcase, achievements, facilities, and notable alumni
- **About Page** — School history, mission/vision, buildings, and subjects offered
- **Teachers Page** — Indexed directory of all teachers with details
- **Headmasters Page** — Complete list of headmasters through history
- **Notices Page** — Important and general notices published via admin panel
- **Alumni Page** — Notable alumni directory
- **Facilities Page** — School facilities showcase
- **Achievements Page** — Milestones and accomplishments
- **Contact Page** — Contact form with validation
- **Admin Panel** — Fully customized with django-jazzmin; manage teachers, notices, alumni, headmasters, facilities, achievements, contact messages, and more

## Design

- **Royal Navy & Gold** aesthetic — deep navy (`#0F1B33`) and gold (`#C9A84C`) color palette
- **Typography** — Playfair Display (headings), Cormorant Garamond (body), Inter (UI)
- **Gold ornamental accents**, animated floating particles, refined cards with hover effects
- **Fully responsive** — mobile-first with smooth animations and slide-in mobile menu
- **Custom admin CSS/JS** for jazzmin integration with matching navy theme

## Tech Stack

- Python 3.14+
- Django 6.0.5
- django-jazzmin 3.0.4 (admin theming)
- Pillow (image handling)
- Whitenoise (static files)
- django-storages + boto3 (B2/S3 media storage for production)
- dj-database-url (PostgreSQL for production)
- python-dotenv (environment configuration)

## Quick Start

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
# Clone the repository
git clone <repo-url>
cd bindubasini

# Create virtual environment and install dependencies
uv sync

# Copy environment file and adjust settings
cp .env.example .env  # or use the existing .env

# Run migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Collect static files
uv run python manage.py collectstatic

# Run development server
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

### Admin Panel

Navigate to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

## Production Deployment

### 1. Set environment variables in `.env`:

```bash
DEBUG=False
ALLOWED_HOSTS=.yourdomain.com
SECRET_KEY=<generate-a-strong-key>

# PostgreSQL
DATABASE_URL=postgres://user:password@host:5432/dbname

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_TLS=True

# B2 / S3-compatible Storage (for media/static)
AWS_S3_ENDPOINT_URL=https://s3.us-west-002.backblazeb2.com
AWS_ACCESS_KEY_ID=your-key-id
AWS_SECRET_ACCESS_KEY=your-app-key
AWS_STORAGE_BUCKET_NAME=bindubasini-media
AWS_S3_REGION_NAME=us-west-002

# Security
CSRF_TRUSTED_ORIGINS=https://yourdomain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 2. Collect static files and run migrations

```bash
uv run python manage.py collectstatic
uv run python manage.py migrate
```

### 3. Serve with a production WSGI server

On Linux/macOS (recommended for production):
```bash
uv run gunicorn config.wsgi:application --workers 4 --bind 0.0.0.0:8000
```

On Windows (development/staging):
```bash
uv run waitress-serve --port 8000 config.wsgi:application
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `DEBUG` | `True` | Set to `False` for production |
| `SECRET_KEY` | *(required)* | Django secret key |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated hosts |
| `DATABASE_URL` | *(optional)* | PostgreSQL connection string |
| `EMAIL_HOST` | `smtp.gmail.com` | SMTP server |
| `EMAIL_PORT` | `587` | SMTP port |
| `EMAIL_HOST_USER` | *(optional)* | SMTP username |
| `EMAIL_HOST_PASSWORD` | *(optional)* | SMTP password |
| `AWS_ACCESS_KEY_ID` | *(optional)* | B2/S3 access key |
| `AWS_SECRET_ACCESS_KEY` | *(optional)* | B2/S3 secret key |
| `AWS_STORAGE_BUCKET_NAME` | `bindubasini-media` | B2/S3 bucket name |
| `AWS_S3_ENDPOINT_URL` | B2 endpoint | S3-compatible endpoint |

## Usage with uv

```bash
uv run python manage.py makemigrations    # Create new migrations
uv run python manage.py migrate           # Apply migrations
uv run python manage.py collectstatic     # Collect static files
uv run python manage.py createsuperuser   # Create admin user
uv run python manage.py runserver         # Start development server
uv add <package>                          # Add a new dependency
```

## Project Structure

```
bindubasini/
├── config/               # Django project settings
│   ├── settings.py       # Main settings with jazzmin config
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI application
├── school/               # Main school app
│   ├── models.py         # Teacher, Headmaster, Alumni, AboutInfo, etc.
│   ├── views.py          # All page views
│   ├── admin.py          # Admin configurations
│   ├── urls.py           # URL routing
│   └── context_processors.py  # School info context
├── notice/               # Notice management app
│   ├── models.py         # Notice, NoticeCategory
│   └── admin.py          # Notice admin configuration
├── templates/school/     # HTML templates
├── static/               # CSS, JS, images
│   ├── css/style.css     # Main stylesheet
│   ├── css/admin.css     # Admin customization
│   ├── js/main.js        # Main JavaScript
│   └── js/admin.js       # Admin JavaScript
├── media/                # User-uploaded files
├── staticfiles/          # Collected static files
├── manage.py             # Django management script
└── pyproject.toml        # Project dependencies
```

## Admin Models

| Model | Description |
|---|---|
| Teacher | Staff directory with designation, subject, qualification |
| Headmaster | Historical headmasters with tenure dates |
| Alumni | Notable alumni with achievements |
| Notice | Notices with categories, file attachments, importance flag |
| NoticeCategory | Categorization for notices |
| AboutInfo | Dynamic content sections for about page |
| Facility | School facilities with icons |
| SchoolBuilding | Campus buildings |
| Achievement | School achievements and milestones |
| Subject | Academic subjects offered |
| ContactMessage | Visitor contact form submissions |
| SchoolInfo | Global school information settings |

## License

MIT
