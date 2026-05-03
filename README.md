# Expense Tracker API

## Overview

Expense Tracker is a FastAPI-based backend for managing users, categories, expenses, and analytics. The API is versioned under `/api/v1` and uses Bearer token authentication for protected resources.

## Base URL

- Local development: `http://localhost:8000`
- API root: `http://localhost:8000/api/v1`
- OpenAPI JSON: `http://localhost:8000/openapi.json`
- Swagger UI: `http://localhost:8000/docs`

## Authentication

- Register a new user with `POST /api/v1/auth/register`
- Login with `POST /api/v1/auth/login`
- Protected endpoints require an `Authorization` header:

```http
Authorization: Bearer <access_token>
```

## Run locally

1. Create and activate a Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -e .
```

3. Start the application:

```bash
uvicorn app.main:app --reload
```

4. Visit the docs:

- Swagger: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Auth

#### `POST /api/v1/auth/register`

Create a new user account.

Request body:

```json
{
  "username": "string",
  "email": "user@example.com",
  "password": "stringst"
}
```

Response `201`:

```json
{
  "id": 0,
  "username": "string",
  "email": "string",
  "is_active": true,
  "created_at": "2026-05-03T14:18:11.951Z"
}
```

Possible errors:

- `409 Conflict` if the email is already registered
- `422 Unprocessable Entity` for invalid request data

#### `POST /api/v1/auth/login`

Authenticate an existing user and receive a JWT access token.

Request body:

```json
{
  "email": "user@example.com",
  "password": "string"
}
```

Response `200`:

```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

Possible errors:

- `401 Unauthorized` for invalid credentials
- `422 Unprocessable Entity` for invalid request data

### Users

#### `GET /api/v1/users/me`

Get the current authenticated user's profile.

Response `200`:

```json
{
  "id": 0,
  "username": "string",
  "email": "string",
  "is_active": true,
  "created_at": "2026-05-03T14:18:11.962Z"
}
```

#### `PUT /api/v1/users/me`

Update the authenticated user's profile.

Request body:

```json
{
  "username": "string",
  "email": "user@example.com",
  "password": "stringst"
}
```

Response `200`:

```json
{
  "id": 0,
  "username": "string",
  "email": "string",
  "is_active": true,
  "created_at": "2026-05-03T14:18:11.972Z"
}
```

Possible errors:

- `404 Not Found` if user does not exist
- `422 Unprocessable Entity` for invalid request data

#### `DELETE /api/v1/users/me`

Delete the current authenticated user.

Response `204` No Content

### Categories

#### `GET /api/v1/categories`

List all categories owned by the authenticated user.

Response `200`:

```json
[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "created_at": "2026-05-03T14:18:11.988Z"
  }
]
```

#### `POST /api/v1/categories`

Create a new category.

Request body:

```json
{
  "name": "string",
  "description": "string"
}
```

Response `201`:

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "created_at": "2026-05-03T14:18:11.998Z"
}
```

Possible errors:

- `422 Unprocessable Entity` for invalid request data

#### `PUT /api/v1/categories/{category_id}`

Update an existing category by ID.

Path parameter:

- `category_id` (integer) – ID of the category to update

Request body:

```json
{
  "name": "string",
  "description": "string"
}
```

Response `200`:

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "created_at": "2026-05-03T14:18:12.021Z"
}
```

Possible errors:

- `404 Not Found` if category does not exist
- `422 Unprocessable Entity` for invalid request data

#### `DELETE /api/v1/categories/{category_id}`

Delete a category by ID.

Path parameter:

- `category_id` (integer) – ID of the category to delete

Response `204` No Content

Possible errors:

- `404 Not Found` if category does not exist

### Expenses

#### `GET /api/v1/expenses`

List all expenses for the authenticated user.

Response `200`:

```json
[
  {
    "id": 0,
    "title": "string",
    "amount": 123.45,
    "date": "2026-05-03",
    "note": "string",
    "category_id": 0,
    "created_at": "2026-05-03T14:18:12.050Z"
  }
]
```

#### `POST /api/v1/expenses`

Create a new expense.

Request body:

```json
{
  "title": "string",
  "amount": 1,
  "date": "2026-05-03",
  "note": "string",
  "category_id": 0
}
```

