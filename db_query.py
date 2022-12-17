from app import app, db, BlogPost

with app.app_context():
    print(BlogPost.query.all())