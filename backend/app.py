import sys
import os
import multiprocessing
from main import app, run_gui
import uvicorn
import logging
import time

def run_server():
    try:
        uvicorn.run(app, host="127.0.0.1", port=8080, log_level="error")
    except Exception as e:
        logging.error(f"Server error: {e}")

def main():
    # Set up logging
    logging.basicConfig(level=logging.ERROR)

    # Start the server in a separate process
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    # Give the server a moment to start
    time.sleep(2)

    try:
        # Start the GUI in the main process
        run_gui()
    except Exception as e:
        logging.error(f"GUI error: {e}")
    finally:
        # Clean up when GUI closes
        server_process.terminate()
        server_process.join()

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Required for PyInstaller
    main() 