# AccountFeature-Nakashima-Kunihiko-g8

A full-stack Django web application implementing custom user authentication, Role-Based Access Control (RBAC), and core CRUD functionality backed by PostgreSQL.

## Features

* **Custom User Model (`CustomUser`)**: Extends Django's authentication system with role distinctions (`ADMIN` and `MEMBER`) and profile management.
* **Role-Based Access Control (RBAC)**: Custom `@role_required` decorators and template-level checks restricting administrative dashboards and global record management to authorized roles.
* **Core Record Management (CRUD)**: Authenticated users can create, read, update, and delete records (`ItemOrRecord`), with strict ownership verification preventing members from altering another user's data.
* **PostgreSQL Integration**: Configured via `psycopg` and environment variables (`python-dotenv`) for secure database connectivity.

## Tech Stack

* **Backend**: Python 3.14, Django 6.1.3
* **Database**: PostgreSQL / Supabase (`psycopg[binary]`)
* **Environment & Media**: `python-dotenv`, `Pillow`

## Project Structure

```text
AccountFeature-Nakashima-Kunihiko-g8/
├── accounts/          # Custom user model, auth views, RBAC decorators, profiles
├── config/            # Project settings, root URL routing, WSGI/ASGI
├── core/              # Domain models (ItemOrRecord), CRUD views, forms, URLs
├── templates/         # Base layout and account templates
├── manage.py
└── requirements.txt
