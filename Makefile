init:
ifeq ($(TRAVIS), true)
		pip install pipenv
		pipenv install --dev
		pip install .
		touch tests/__init__.py
else
		pipenv install --dev
		pre-commit install
endif

test:
	pytest -rpsf --cov-report term-missing --cov-report xml --cov=mass_replace tests/

lint:
ifeq ($(TRAVIS_PYTHON_VERSION), 2.7)
		echo "Skip linting for Python2.7"
else
		prospector --output-format grouped
endif

format:
	black .

check_format:
ifeq ($(TRAVIS_PYTHON_VERSION), 3.7)
		black . --check
else
		echo "Only check format on Python3.7"
endif

pre:
	pre-commit run --all-files
