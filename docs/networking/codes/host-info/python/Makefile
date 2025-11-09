VENV?=.venv

.PHONY: venv install host_info clean
# Makefile for setting up a Python virtual environment and running a TCP server/client

venv:
	python3 -m venv $(VENV)
	@echo "Virtual environment created at $(VENV)"

install:
	. $(VENV)/bin/activate && pip install -r requirements.txt

host_info self:
	. $(VENV)/bin/activate && python host_info.py --self

host_info internet:
	. $(VENV)/bin/activate && python host_info.py --internet


clean:
	rm -rf $(VENV)
	rm -f *.pyc
	rm -f __pycache__/*
	rm -rf __pycache__
	rm -f *.log
	rm -f *.db
	rm -f *.sqlite3
