import requests
from bs4 import BeautifulSoup
import threading

def scrape_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print("Scraped page:", url)
    return soup

def main():
    urls = ["https://www.example1.com", "https://www.example2.com", "https://www.example3.com"]
    threads = []
    for url in urls:
        t = threading.Thread(target=scrape_page, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()