Response `201`:

```json
{
  "id": 0,
  "title": "string",
  "amount": 1.0,
  "date": "2026-05-03",
  "note": "string",
  "category_id": 0,
  "created_at": "2026-05-03T14:18:12.064Z"
}
```

Possible errors:

- `422 Unprocessable Entity` for invalid request data

#### `GET /api/v1/expenses/{expense_id}`

Retrieve a single expense by ID.

Path parameter:

- `expense_id` (integer) – ID of the expense to retrieve

Response `200`:

```json
{
  "id": 0,
  "title": "string",
  "amount": 1.0,
  "date": "2026-05-03",
  "note": "string",
  "category_id": 0,
  "created_at": "2026-05-03T14:18:12.078Z"
}
```

Possible errors:

- `404 Not Found` if expense does not exist
- `422 Unprocessable Entity` for invalid path parameter

#### `PUT /api/v1/expenses/{expense_id}`

Update an existing expense by ID.

Path parameter:

- `expense_id` (integer) – ID of the expense to update

Request body:

```json
{
  "title": "string",
  "amount": 1,
  "date": "2026-05-03",
  "note": "string",
  "category_id": 0
}
```

Response `200`:

```json
{
  "id": 0,
  "title": "string",
  "amount": 1.0,
  "date": "2026-05-03",
  "note": "string",
  "category_id": 0,
  "created_at": "2026-05-03T14:18:12.096Z"
}
```

Possible errors:

- `404 Not Found` if expense does not exist
- `422 Unprocessable Entity` for invalid request data

#### `DELETE /api/v1/expenses/{expense_id}`

Remove an expense by ID.

Path parameter:

- `expense_id` (integer) – ID of the expense to delete

Response `204` No Content

Possible errors:

- `404 Not Found` if expense does not exist

### Analytics

#### `GET /api/v1/analytics/summary`

Get aggregated expense totals for the current user.

Response `200`:

```json
{
  "total_this_month": 0.0,
  "total_last_month": 0.0,
  "total_all_time": 0.0,
  "expense_count_this_month": 0,
  "highest_category": "string"
}
```

#### `GET /api/v1/analytics/by-category`

Get expenses grouped by category.

Response `200`:

```json
[
  {
    "category_id": 0,
    "category_name": "string",
    "total": 0.0,
    "count": 0
  }
]
```

#### `GET /api/v1/analytics/daily`

Get daily analytics breakdown for the current user.

Response `200`:

```json
"string"
```

### Health Check

#### `GET /health`

Verify the application is running.

Response `200`:

```json
{
  "status": "Healthy",
  "app": "Expense Tracker API",
  "version": "0.1.0",
  "environment": "development"
}
```

> Adjust the returned values to match your environment settings.

## Schemas

### `UserCreate`

- `username`: string, 3–50 characters
- `email`: valid email address
- `password`: string, minimum 8 characters

### `UserUpdate`

- `username`: string, 3–50 characters
- `email`: valid email address
- `password`: optional string, minimum 8 characters

### `CategoryCreate` / `CategoryUpdate`

- `name`: string, 1–100 characters
- `description`: optional string, up to 255 characters

### `ExpenseCreate` / `ExpenseUpdate`

- `title`: string, 1–255 characters
- `amount`: decimal greater than `0`, with two decimal places
- `date`: ISO date string, `YYYY-MM-DD`
- `note`: optional string
- `category_id`: optional integer

### `ExpenseResponse`

- `id`: integer
- `title`: string
- `amount`: decimal
- `date`: ISO date string
- `note`: optional string
- `category_id`: optional integer
- `created_at`: timestamp

### `AnalyticsSummary`

- `total_this_month`: decimal
- `total_last_month`: decimal
- `total_all_time`: decimal
- `expense_count_this_month`: integer
- `highest_category`: optional string

### `CategorySummary`

- `category_id`: integer or null
- `category_name`: string or null
- `total`: decimal
- `count`: integer

## Notes

- All protected API endpoints require a valid JWT Bearer token.
- Use the Swagger UI to inspect request/response examples and to test endpoints.
- The API is built with FastAPI and exposes OpenAPI documentation automatically.
