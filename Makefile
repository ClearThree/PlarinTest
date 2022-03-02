# Makefile
build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down -v

logs:
	docker-compose logs -f

rebuild:
	make build
	make up

format:
	isort app
	black app
	pflake8 app

tests:
	docker exec plarin-api "pytest"
