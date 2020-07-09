# RSS reader that is yet to be named

## Development setup (with make)

```bash
make db # If the db needs to be created
make
```

## Manual Setup

### Postgrest

#### 1. Follow the instructions to install [postgrest](http://postgrest.org/) (including postgresql)

#### 2. Create a postgresql database `api` and initialize it with `postgrest.sql`

```bash
su postgres
cd postgrest
createdb api
psql < postgrest.sql
```

#### 3. Start postgrest

```bash
postgrest postgrest/postgrest.conf
```

#### 4. Find the backend on http://0.0.0.0:3000

### Frontend

#### 1. Create the API from Progrest and openapi-generator

```bash
cd frontend/api
curl localhost:3000 > openapi.json
openapi-generator generate -i openapi.json -g typescript-fetch --additional-properties=typescriptThreePlus=true
```

#### 2. Install & run the frontend

```bash
cd frontend/
yarn install
yarn start
```
