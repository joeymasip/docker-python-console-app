import requests
from bs4 import BeautifulSoup


class BlogPost:
    title = None
    first_sentence = None

    def __init__(self, title, first_sentence):
        self.title = title
        self.first_sentence = first_sentence

    def __str__(self):
        return str(self.title) + '\n' + str(self.first_sentence)


def scrape(url):
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, features="html.parser")
        # print(soup.prettify())

        for article in soup.find_all('article', attrs={'class': 'post'}):
            title = article.find('h2', attrs={'class': 'entry-title'}).string
            first_sentence = article.find('div', attrs={'class': 'entry-content'}).find('p').string

            blog_post = BlogPost(
                title=title,
                first_sentence=first_sentence
            )
            print(blog_post)
            print('------------------------------')
    else:
        print('Whoops! Something went wrong!')


scrape("https://blog.joeymasip.com/")
