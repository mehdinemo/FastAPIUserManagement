## .env

```
USER_MANAGEMENT_PROXY=socks5://127.0.0.1:8080
USER_MANAGEMENT_SECRET_KEY=
USER_MANAGEMENT_GOOGLE_OAUTH_CLIENT_ID=
USER_MANAGEMENT_GOOGLE_OAUTH_CLIENT_SECRET=
USER_MANAGEMENT_DB_NAME=
USER_MANAGEMENT_DB_USERNAME=
USER_MANAGEMENT_DB_PASSWORD=
```

## Generate Secret Key

To generate a secure random secret key for JWT:

1. Directly from the Ubuntu terminal:
   ```shell
   openssl rand -hex 32
   ```
2. In Python using the `secrets` module:
   ```python
   import secrets
   
   # Generate a 256-bit (32-byte) secret key
   secret_key = secrets.token_hex(32)
   print(f"Your secret key: {secret_key}")
   ```

## PostgreSQL

In PostgreSQL, managing databases, users, and tables involves using SQL commands within the PostgreSQL shell (`psql`).
Below are the most common commands used for these tasks:

### 1. **Database Management**

#### Create a New Database:

```sql
CREATE DATABASE dbname;
```

#### List All Databases:

```sql
\l
```

#### Connect to a Database:

```sql
\c dbname;
```

#### Drop a Database (delete):

```sql
DROP DATABASE dbname;
```

### 2. **User Management**

#### Create a New User:

```sql
CREATE USER username WITH PASSWORD 'password';
```

#### List All Users:

```sql
\du
```

#### Grant Privileges to a User:

- Full privileges on a specific database:
  ```sql
  GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
  ```
- For table-specific privileges:
  ```sql
  GRANT ALL PRIVILEGES ON TABLE tablename TO username;
  ```

#### Revoke Privileges:

```sql
REVOKE ALL PRIVILEGES ON DATABASE dbname FROM username;
```

#### Alter a User’s Password:

```sql
ALTER USER username WITH PASSWORD 'new_password';
```

#### Drop a User (delete):

```sql
DROP USER username;
```

### 3. **Table Management**

#### Create a Table:

```sql
CREATE TABLE tablename
(
    column1 datatype PRIMARY KEY,
    column2 datatype,
    column3 datatype
);
```

#### List All Tables:

```sql
\dt
```

#### Describe Table Structure:

```sql
\d tablename
```

#### Insert Data into a Table:

```sql
INSERT INTO tablename (column1, column2, column3)
VALUES (value1, value2, value3);
```

#### Select Data from a Table:

```sql
SELECT *
FROM tablename;
```

#### Update Data in a Table:

```sql
UPDATE tablename
SET column1 = value1
WHERE condition;
```

#### Delete Data from a Table:

```sql
DELETE
FROM tablename
WHERE condition;
```

#### Drop (Delete) a Table:

```sql
DROP TABLE tablename;
```

### 4. **Granting Permissions for Tables and Columns**

#### Grant Select Permissions:

```sql
GRANT SELECT ON tablename TO username;
```

#### Grant Insert Permissions:

```sql
GRANT INSERT ON tablename TO username;
```

#### Revoke Permissions:

```sql
REVOKE ALL PRIVILEGES ON tablename FROM username;
```

### 5. **Additional Useful Commands**

#### Check Connection Information:

```sql
\conninfo
```

#### Quit the PostgreSQL Prompt:

```sql
\q
```

These are the core commands to get started with PostgreSQL management.