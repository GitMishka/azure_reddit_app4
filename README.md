#### Project Title: Reddit Search Flask Application

---

#### Description
This Flask application allows users to search Reddit posts and comments based on a username and keyword. It uses Python's Flask framework for the web interface and PRAW (Python Reddit API Wrapper) to interact with Reddit's API.

---

#### Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone [URL to the GitHub repository]
   ```

2. **Install Dependencies:**
   ```bash
   pip install flask praw
   ```

3. **Setup Reddit API Credentials:**
   - Create a Reddit API account.
   - Generate CLIENT_ID, CLIENT_SECRET, and USER_AGENT.
   - Place these credentials in a `config.py` file.

4. **Running the Application:**
   ```bash
   python app.py
   ```

---

#### Usage

- **Home Page (`/`):** 
  - Provides a form to enter the Reddit username and a search keyword.

- **Search Results (`/search`):**
  - Displays the most common subreddits, matching posts, and comments based on the input.

---

#### Files and Directories

- `app.py`: Main Flask application file.
- `reddit_service.py`: Contains functions to interact with Reddit.
- `/templates`: Folder containing HTML templates.
  - `search.html`: Form for initiating a search.
  - `results.html`: Displays the search results.
