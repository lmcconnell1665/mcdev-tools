
# source ~/.mcdev-tools/bin/activate
setup:
	python3 -m venv ~/.mcdev-tools

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 setup.py pytest

build:
	python3 setup.py bdist_wheel
