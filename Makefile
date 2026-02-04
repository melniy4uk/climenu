.PHONY: fmt lint type test check

fmt:
	python -m ruff format .

lint:
	python -m ruff check . --fix
	python -m ruff check .

type:
	python -m pyright

test:
	python -m pytest

check: fmt lint type test
