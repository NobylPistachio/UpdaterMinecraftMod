


#url = "https://www.curseforge.com/minecraft-bedrock/addons/serp-pokemon-addon"

# Connect to the website
    # Using selenium to connect to the website
    # Get the download links
# Download Files
# Put files into folder
# Open Aternos Server
# Remove Olds Files 
# Add New Files

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Set your download directory
download_dir = os.path.abspath("downloads")

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True
})
chrome_options.add_argument("--start-maximized")

# Start the driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the initial site
driver.get("https://www.curseforge.com/minecraft-bedrock/addons/serp-pokemon-addon")

print("Browser is ready. Navigate manually to your download link.")
print(f"Files will be saved to: {download_dir}")

# Wait for user to finish interaction
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped by user")

# Optional: Close browser
driver.quit()


