.PHONY: help up stop test lint format wip

help:
	@echo "Available commands:"
	@echo "  up     - Build and start the services"
	@echo "  stop   - Stop the services"
	@echo "  test   - Run tests"
	@echo "  lint   - Lint the code"
	@echo "  format - Format the code"
	@echo "  wip    - Amend the last commit with a 'wip' message"

up:
	docker-compose up -d --build

stop:
	docker-compose down

test:
	docker-compose exec api pytest

lint:
	docker-compose exec api ruff check . --fix

format:
	docker-compose exec api ruff format .

wip:
	git add .
	git commit --amend -m "$$(git log -1 --pretty=%B)"

health:
	@echo "Checking health of http://localhost:8000/api/health..."
	@until curl -s -f -o /dev/null "http://localhost:8000/api/health"; do \
		echo "Waiting for service..."; \
		sleep 2; \
	done
	@echo "Service is healthy!"

