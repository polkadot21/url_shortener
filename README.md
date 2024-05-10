# URL Shortener

A simple URL shortening service built with FastAPI, using PostgreSQL for storage, 
Docker for easy deployment, and SQLAlchemy for ORM.

## Features
- Shorten URLs: Convert long URLs into manageable short links.
- Redirect: Use short links to redirect to the original URLs.

## Requirements
- Docker & Docker compose

## Usage

1. Clone the repo

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

2. Build & Run in Docker

```bash
docker compose up --build
```

## API Schema

- `POST /shorten/`: Shorten a new URL.
    Input: original_url (query parameter)
    Returns: Shortened URL
- `GET /{short_url}`: Redirects to the original URL using the shortened link.
- `GET /health`: Checks the DB connection.
