# RestauranteClass — Restaurant Management API

REST API for managing orders, menu, and staff at a restaurant, built with FastAPI and MongoDB.

---

## Technologies

- **Python 3.14**
- **FastAPI** — web framework
- **MongoDB** — NoSQL database
- **PyMongo** — MongoDB driver for Python
- **Pydantic** — data validation
- **python-dotenv** — environment variables
- **validate-docbr** — CPF validation

---

## Project Structure

```
src/
  app.py                  ← FastAPI instance
  main.py                 ← application entry point
  controllers/
    menu_controller.py    ← menu logic
    orders_controller.py  ← orders logic
    waiters_controller.py ← waiters logic
  database/
    connection.py         ← MongoDB connection
    menu_data.py          ← menu population
  entities/
    item.py               ← item management
    menu.py               ← menu entity
    order.py              ← order entity
    waiter.py             ← waiter entity
  routes/
    menu_routes.py        ← menu routes
    order_routes.py       ← order routes
    waiters_routes.py     ← waiter routes
  schema/
    delete_user_schema.py ← delete schemas
    post_user_schema.py   ← order creation schema
    put_user_schema.py    ← order update schema
    waiter_schema.py      ← waiter schemas
  utils/
    id_generator.py       ← ID generator
    validators.py         ← validations (CPF, email, phone)
```

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/RestauranteClass.git
cd RestauranteClass
```

**2. Create and activate the virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure the `.env` file**

Create a `.env` file at the project root based on `.env.example`:
```
MONGO_URL=mongodb+srv://your_user:your_password@your_cluster.mongodb.net/restaurant
```

> Never share your `.env` file. It is already listed in `.gitignore`.

---

## Running the Server

```bash
python -m uvicorn src.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`

---

## Documentation

After running the server, access the interactive documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## Available Routes

### Menu `/menu`

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/menu/` | Returns the full menu |
| `GET` | `/menu/category/?category=drink` | Filter by category |
| `GET` | `/menu/name/?name=Pizza Margherita` | Search by name |

**Available categories:** `main_course`, `starter`, `drink`, `dessert`

---

### Orders `/orders`

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/orders/` | Creates a new order |
| `GET` | `/orders/` | Gets order by table number |
| `GET` | `/orders/all/` | Returns all orders |
| `PUT` | `/orders/` | Updates an item in an order |
| `DELETE` | `/orders/` | Clears all orders from a table |
| `DELETE` | `/orders/item/` | Removes a specific item |

**Example — Create order (`POST /orders/`):**
```json
{
  "table_number": 1,
  "main_course": "Pizza Margherita",
  "drink": "Coca-Cola",
  "starter": "Salada Caesar"
}
```

**Example — Update item (`PUT /orders/`):**
```json
{
  "table_number": 1,
  "item_id": 1,
  "new_main_course": "Hamburguer",
  "new_drink": "Suco de Laranja",
  "new_starter": "Pao de Alho"
}
```

**Example — Delete table order (`DELETE /orders/`):**
```json
{
  "table_number": 1
}
```

**Example — Delete specific item (`DELETE /orders/item/`):**
```json
{
  "table_number": 1,
  "item_id": 1
}
```

---

### Waiters `/waiters`

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/waiters/` | Registers a waiter |
| `GET` | `/waiters/all/` | Lists all waiters |
| `GET` | `/waiters/?waiter_id=1` | Gets waiter by ID |
| `PUT` | `/waiters/` | Updates waiter data |
| `DELETE` | `/waiters/` | Removes a waiter |

**Example — Create waiter (`POST /waiters/`):**
```json
{
  "name": "Joao Silva",
  "cpf": "123.456.789-09",
  "wage": 1500.0,
  "email": "joao.silva@email.com",
  "phone_number": "(11) 99999-9999"
}
```

**Example — Update waiter (`PUT /waiters/`):**
```json
{
  "waiter_id": 1,
  "new_name": "Joao Santos",
  "new_wage": 2000.0
}
```
> Send only the fields you want to update. Fields not sent will remain unchanged.

**Example — Delete waiter (`DELETE /waiters/`):**
```json
{
  "waiter_id": 1
}
```

---

## Fixed Menu

The menu is automatically populated when the server starts.

| Item | Category | Price |
|------|----------|-------|
| Pizza Margherita | Main Course | R$ 39.90 |
| Hamburguer | Main Course | R$ 29.90 |
| Macarrao Bolonhesa | Main Course | R$ 34.90 |
| Salada Caesar | Starter | R$ 19.90 |
| Pao de Alho | Starter | R$ 12.90 |
| Coca-Cola | Drink | R$ 8.00 |
| Suco de Laranja | Drink | R$ 10.00 |
| Agua | Drink | R$ 5.00 |
| Pudim | Dessert | R$ 14.90 |
| Brownie | Dessert | R$ 16.90 |