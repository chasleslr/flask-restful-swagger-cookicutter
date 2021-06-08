.PHONY = build push dev

NAME   := {{ cookiecutter.project_slug }}
TAG    := $$(git describe)
IMG    := ${NAME}:${TAG}
LATEST := ${NAME}:latest

deploy: build push

build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}

push:
	@docker push ${NAME}

dev:
	pip install pipenv
	pipenv install --dev
