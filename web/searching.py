import webbrowser as web

STARTING_URL = 'https://www.google.com/search?q='

def get_first_website(phrase):
    phrase_split = phrase.split()
    phrase_url = '+'.join(phrase_split)
    search_url = STARTING_URL + phrase_url
    web.open_new_tab(search_url)

get_first_website('newer gonna give you up')
