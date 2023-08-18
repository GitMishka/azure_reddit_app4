from flask import Flask, render_template, request
from reddit_service import create_reddit_instance, get_subreddits, search_reddit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

# @app.route('/search', methods=['POST'])
# def search():
#     reddit = create_reddit_instance()
#     username = request.form.get('username')
#     search_string = request.form.get('search_string')
    
#     subreddits = get_subreddits(reddit, username)
#     matching_posts, matching_comments = search_reddit(reddit, username, search_string)
    
#     return render_template('results.html', username=username, subreddits=subreddits, 
#                            matching_posts=matching_posts, matching_comments=matching_comments)
@app.route('/search', methods=['POST'])
def search():
    reddit = create_reddit_instance()
    
    username = request.form.get('username')
    search_string = request.form.get('search_string')

    subreddits = []
    matching_posts = []
    matching_comments = []

    # If a username is provided, get their subreddits
    if username:
        subreddits = get_subreddits(reddit, username)
    
    # If a search string is provided, search for it either globally or for the specific user
    if search_string:
        matching_posts, matching_comments = search_reddit(reddit, username if username else None, search_string)

    # You can add more conditions to handle cases where both fields are empty, etc.

    return render_template('results.html', username=username if username else 'Reddit', 
                           subreddits=subreddits, 
                           matching_posts=matching_posts, 
                           matching_comments=matching_comments)


if __name__ == "__main__":
    app.run(debug=True)
