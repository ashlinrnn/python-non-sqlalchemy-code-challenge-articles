class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            return
        if type(value) is not str:
            return
        if len(value) < 5 or len(value) > 50:
            return
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            return
        if type(value) is not str:
            return
        if len(value) == 0:
            return
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        return list(set(mag.category for mag in mags)) if mags else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            return
        if len(value) < 2 or len(value) > 16:
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) is not str:
            return
        if len(value) == 0:
            return
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [a for a in set(authors) if authors.count(a) > 2]
        return result if result else None
