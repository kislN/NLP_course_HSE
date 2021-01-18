from tqdm import tqdm
import json

from Lab_1_parsing.parsing_utils import *


cats_dict = {
    '/finance': 'Экономика',
    '/hitech': 'Технологии',
    '/sport': 'Спорт',
    '/cinema': 'Культура',
    '/realty': 'Недвижимость',
}
url_base = 'https://www.newsru.com'


links_dict = {}
for c in tqdm(cats_dict):
    links_dict[c] = article_links(url_base, c)


catalog_list = []
for c in links_dict:
    print(links_dict[c])
    for link in tqdm(links_dict[c]):
        catalog_list.append(article_dict(url_base + link, cats_dict[c]))


if None in catalog_list:
    catalog_list = [x for x in catalog_list if x is not None]

print(f'Length of the catalog is {len(catalog_list)}')


corpora_dict = {
    'catalog': catalog_list,
}

with open("corpora.json", "w") as write_file:
    json.dump(corpora_dict, write_file, ensure_ascii=False)
