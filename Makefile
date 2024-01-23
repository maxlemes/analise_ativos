.PHONY: install format lint test sec

install:
	@poetry install
format:
	@isort .
	@blue .
lint:
	@isort . --check
	@blue . --check
	@prospector --with-tool pep257 --doc-warning
test:
	@pytest -v
sec:
	@pip-audit