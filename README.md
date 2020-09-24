# Config

You'll need a `.env` file in your project root.

**Populate these variables with your local config.**

```
mysql_port
mysql_user
mysql_pass
mysql_db
```


# Running

- If you're not already running the docker services: Start up docker services: `docker-compose up -d`
- From your project root exec: `python -m src.app`

# Adminer

Adminer offers a simple GUI to administer your MySQL DBs running on Docker. Navigate to `localhost:8080` to access it.
