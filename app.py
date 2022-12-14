from flask import Flask, render_template


app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1. LAlalalalalalala.',
        'author': 'Lala'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2. LAlalalalalalala.'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home')
def hello():
    return 'Hello home2'

@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'You can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)