import requests
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree

res = requests.get('https://www.foxnews.com/')
# res = requests.get('https://www.cnn.com/')

tree = parse_html_bytes(res.content, res.headers.get('content-type'))

links = set(find_links_tree(tree))
links
