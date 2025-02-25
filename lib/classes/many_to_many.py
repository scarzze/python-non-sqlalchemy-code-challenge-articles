class Article:
    # Use 'all' as the single source of truth for all articles
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise ValueError("Author and Magazine must be instances of Author and Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        # Title is immutable; ignore any attempts to change it.
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        # Else: ignore invalid assignment

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        # Else: ignore invalid assignment


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Author name is immutable; ignore changes.
        pass

    def articles(self):
        """Return a list of all articles this author has written."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return a unique list of magazines for which the author has contributed."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Creates and returns a new Article instance associated with this author."""
        if not isinstance(magazine, Magazine):
            raise ValueError("Expected a Magazine instance.")
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns a unique list of magazine categories this author has contributed to.
        Returns None if the author has no articles."""
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))


class Magazine:
    instances = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine.instances.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Instead of raising errors, we ignore invalid assignments.
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name
        # Otherwise, do nothing.

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # Otherwise, ignore the invalid assignment.

    def articles(self):
        """Return a list of all articles published in this magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return a unique list of authors who have contributed to this magazine."""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """Return a list of titles of all articles written for this magazine.
        Returns None if there are no articles."""
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        """Return a list of authors who have written more than 2 articles for this magazine.
        Returns None if no such authors exist."""
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        contributing = [author for author, count in author_count.items() if count > 2]
        return contributing if contributing else None

    @classmethod
    def top_publisher(cls):
        """Return the magazine that has published the most articles, or None if no magazines exist."""
        if not cls.instances:
            return None
        return max(cls.instances, key=lambda m: len(m.articles()))
