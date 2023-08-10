import requests
from bs4 import BeautifulSoup


#The application that fetches the links of the top 30 news articles from Hacker News site.

target_url = "https://news.ycombinator.com"
key_word = "https://"
top30_news = list()
counter = 1


def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawl(url):
    links = make_request(url)

    for link in links.find_all("a"):
        found_link = link.get("href")

        if found_link:

#add links starting with https and do not add the link of main website and also do not add the same link more than one

            if (key_word in found_link and found_link not in top30_news) and (target_url not in found_link):
                global counter
                top30_news.append(found_link)
                print(f"{counter}.\tnew ---> {found_link}")
                counter += 1
                if counter == 31:
                    break


crawl(target_url)