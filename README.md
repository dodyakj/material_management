```markdown
# Material Management Module for Odoo 14

This repository contains an Odoo 14 module for managing materials and suppliers. The module includes:
- CRUD operations for materials.
- Validation rules (e.g., material price must be ≥ 100).
- REST API for managing materials.
- Unit testing for all functionalities.

## Prerequisites
- Docker
- Docker Compose

## How to Run Using Docker Compose

### 1. Clone the Repository
```bash
git clone https://github.com/dodyakj/material_management.git
cd material_management
```

### 2. Set Up Configuration
Ensure the `odoo.conf` file is placed in the `config/` folder. Here is an example configuration:

**`config/odoo.conf`:**
```ini
[options]
addons_path = /mnt/custom-addons,/mnt/extra-addons
data_dir = /var/lib/odoo
admin_passwd = masukaja
dbfilter = tes
; csv_internal_sep = ,
; db_maxconn = 64
; db_name = False
; db_template = template1
; debug_mode = False
; email_from = False
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 60
limit_time_real = 120
; list_db = True
; log_db = False
; log_handler = [':INFO']
; log_level = info
; logfile = None
; longpolling_port = 8072
; max_cron_threads = 2
; osv_memory_age_limit = 1.0
; osv_memory_count_limit = False
; smtp_password = False
; smtp_port = 25
; smtp_server = localhost
; smtp_ssl = False
; smtp_user = False
; workers = 0
; xmlrpc = True
; xmlrpc_interface =
; xmlrpc_port = 8069
; xmlrpcs = True
; xmlrpcs_interface =
; xmlrpcs_port = 8071
```

### 3. Docker Compose Setup
The `docker-compose.yml` file defines the Odoo and PostgreSQL services.

**`docker-compose.yml`:**
```yaml
version: '3.1'

services:
  db:
    image: postgres:14 # we will use postgres:14 image from docker hub for database
    ports:
      - "127.0.0.1:5432:5432"
    environment:
      - POSTGRES_USER=odoo # Set value of postgres credential
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
      - PGDATA=/var/lib/postgresql/data
    volumes:
      - odoo-db-data:/var/lib/postgresql/data # set postgresql data persistence

  tes:
    container_name: tes
    image: odoo:14
    volumes:
      - ../addons:/mnt/custom-addons # Mount volume between host and container, host_dir:container_dir
      # - ../../odoo_e14/enterprise-14:/mnt/extra-addons # Mount volume between host and container, host_dir:container_dir
      - ../config:/etc/odoo/
      - odoo-tes-data:/var/lib/odoo
    ports:
      - "8014:8069" # this will create connection port between host and container, this means host_port:container_port
    depends_on:
      - db # set depends on postgresql db
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
    command: odoo --dev xml,qweb

volumes:
  odoo-tes-data:
  odoo-db-data:
```

### 4. Start the Services
Run the following command to start Odoo and PostgreSQL:
```bash
docker-compose up
```

### 5. Access Odoo
Once the services are running, access Odoo via your browser:
```
http://localhost:8014
```

- **Database Manager**: Create a new database.
- **Install Module**: Go to **Apps** → **Update Apps List** → Search for "Material Management" → Install the module.

### 6. Run Unit Tests
To run the unit tests, execute the following command:
```bash
docker-compose exec tes odoo -i material_management --test-enable --stop-after-init
```

## REST API Endpoints
The module provides the following REST API endpoints:
- **GET** `/api/materials` - List all materials (filter by `material_type` using query parameter).
- **POST** `/api/materials` - Create a new material.
- **PUT** `/api/materials/<id>` - Update a material.
- **DELETE** `/api/materials/<id>` - Delete a material.

Example API request:
```bash
curl -X POST http://localhost:8014/api/materials -H "Content-Type: application/json" -d '{
  "material_code": "TEST001",
  "material_name": "Test Material",
  "material_type": "fabric",
  "material_price": 150,
  "supplier_id": 1
}'
```

## Unit Testing
Unit tests are located in the `tests/` folder. You can run them using the command provided in step 6.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

---
