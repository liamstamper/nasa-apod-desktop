import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import subprocess

load_dotenv()

def main():
    # DEFAULT SAVE PATH
    save_dir = os.path.expanduser("~/desktop/nasa-potd")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY environment variable not set. Access https://api.nasa.gov/ and create your env.")

    # fetch image
    date = datetime.now()
    date_str = date.strftime('%Y-%m-%d')
    url, title = get_image(api_key, date_str)

    # download
    image_path = os.path.join(save_dir, f"APOD_{date_str}.jpg")
    download_image(url, image_path)

    # Set the wallpaper on Mac
    set_wallpaper(image_path)

# Get URL
def get_image(api_key, date_str):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date_str}"
    response = requests.get(url)
    data = response.json()
    while 'url' not in data or 'media_type' not in data or data['media_type'] != 'image':
        date = datetime.strptime(date_str, '%Y-%m-%d') - timedelta(1)
        date_str = date.strftime('%Y-%m-%d')
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date_str}"
        response = requests.get(url)
        data = response.json()
    return data['url'], data['title']

# Download the image
def download_image(url, image_path):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to download the image.")
    
    with open(image_path, 'wb') as file:
        file.write(response.content)

# Set the wallpaper on Mac
def set_wallpaper(image_path):
    script = f'tell application "System Events" to set picture of every desktop to POSIX file "{image_path}"'
    try:
        subprocess.run(["osascript", "-e", script], check=True)
        # Refresh the Dock
        subprocess.run(["killall", "Dock"])
        print("Desktop wallpaper changed successfully!")
    except subprocess.CalledProcessError:
        print("Error: Desktop wallpaper could not be changed.")

if __name__ == "__main__":
    main()
