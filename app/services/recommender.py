# services/recommender.py

import numpy as np

def recommend_books(book_name, pt, similarity_scores, final_df):
    if book_name not in pt.index:
        return None

    index = np.where(pt.index == book_name)[0][0]
    suggestions = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    recommended_books = []

    for i in suggestions:
        title = pt.index[i[0]]
        book_data = final_df[final_df['title'] == title].iloc[0]

        recommended_books.append({
            'title': str(title),
            'author': str(book_data['author']),
            'image_url': str(book_data['Image-URL-M']),
            'year': str(book_data['year'])
        })

    return recommended_books
