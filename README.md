# Magazine Domain - Python Code Challenge
This project simulates a Magazine domain with classes for Author, Magazine, and Article. The relationships between these classes represent a real-world scenario where an author writes articles for various magazines, and each magazine contains multiple articles by different authors. The solution implements object-oriented principles, including object relationships, aggregation, and data integrity constraints.

# Table of Contents
Overview
Installation
Classes
Author
Magazine
Article
Methods
Author Methods
Magazine Methods
Article Methods
Testing
Usage Example
Contributing
License
Overview
# The system consists of three primary classes:

Author: Represents an author who can write articles for different magazines.
Magazine: Represents a magazine that publishes articles.
Article: Represents a single article written by an author for a magazine.
The relationships between these classes are as follows:

An Author can write many Articles.
A Magazine can have many Articles.
An Article belongs to one Author and one Magazine.
An Author can contribute to multiple Magazines, and a Magazine can have multiple Authors.
Installation
Follow these steps to set up the project:

Clone the repository: Clone this repository to your local machine using Git:

bash
Copy
git clone https://github.com/your-username/magazine-domain.git
cd magazine-domain
Set up the virtual environment: Install pipenv if it's not already installed. Follow these instructions for Fedora or other systems:

bash
Copy
sudo dnf install python3-pip  # Fedora: Install pip if it's missing
python3 -m pip install --user pipenv  # Install pipenv
Install dependencies: Once inside the project directory, run the following command to install the project dependencies using pipenv:

bash
Copy
pipenv install
Activate the virtual environment: Activate the virtual environment with the following command:

bash
Copy
pipenv shell
Classes
Author
The Author class represents an individual author in the system. An author can write multiple articles and contribute to multiple magazines.

Attributes:
name (str): The author's name. Must be a non-empty string.
articles (list): A list that holds all articles written by the author.
Methods:
add_article(magazine, title): Adds an article written by the author to a specific magazine.
articles(): Returns a list of articles the author has written.
magazines(): Returns a list of unique magazines the author has contributed to.
topic_areas(): Returns a list of unique categories of magazines the author has contributed to.
Magazine
The Magazine class represents a magazine that publishes articles from various authors.

Attributes:
name (str): The magazine's name. Must be between 2 and 16 characters.
category (str): The category/genre of the magazine (e.g., "Technology", "Health").
articles (list): A list of articles published in the magazine.
Methods:
article_titles(): Returns a list of titles of all articles in the magazine.
contributors(): Returns a list of unique authors who have written for the magazine.
contributing_authors(): Returns a list of authors who have written more than 2 articles for the magazine.
top_publisher(): A class method that returns the magazine with the most articles.
Article
The Article class represents an article written by an author and published in a magazine.

Attributes:
author (Author): The author of the article.
magazine (Magazine): The magazine where the article is published.
title (str): The title of the article.
Methods:
title: Returns the title of the article.
author: Returns the author of the article.
magazine: Returns the magazine the article is published in.
Methods
Author Methods
add_article(magazine, title): Creates a new Article instance and associates it with the author and the provided magazine.

articles(): Returns a list of all articles written by the author.

magazines(): Returns a unique list of magazines the author has contributed to.

topic_areas(): Returns a list of unique categories (topics) of magazines the author has written for.

Magazine Methods
article_titles(): Returns a list of the titles of all articles published in the magazine.

contributors(): Returns a unique list of authors who have written for this magazine.

contributing_authors(): Returns a list of authors who have written more than 2 articles for this magazine.

top_publisher(): Class method that returns the magazine with the most articles.

Article Methods
title: Returns the title of the article.

author: Returns the author of the article.

magazine: Returns the magazine where the article was published.

Testing
This project comes with built-in tests that verify the functionality of the methods. To run the tests:

Ensure you're in the virtual environment:

bash
Copy
pipenv shell
Run the tests using pytest:

bash
Copy
pytest test.py
pytest will automatically discover and run the test cases, providing feedback on whether everything is working as expected.

Usage Example
Here is an example of how to use the classes:

python
Copy
# Import the classes
from author import Author
from magazine import Magazine
from article import Article

# Create authors
author1 = Author("John Doe")
author2 = Author("Jane Smith")

# Create magazines
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

# Add articles to authors and magazines
author1.add_article(magazine1, "The Future of AI")
author2.add_article(magazine1, "Tech Trends 2025")
author1.add_article(magazine2, "Staying Fit in a Digital World")

# Check the author's contributions
print(author1.articles())  # List of articles by John Doe
print(author2.magazines())  # List of magazines Jane Smith contributed to

# Check the magazine's contributors
print(magazine1.contributors())  # List of authors who wrote for Tech Today
Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Please ensure that your code is well-tested and follows Python's PEP 8 style guide.

License
This project is licensed under the MIT License - see the LICENSE file for details.