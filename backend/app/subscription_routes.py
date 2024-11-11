from flask import Blueprint, request, jsonify, session
from .config import get_db_connection
from functools import wraps
from .scrape_routes import scrape_user, scrape_posts  # Import the scrape functions

subscription_bp = Blueprint('subscription', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

@subscription_bp.route('/subscriptions', methods=['GET'])
@login_required
def get_subscriptions():
    user_id = session['user_id']
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT insta_accounts.insta_username 
                FROM subscriptions
                JOIN insta_accounts ON subscriptions.insta_account_id = insta_accounts.insta_account_id
                WHERE subscriptions.user_id = %s
            """, (user_id,))
            subscriptions = cur.fetchall()
    
    return jsonify({"subscriptions": [row[0] for row in subscriptions]}), 200

@subscription_bp.route('/subscriptions', methods=['POST'])
@login_required
def add_subscription():
    user_id = session.get('user_id')
    insta_username = request.json.get("insta_username")
    
    if not insta_username:
        return jsonify({"error": "Instagram username required"}), 400

    # Verify if the Instagram account exists
    try:
        insta_account_id = int(scrape_user(insta_username))  # Convert to int explicitly
    except Exception as e:
        print(f"Error in scrape_user: {e}")
        return jsonify({"error": "Instagram account not found or inaccessible"}), 404

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Check if the user is already subscribed to this account
            cur.execute("SELECT * FROM subscriptions WHERE user_id = %s AND insta_account_id = %s", (user_id, insta_account_id))
            if cur.fetchone():
                return jsonify({"message": "Already subscribed"}), 409

            # Add the Instagram account to the database if it doesn't exist
            cur.execute("""
                INSERT INTO insta_accounts (insta_account_id, insta_username) 
                VALUES (%s, %s) 
                ON CONFLICT (insta_username) DO NOTHING
                RETURNING insta_account_id
            """, (insta_account_id, insta_username))
            
            # Fetch the newly inserted or existing insta_account_id
            if cur.rowcount == 0:
                print("Account already exists in database.")
            else:
                print(f"Added insta_account_id: {insta_account_id} for username {insta_username}")

            # Subscribe the user to the Instagram account
            cur.execute("INSERT INTO subscriptions (user_id, insta_account_id) VALUES (%s, %s)", (user_id, insta_account_id))
            conn.commit()

    # Trigger the post-scraping function for the newly added account
    scrape_result = scrape_posts(insta_account_id, insta_username)
    if 'error' in scrape_result:
        return jsonify({"message": f"Subscribed to {insta_username} but failed to scrape posts", "error": scrape_result['error']}), 207

    return jsonify({"message": f"Subscribed to {insta_username} successfully"}), 201


@subscription_bp.route('/subscriptions', methods=['DELETE'])
@login_required
def delete_subscription():
    user_id = session['user_id']
    insta_username = request.json.get("insta_username")

    if not insta_username:
        return jsonify({"error": "Instagram username required"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT insta_account_id FROM insta_accounts WHERE insta_username = %s", (insta_username,))
            result = cur.fetchone()

            if result:
                insta_account_id = result[0]
                cur.execute("DELETE FROM subscriptions WHERE user_id = %s AND insta_account_id = %s", (user_id, insta_account_id))
                conn.commit()
                return jsonify({"message": f"Unsubscribed from {insta_username}"}), 200
            else:
                return jsonify({"error": "Instagram account not found"}), 404


@subscription_bp.route('/posts/<string:insta_username>', methods=['GET'])
def get_posts(insta_username):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Check if the Instagram account exists in the database
            cur.execute("SELECT insta_account_id FROM insta_accounts WHERE insta_username = %s", (insta_username,))
            insta_account = cur.fetchone()

            if not insta_account:
                return jsonify({"error": "Instagram account not found"}), 404

            insta_account_id = insta_account[0]

            # Retrieve all posts associated with the Instagram account
            cur.execute("""
                SELECT post_id_str, shortcode, dimensions_height, dimensions_width, src, src_attached, video_url, 
                       location, taken_at, is_video, link, caption_text
                FROM posts
                WHERE insta_account_id = %s
                ORDER BY taken_at DESC
            """, (insta_account_id,))

            posts = cur.fetchall()

            # Format the posts as a list of dictionaries
            post_list = [
                {
                    "post_id": row[0],
                    "shortcode": row[1],
                    "dimensions": {"height": row[2], "width": row[3]},
                    "src": row[4],
                    "src_attached": row[5],
                    "video_url": row[6],
                    "location": row[7],
                    "taken_at": row[8],
                    "is_video": row[9],
                    "link": row[10],
                    "caption_text": row[11],
                }
                for row in posts
            ]

    return jsonify({"username": insta_username, "posts": post_list}), 200