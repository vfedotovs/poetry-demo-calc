.DEFAULT_GOAL := help

help:  ## 💬 This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup-venv: ## Setup virtual environment
	poetry env use python3.9 && \
	poetry shell && \
	poetry install

test: ##  Unit tests for app
	pytest -vv

cov: ##  Tests coverage for app
	pytest --cov poetry_demo_calc/

docs: ##  Generate code documentation with pdoc
	pdoc poetry_demo_calc/

lint: ##  Lint code with pylint
	pylint poetry_demo_calc/

build: ##  Build docker container
	docker build -t vfedotovsdocker/app:latest .	

run: ##  Run docker container locally
	docker run -p 5000:5000 vfedotovsdocker/app

push: ##  Push container to dockerhub
	docker push vfedotovsdocker/app

clean: ##  clean test files
	rm -rf .coverage 
	rm -rf .pytest_cache
	rm -rf tests/__pycache__
	rm -rf poetry_demo_calc/__pycache__
