from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    
   1: {"title": "Welcome to FastAPI", "content": "FastAPI makes building APIs fast and enjoyable."},
   2: {"title": "Python Tips","content": "Use list comprehensions to write cleaner code."},
   3: {"title": "React vs Vue","content": "Both are great frontend frameworks with different philosophies."},
   4: { "title": "Football Update","content": "Manchester City wins 3-1 in an intense match."},
   5: {"title": "AI in 2025","content": "Automation and AI continue to transform modern businesses."},
   6: {"title": "Daily Motivation","content": "Consistency beats motivation every time."},
   7: {"title": "Travel Diaries","content": "Exploring new cities gives fresh perspectives."},
   8: {"title": "Health Tips","content": "Drink water and stretch every morning."},
   9: {"title": "Tech News", "content": "New smartphone releases this month are impressive."},  
  10: {"title": "Cooking Guide","content": "Try adding garlic butter for better flavor.",}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts



@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(id)