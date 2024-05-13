# Google Image Scraper
A library created to scrape Google Images.<br>
This project was created with the help [ofohyicong/Google-Image-Scraper](https://github.com/ohyicong/Google-Image-Scraper), thanks for it I updated the scraper according to my needs.

If you are looking for other image scrapers, JJLimmm has created image scrapers for Gettyimages, Shutterstock, and Bing. <br>
Visit their repo here: https://github.com/JJLimmm/Website-Image-Scraper

## Pre-requisites:
1. Google Chrome
2. Python3 packages (Pillow, Selenium, Requests)

## Setup and Usage:
1. Open command prompt
2. Clone this repository or download
    ```
    git clone https://github.com/feceugur/GoogleImageScraper
    ```
3. Install Dependencies
    ```
    pip install -r requirements.txt
    ```
4. Run the program with your desired parameters 
    ```
    python main_f.py "SEACRH-KEY" -n NUMBER-OF-IMAGES

    SEACRH-KEY = Search key for images
    -n = Desired number of images (default=50)
    -hd = Headless mode (True/False) (default=True)
    -min = Minimum desired image resolution (default=[512, 512])
    -max = Maximum desired image resolution (default=[9999, 9999])
    -mm = Max number of failed images before exit (default=10000)
    -kfn = Keep original URL image filenames (default=True)

    ```


## Youtube Video of the ofohyicong/Google-Image-Scraper's project:
[![IMAGE ALT TEXT](https://github.com/ohyicong/Google-Image-Scraper/blob/master/youtube_thumbnail.PNG)](https://youtu.be/QZn_ZxpsIw4 "Google Image Scraper")

