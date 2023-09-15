from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_limiter import Limiter
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Add this line

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize Flask-Limiter
limiter = Limiter(key_func=lambda: request.remote_addr)
limiter.init_app(app)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, role FROM users WHERE id = %s', (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    
    if user_data:
        return User(id=user_data[0], username=user_data[1], role=user_data[2])
    else:
        return None
    
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/some_route', methods=['GET'])
@limiter.limit("5 per minute")
def some_route():
    return jsonify({"message": "This is rate-limited"})

# Audit trail logging function
def log_audit_trail(table_name, action, record_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO audit_trails (table_name, action, record_id, modified_by) VALUES (%s, %s, %s, %s)',
        (table_name, action, record_id, user_id)
    )
    conn.commit()
    conn.close()

@app.route('/create_forum', methods=['POST'])
def create_forum():
    missing_person_id = request.json['missing_person_id']
    title = request.json['title']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO forums (missing_person_id, title) VALUES (%s, %s)',
        (missing_person_id, title)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Forum created'})

@app.route('/add_comment', methods=['POST'])
def add_comment():
    forum_id = request.json['forum_id']
    content = request.json['content']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO comments (forum_id, content) VALUES (%s, %s)',
        (forum_id, content)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Comment added'})

@app.route('/list_forums/<int:missing_person_id>', methods=['GET'])
def list_forums(missing_person_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM forums WHERE missing_person_id = %s', (missing_person_id,))
    forums = cursor.fetchall()
    conn.close()

    return jsonify(forums)

@app.route('/list_comments/<int:forum_id>', methods=['GET'])
def list_comments(forum_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments WHERE forum_id = %s', (forum_id,))
    comments = cursor.fetchall()
    conn.close()

    return jsonify(comments)

@app.route('/add_missing_person', methods=['POST'])
@login_required
def add_missing_person():
    try:
        log_audit_trail('missing_persons', 'insert', new_record_id, current_user.id)
        # Fetch all the relevant information
        name = request.json['name']
        last_seen_date = request.json['last_seen_date']
        last_seen_location = request.json['last_seen_location']
        status = request.json['status']
        picture_url = request.json['picture_url']
        contact_info = request.json['contact_info']
        height = request.json['height']
        weight = request.json['weight']
        eye_color = request.json['eye_color']
        case_number = request.json['case_number']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        # ... [Database operations]
        conn.commit()
        
        # Get the ID of the newly inserted missing person
        new_record_id = cursor.lastrowid
        log_audit_trail('missing_persons', 'insert', new_record_id, current_user.id)
        
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        conn.rollback()
        return jsonify({'message': 'An error occurred'}), 500
    finally:
        conn.close()
        
    return jsonify({'message': 'Missing person added'}), 201

# New endpoint to upload media
@app.route('/upload_media', methods=['POST'])
@login_required
def upload_media():
    # Your code to upload media and save URL in the 'media' table
    log_audit_trail('media', 'insert', 0, current_user.id)
    return jsonify({'message': 'Media uploaded'})

# New endpoint to delete a comment
@app.route('/delete_comment/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}), 403
    # Your code to delete a comment
    log_audit_trail('comments', 'delete', comment_id, current_user.id)
    return jsonify({'message': 'Comment deleted'})

# New endpoint to search for missing persons
@app.route('/search_missing_persons', methods=['GET'])
def search_missing_persons():
    search_query = request.args.get('q')
    # Your code to perform the search
    return jsonify({'message': 'Search performed'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)