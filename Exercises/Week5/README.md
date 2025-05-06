# Database and API Project

This project consists of a FastAPI-based REST API and SQL queries for database operations. The project includes various SQL queries for analyzing sales data, customer behavior, and order statistics.

## Project Structure

```
.
├── api/                    # API application directory
│   ├── app/               # Application code
│   ├── .env               # Environment variables
│   ├── Dockerfile         # Docker configuration
│   └── requirements.txt   # Python dependencies
├── *.sql                  # SQL query files
└── .gitignore            # Git ignore configuration
```

## SQL Queries

The project includes several SQL query files for different analyses:

- `averageOrderByCountry.sql`: Calculates average order values by country
- `frequentBuyers.sql`: Identifies customers with frequent purchases
- `monthlySalesShippedOrDelivered.sql`: Analyzes monthly sales statistics
- `productsNeverOrdered.sql`: Lists products that have never been ordered
- `setup.sql`: Database setup and schema
- `topCustomersBySpend.sql`: Identifies top customers by spending

## API Setup and Running

### Prerequisites

- Python 3.8 or higher
- MySQL database
- Docker (optional)

### Environment Setup

1. Create a `.env` file in the `api` directory with the following variables:
   ```
   DB_HOST=your_database_host
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_NAME=your_database_name
   ```

2. Install dependencies:
   ```bash
   cd api
   pip install -r requirements.txt
   ```

### Running the API

#### Local Development

1. Navigate to the api directory:
   ```bash
   cd api
   ```

2. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

#### Using Docker

1. Build the Docker image:
   ```bash
   cd api
   docker build -t api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 api
   ```

## API Documentation

Once the API is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database Setup

1. Ensure MySQL is running
2. Run the setup script:
   ```bash
   mysql -u your_username -p < setup.sql
   ```

## Notes

- The `.env` file is gitignored for security reasons. Make sure to create it with your database credentials.
- All SQL queries are provided as separate files for easy reference and execution.
- The API is built using FastAPI, providing automatic OpenAPI documentation and high performance. 