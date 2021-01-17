import requests
from bs4 import BeautifulSoup


def article_links(url_base, url):
    art_links = []
    while len(art_links) < 1000:
        r = requests.get(url_base + url).text
        soup = BeautifulSoup(r, 'html.parser')
        art_links += [x.get('href') for x in soup.find_all('a', class_='index-news-title')]
        url = soup.find('a', class_='arch-arrows-link-l').get('href')
    return art_links


def article_dict(url, cat):
    try:
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')

        title = soup.find('h1', class_='article-title').get_text()

        article = soup.find('div', class_='article-text')
        article_p = [x.text for x in article.find_all('p')]
        article_text = ' '.join(article_p)
    except:
        return

    try:
        tags = soup.find('div', class_='article-tags-list dossieros')
        tags_list = [x.get_text() for x in tags.find_all('a')[1:]]
        tags_text = ', '.join(tags_list)
    except:
        tags_text = 0

    art_dict = {
        'article_id': url,
        'title': title,
        'category': cat,
        'tags': tags_text,
        'text': article_text
    }

    return art_dict
