PYTHON := $(if $(shell bash -c "command -v python3.10"), python3.10, python3)
PIP := $(if $(shell bash -c "command -v pip"), pip, pip3)

install-pip-model:
	$(PIP) install --ignore-installed  --disable-pip-version-check -e .

gen:
	$(PYTHON) generate.py
