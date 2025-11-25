class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    #  TITLE 
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title") and self._title is not None:
            # immutable after first assignment
            return

        if not isinstance(value, str):
            return
        if not (5 <= len(value) <= 50):
            return

        self._title = value

    #  AUTHOR 
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return
        self._author = value

    #  MAGAZINE 
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    #  NAME 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name") and self._name is not None:
            # immutable
            return
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._name = value

    #  ARTICLES 
    def articles(self):
        return [article for article in Article.all if article.author == self]

    #  MAGAZINES 
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    #  ADD ARTICLE 
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            return
        if not isinstance(title, str):
            return
        return Article(self, magazine, title)

    #  TOPIC AREAS 
    def topic_areas(self):
        categories = [article.magazine.category for article in self.articles()]
        return list(set(categories)) if categories else None  


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name
        self.category = category

    #  NAME 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if not (2 <= len(value) <= 16):
            return
        self._name = value

    #  CATEGORY 
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value

    #  ARTICLES 
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    #  CONTRIBUTORS 
    def contributors(self):
        return list({article.author for article in self.articles()})

    #  ARTICLE TITLES 
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None   # <-- FIXED

    # CONTRIBUTING AUTHORS (MORE THAN 2 ARTICLES)
    def contributing_authors(self):
        authors = self.contributors()
        result = [
            author for author in authors
            if len([a for a in self.articles() if a.author == author]) > 2
        ]
        return result if result else None
