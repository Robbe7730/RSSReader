start:
	postgrest postgrest/postgrest.conf &
	cd frontend/api && \
		curl localhost:3000 > openapi.json && \
		openapi-generator generate -i openapi.json -g typescript-fetch --additional-properties=typescriptThreePlus=true
	cd frontend && \
		yarn install && \
		yarn start

db:
	sudo -u postgres bash -c 'createdb api; psql < postgrest/postgrest.sql'
