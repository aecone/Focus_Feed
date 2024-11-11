from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from .config import get_db_connection
from functools import wraps

user_bp = Blueprint('user', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

@user_bp.route('/user/password', methods=['PUT'])
@login_required
def change_password():
    user_id = session['user_id']
    data = request.get_json()
    current_password = data.get("current_password")
    new_password = data.get("new_password")
    
    if not current_password or not new_password:
        return jsonify({"error": "Both current and new passwords are required"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT pw FROM users WHERE user_id = %s", (user_id,))
            user = cur.fetchone()

            if user and check_password_hash(user[0], current_password):
                new_hashed_pw = generate_password_hash(new_password)
                cur.execute("UPDATE users SET pw = %s WHERE user_id = %s", (new_hashed_pw, user_id))
                conn.commit()
                return jsonify({"message": "Password changed successfully"}), 200
            else:
                return jsonify({"error": "Current password is incorrect"}), 401

@user_bp.route('/user/update_frequency', methods=['PUT'])
@login_required
def update_frequency():
    user_id = session['user_id']
    data = request.get_json()
    update_frequency = data.get("update_frequency")
    
    if not update_frequency:
        return jsonify({"error": "Update frequency is required"}), 400
    
    if not isinstance(update_frequency, int) or update_frequency < 1 or update_frequency > 3:
        return jsonify({"error": "Update frequency must be an integer between 1 and 3"}), 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET update_frequency = %s WHERE user_id = %s", (update_frequency, user_id))
            conn.commit()

    return jsonify({"message": f"Update frequency set to {update_frequency}"}), 200

@user_bp.route('/user', methods=['DELETE'])
@login_required
def delete_user():
    user_id = session['user_id']
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM subscriptions WHERE user_id = %s", (user_id,))
            cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
    
    session.pop('user_id', None)
    return jsonify({"message": "User account deleted successfully"}), 200
