# NASA Astronomy Picture of the Day Wallpaper

A Python script that automatically sets NASA's Astronomy Picture of the Day (APOD) as your Mac desktop wallpaper. It fetches the latest image using NASA's APOD API, downloads it, and updates your Mac desktop background daily. 

Note: On days when the astronomy picture of the day is a video the previous day's photo is used

### Setup:

1. Clone the repo
   
   ```bash
   https://github.com/liamstamper/nasa-apod-desktop.git
   ```
2. Request a free API key from [https://api.nasa.gov/](https://api.nasa.gov/)
3. Create an .env like the following
   ```bash
    API_KEY = "Your key"
   ```
4. (Optional) Change the folder path that saves the images. Defaults to dekstop, creating a folder named nasa-potd
5. Use cron to automate the script. Run the following in your terminal to open your crontab editor:

   ```bash
     env EDITOR=nano crontab -e
   ```
   I then used this to run the script daily at midnight:
   ```bash
     0 0 * * *  /full/path/to/script.py
   ```
   
   ``ctr-O`` to save and ``crt-x`` to exit.
   
   (The time is formated as the following: ``[minute: 0-59] [hour: 0-23] [day: 1-31] [months: 1-12] [weekday: 0-6]``)
   
   To view your scheduled events you can type `` crontab -l``
   
   
  
