PYTHON_TEST_MIGRATIONS_PROJECT ?= python-test-migrations-project
PYTHON_TEST_MIGRATIONS_IMAGE_VERSION ?= 0.0.1
PYTHON_TEST_MIGRATIONS_IMAGE_NAME ?= python-test-migrations
PYTHON_TEST_DB_NAME ?= pythontestdb
PYTHON_TEST_DB_USERNAME ?= pythontestdb
PYTHON_TEST_DB_PASSWORD ?= pythontestdbpwd
PYTHON_TEST_DB_PORT ?= 5432
PYTHON_TEST_DB_HOST ?= python-test-db
PYTHON_TEST_PROXY_NETWORK ?= "proxy-network-python-test"

.PHONY: default
default:

.PHONY: build
build:
	docker build -t $(PYTHON_TEST_MIGRATIONS_IMAGE_NAME):$(PYTHON_TEST_MIGRATIONS_IMAGE_VERSION) -f Dockerfile .

.PHONY: run
run:
	if ! docker network inspect "proxy-network-python-test" >/dev/null 2>&1 ; then \
    docker network create "proxy-network-python-test" ; \
    fi
	sleep 1
	APP_IMAGE_VERSION=$(PYTHON_TEST_MIGRATIONS_IMAGE_VERSION) \
    APP_IMAGE_NAME=$(PYTHON_TEST_MIGRATIONS_IMAGE_NAME) \
    APP_PROXY_NETWORK=$(PYTHON_TEST_PROXY_NETWORK) \
    APP_DB_USERNAME=$(PYTHON_TEST_DB_USERNAME) \
    APP_DB_PASSWORD=$(PYTHON_TEST_DB_PASSWORD) \
    APP_DB_NAME=$(PYTHON_TEST_DB_NAME) \
    APP_DB_HOST=$(PYTHON_TEST_DB_HOST) \
    APP_DB_PORT=$(PYTHON_TEST_DB_PORT) \
    docker-compose -p $(PYTHON_TEST_MIGRATIONS_PROJECT) -f docker-compose.yaml up -d

.PHONY: down
down:
	if ! docker network inspect "proxy-network-python-test" >/dev/null 2>&1 ; then \
    docker network create "proxy-network-python-test" ; \
    fi
	sleep 1
	APP_IMAGE_VERSION=$(PYTHON_TEST_MIGRATIONS_IMAGE_VERSION) \
    APP_IMAGE_NAME=$(PYTHON_TEST_MIGRATIONS_IMAGE_NAME) \
    APP_PROXY_NETWORK=$(PYTHON_TEST_PROXY_NETWORK) \
    APP_DB_USERNAME=$(PYTHON_TEST_DB_USERNAME) \
    APP_DB_PASSWORD=$(PYTHON_TEST_DB_PASSWORD) \
    APP_DB_NAME=$(PYTHON_TEST_DB_NAME) \
    APP_DB_HOST=$(PYTHON_TEST_DB_HOST) \
    APP_DB_PORT=$(PYTHON_TEST_DB_PORT) \
	docker-compose -p $(PYTHON_TEST_MIGRATIONS_PROJECT) -f docker-compose.yaml down
