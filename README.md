# portflio

Minimal Django portfolio project focused on presenting a personal profile, featured projects, and a direct WhatsApp contact flow.

## Features

- Hero, about, skills, projects, and contact sections
- Project management from Django admin
- SQLite database for simple local setup
- Responsive dark UI with smooth hover states
- Scroll reveal animations with native CSS and JavaScript
- WhatsApp contact CTA

## Stack

- Django
- SQLite
- Django templates
- Custom CSS
- Vanilla JavaScript

## Deploy

This project is prepared for Render deployment with:

- `requirements.txt`
- `build.sh`
- `render.yaml`

Render docs used as reference:

- https://render.com/docs/deploy-django
- https://render.com/docs/configure-environment-variables

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Content management

Use Django admin to update:

- active profile
- project cards
- featured project order

## Static and media

- static files live in `static/`
- uploaded images use `media/`

## Project structure

```text
portflio/
|-- core/
|-- portfolio/
|-- static/
|-- templates/
|-- manage.py
`-- README.md
```

## Notes

- Contact flow uses WhatsApp instead of a database contact form
- Scroll reveal behavior is implemented in `static/js/main.js`
- Production settings use environment variables and WhiteNoise for static files
