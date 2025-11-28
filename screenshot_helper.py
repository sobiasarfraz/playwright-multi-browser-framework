import os
from datetime import datetime

os.makedirs("screenshot",  exist_ok=True)
def take_screenshot(page, name= "screenshot"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"screenshot/{name}_{timestamp}.png"
    page.screenshot(path=file_path)
    return file_path
