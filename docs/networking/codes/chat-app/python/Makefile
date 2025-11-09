VENV?=.venv

.PHONY: venv install server client clean send clients
# Makefile for setting up a Python virtual environment and running a TCP server/client

venv:
	python3 -m venv $(VENV)
	@echo "Virtual environment created at $(VENV)"

install:
	. $(VENV)/bin/activate && pip install -r requirements.txt

server:
	. $(VENV)/bin/activate && python server.py	--server

clients:
	. $(VENV)/bin/activate && python server.py --clients

send:
	. $(VENV)/bin/activate && python server.py --send-single client_id="$(client_id)" message="$(message)"

sendbox:
	. $(VENV)/bin/activate && python server.py --sendbox

client:
	. $(VENV)/bin/activate && python client.py



clean:
	rm -rf $(VENV)
	rm -f *.pyc
	rm -f __pycache__/*
	rm -rf __pycache__
	rm -f *.log
	rm -f *.db
	rm -f *.sqlite3
