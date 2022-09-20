import logging
import threading
import time
import concurrent.futures
import requests

res = requests.get('https://brunoyam.com')

print(res.text)
 
start = time.time()


def get_html(link):
    link = 'https://brunoyam.com'

    time.sleep(1)
    logging.info("Thread %s", link)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


for i in range(5):
    get_html(i + 1)

print(time.time() - start)


start = time.time()
def get_html(link):

    time.sleep(1)
    logging.info("Thread %s", link)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_html, range(5))


print(time.time() - start)
