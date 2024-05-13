import argparse
import os
import concurrent.futures
from ImageScraper import ImageScraper  # Assuming ImageScraper is defined in image_scraper.py
from patch import webdriver_executable


def worker_thread(search_key, webdriver_path, image_path, number_of_images, headless, min_resolution, max_resolution,
                  max_missed, keep_filenames):
    image_scraper = ImageScraper(
        webdriver_path,
        image_path,
        search_key,
        number_of_images,
        headless,
        min_resolution,
        max_resolution,
        max_missed)
    image_scraper.find_image_urls()
    # image_scraper.save_image(image_urls, keep_filenames)

    # Release resources
    del image_scraper


def parse_arguments():
    parser = argparse.ArgumentParser(description='Image Scraper Parameters')
    parser.add_argument('search_key', type=str, help='Search key for images')
    parser.add_argument('-n', '--number_of_images', type=int, default=50, help='Desired number of images')
    parser.add_argument('-hd', '--headless', type=bool, default=True, help='Headless mode (True/False)')
    parser.add_argument('-min', '--min_resolution', type=int, nargs=2, default=[512, 512],
                        help='Minimum desired image resolution')
    parser.add_argument('-max', '--max_resolution', type=int, nargs=2, default=[9999, 9999],
                        help='Maximum desired image resolution')
    parser.add_argument('-mm', '--max_missed', type=int, default=10000, help='Max number of failed images before exit')
    parser.add_argument('-kfn', '--keep_filenames', type=bool, default=True, help='Keep original URL image filenames')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()

    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    search_keys = [args.search_key]

    # Run each search_key in a separate thread
    # Automatically waits for all threads to finish
    # Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(search_keys)) as executor:
        executor.map(worker_thread, search_keys, [webdriver_path] * len(search_keys), [image_path] * len(search_keys),
                     [args.number_of_images] * len(search_keys), [args.headless] * len(search_keys),
                     [tuple(args.min_resolution)] * len(search_keys), [tuple(args.max_resolution)] * len(search_keys),
                     [args.max_missed] * len(search_keys), [args.keep_filenames] * len(search_keys))
