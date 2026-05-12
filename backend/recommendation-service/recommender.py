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

    def recommend_courses(
        self,
        query,
        difficulty=None,
        top_n=5
    ):

        print("\nGenerating recommendations...")

        # ---------------------------------
        # Convert query into TF-IDF vector
        # ---------------------------------

        query_vector = self.vectorizer.transform([query.lower()])

        # ---------------------------------
        # Calculate cosine similarity
        # ---------------------------------

        similarity_scores = cosine_similarity(
            query_vector,
            self.tfidf_matrix
        ).flatten()

        # ---------------------------------
        # Copy dataset
        # ---------------------------------

        results = self.df.copy()

        # ---------------------------------
        # Add similarity scores
        # ---------------------------------

        results['similarity'] = similarity_scores

        # ---------------------------------
        # Filter by difficulty if provided
        # ---------------------------------

        if difficulty:

            results = results[
                results['course_difficulty'].str.lower()
                ==
                difficulty.lower()
            ]

        # ---------------------------------
        # Calculate final weighted score
        # ---------------------------------

        results['final_score'] = (

            results['similarity']

            *

            results['rating']

            *

            np.log1p(results['enrollment'])

        )

        # ---------------------------------
        # Sort recommendations
        # ---------------------------------

        results = results.sort_values(
            by='final_score',
            ascending=False
        )

        # ---------------------------------
        # Return top recommendations
        # ---------------------------------

        return results[
            [
                'course_title',
                'course_organization',
                'course_difficulty',
                'rating',
                'enrollment',
                'similarity',
                'final_score'
            ]
        ].head(top_n)
    



if __name__ == "__main__":

    recommender = CourseRecommender()

    recommendations = recommender.recommend_courses(
        query="machine learning",
        difficulty="Beginner",
        top_n=5
    )

    print("\nTop Recommendations:\n")

    print(recommendations)