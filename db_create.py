from app import app, db, BlogPost

with app.app_context():
    db.session.add(BlogPost(title='Blog Post 4', content='Content of Blog post 4. Tqeeqeqdeweflal',))
    db.session.commit()
