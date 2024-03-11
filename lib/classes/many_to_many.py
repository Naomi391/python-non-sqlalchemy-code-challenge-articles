class Article:
    all = []  

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)  
        Article.all.append(self)  

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        return self.title
        raise AttributeError("Title is immutable")


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name

    def articles(self):
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        articles = Article(self, magazine, title)
        return articles

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    def contributing_authors(self):
        return [authors for authors in Author.all if len(authors.articles()) > 0]


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @name.setter
    def name(self, new_names):
        if isinstance(new_names, str):
            if 2 <= len(new_names) <= 16:
                self._name = new_names
        return self._name

    @category.setter
    def category(self, new_categories):
        if isinstance(new_categories, str):
            if len(new_categories) > 0:
                self._category = new_categories
        return self._category

    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = {}
        for articles in self.articles():
            if articles.author in authors:
                authors[articles.author] += 1
            else:
                authors[articles.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None