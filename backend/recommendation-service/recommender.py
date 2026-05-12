import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CourseRecommender:

    def __init__(self):

        print("Loading cleaned dataset...")

        self.df = pd.read_csv("data/courses_clean.csv")

        print("Dataset loaded successfully")

        print("Total courses:", len(self.df))

        print("Initializing TF-IDF vectorizer...")

        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=5000
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.df['search_text']
        )

        print("TF-IDF matrix created successfully")


if __name__ == "__main__":

    recommender = CourseRecommender()