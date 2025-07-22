# Book Recommender System 📚

## Overview

This project develops a **Book Recommender System** designed to help users discover new books based on their preferences and the behavior of similar readers. In an age of overwhelming choices, a good recommendation system is crucial for enhancing user experience and increasing engagement. This system aims to provide personalized book suggestions, making the discovery process intuitive and enjoyable.

* **Live APP :** [Link](https://book-recommendation-ui.vercel.app/)

## Features

* **Personalized Recommendations:** Suggests books tailored to individual user tastes.

* **User-Item Interaction Analysis:** Leverages historical user ratings and interactions to find relevant recommendations.

## Dataset

This project utilizes a dataset containing book information and user ratings.

* **Source:** <https://www.kaggle.com/datasets/ra4u12/bookrecommendation>

* **Key Data Points:**

    * `Books`: ISBN, Title, Author, Year of Publication, Publisher, Image-URLs.

    * `Users`: User-ID, Location, Age.

    * `Ratings`: User-ID, ISBN, Book-Rating.

## Methodology

The recommender system employs a **hybrid approach, combining Popularity-Based and Collaborative Filtering techniques** to provide comprehensive recommendations.

The key steps involved are:

1.  **Data Loading & Initial Exploration:** Loading the datasets and performing an initial exploratory data analysis (EDA) to understand data distributions, missing values, and potential biases.

2.  **Data Preprocessing:**

    * Handling missing values and inconsistencies.

    * Filtering out infrequent books or inactive users to improve recommendation quality.

    * \[Mention specific preprocessing for your chosen method, e.g., "Creating a user-item interaction matrix," "Text processing for content-based features."\]

3.  **Model Building:**

    * **Popularity-Based Recommendation:**

        * Identifies the top 50 books with the highest average ratings.

        * **Criteria:** Only books with at least 250 ratings are considered to ensure statistical significance.

    * **Collaborative Filtering Recommendation:**

        * Constructs a user-item matrix where columns represent users and rows represent books, populated with user ratings.

        * **Criteria:** Only users who have provided more than 200 ratings and books with more than 50 ratings are included to focus on active users and well-rated books.

        * Recommendations are generated based on **Cosine Similarity** between books (item-item similarity) or users (user-user similarity) within this filtered matrix.

4.  **Recommendation Generation:** Developing functions to generate real-time recommendations for a given book.

## Technologies Used

* **Programming Language:** Python

* **Libraries:**

    * `pandas` for data manipulation and analysis.

    * `numpy` for numerical operations.

    * `scikit-learn` for machine learning utilities like **cosine_similarity**.

## Results & Key Findings

* The system successfully identifies and recommends books based on the title.

## Contact

Feel free to reach out if you have any questions or feedback!

* **Aditya Kumbhar**

* **GitHub:** [https://github.com/AdityaKumbhar21](https://www.google.com/search?q=https://github.com/AdityaKumbhar21)


## License

This project is licensed under the MIT License - see the `LICENSE` file for details