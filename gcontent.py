from os import path
import ujson
import requests
from bs4 import BeautifulSoup


PROJECT_ROOT = path.abspath(path.dirname(__file__))


class GContent(object):
    _name_file = path.join(PROJECT_ROOT, "content.json")

    def __new__(cls, *args, **kwags):
        cls.load_content()
        return super(GContent, cls).__new__(cls, *args, **kwags)

    @classmethod
    def load_content(cls):
        with open(cls._name_file) as content:
            cls._content = ujson.load(content)
            return cls._content
        return {}

    def run(self):
        """
            Start get content.
        """
        self.build_blog_content()

    def build_blog_content(self):
        """
            Define five principal blog posts.
        """
        resource = requests.get("http://blog.henriquelopes.com.br")
        html = BeautifulSoup(resource.content, 'html.parser')
        if resource.status_code == 200:
            contents = {"posts": list()}

            for article in html.findAll("article"):
                contents["posts"].append({
                    "label": article.find("a").text,
                    "url": article.find("a").get("href")
                })
            self.content = contents
            return True
        return False

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        index = content.keys()[0]
        self._content[index]['content'] = content[index]

    def salve(self):
        self.run()
        with open(self._name_file, "w") as source:
            source.write(ujson.dumps(self.content, ensure_ascii=False, indent=2))


def get_content():
    return GContent.load_content()


if __name__ == "__main__":
    gcontent = GContent()
    gcontent.salve()
