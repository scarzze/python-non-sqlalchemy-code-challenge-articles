#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) Let's debug :vibing_potato:")

    # Create sample authors
    author1 = Author("Alice")
    author2 = Author("Bob")

    # Create sample magazines
    magazine1 = Magazine("TechTime", "Technology")
    magazine2 = Magazine("HealthBeat", "Health")

    # Create articles
    article1 = Article(author1, magazine1, "How to code in Python")
    article2 = Article(author1, magazine2, "The future of healthcare")
    article3 = Article(author2, magazine1, "Latest gadgets review")

    # --- Proof 1: Check articles per author ---
    print("\n=== Author1 Articles ===")
    for art in author1.articles():
        print(f"Title: {art.title}, Magazine: {art.magazine.name}")

    print("\n=== Author2 Articles ===")
    for art in author2.articles():
        print(f"Title: {art.title}, Magazine: {art.magazine.name}")

    # --- Proof 2: Check unique magazines for an author ---
    print("\n=== Author1 Magazines ===")
    for mag in author1.magazines():
        print(f"Magazine Name: {mag.name}, Category: {mag.category}")

    # --- Proof 3: Check articles per magazine ---
    print("\n=== Magazine1 Articles ===")
    for art in magazine1.articles():
        print(f"Title: {art.title}, Author: {art.author.name}")

    # --- Proof 4: Check topic areas for an author ---
    print("\n=== Author1 Topic Areas ===")
    topics = author1.topic_areas()
    print(topics if topics is not None else "No topics available.")

    # --- Proof 5: Test updating mutable magazine properties ---
    print("\n=== Updating Magazine1 Properties ===")
    print(f"Old Name: {magazine1.name}, Old Category: {magazine1.category}")
    magazine1.name = "NewTech"        # Valid update
    magazine1.category = "Innovation" # Valid update
    print(f"Updated Name: {magazine1.name}, Updated Category: {magazine1.category}")

     magazine1.name = 123          
     magazine1.category = ""       
    
    ipdb.set_trace()
