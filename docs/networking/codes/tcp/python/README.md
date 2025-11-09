# TCP Server Example

## Setup

1. **Create a virtual environment:**
   ```sh
   make venv
   ```

2. **Activate the virtual environment:**
   ```sh
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   make install
   ```

## Running the Server

With the virtual environment activated, run:
```sh
make server
```

## Running the Client

With the virtual environment activated, run:
```sh
make client
```


## Clean Up

To remove the virtual environment:
```sh
make clean
```

> **Note:**  
> This example uses only Python's standard library, so `requirements.txt` is empty.
