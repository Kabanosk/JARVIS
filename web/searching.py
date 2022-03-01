import webbrowser as web
from bs4 import BeautifulSoup

STARTING_URL = 'https://www.google.com/search?q='

def get_first_website(phrase):
    phrase_split = phrase.split()
    phrase_url = '+'.join(phrase_split)
    search_url = STARTING_URL + phrase_url
    web.open_new_tab(search_url)

