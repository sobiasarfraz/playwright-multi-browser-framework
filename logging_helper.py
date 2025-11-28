from datetime import datetime
import os
import logging

def setup_logging():
    os.makedirs("Logs",exist_ok=True)  #make logs folder,if not exist
    filename = f"Logs/log_{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

