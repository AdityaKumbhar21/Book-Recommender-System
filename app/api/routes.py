from fastapi import APIRouter, HTTPException
from app.models.schema import UserRequest
from app.services.recommender import recommend_books
from app.data.loader import load_pt, load_similarity, load_final_df, load_popular_df

router = APIRouter()

pt = load_pt()
similarity_scores = load_similarity()
final_df = load_final_df()
popular = load_popular_df()



@router.get('/home')
def home():
    res = popular.to_dict(orient='records')
    return {'popular': res}



@router.post('/recommend')
def recommend(req: UserRequest):
    res = recommend_books(req.book_name, pt, similarity_scores, final_df)

    if res is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"recommendations": res}
