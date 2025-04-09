build:
	docker-compose build

init:
	docker-compose run --rm pokus_pipeline init

validate:
	docker-compose run --rm pokus_pipeline validate

bash:
	docker-compose run --rm pokus_pipeline bash

down:
	docker-compose down
