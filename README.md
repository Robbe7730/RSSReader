# RSS reader that is yet to be named

## Development Setup

### 1. Follow the instructions to install [postgrest](http://postgrest.org/) (including postgresql)

### 2. Create a postgresql database `api` and initialize it with `postgrest.sql`

```bash
su postgres
cd postgrest
createdb api
psql < postgrest.sql
```

### 3. Start postgrest

```bash
postgrest postgrest/postgrest.conf
```

### 4. Find the backend on http://0.0.0.0:3000

