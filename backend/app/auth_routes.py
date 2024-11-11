from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from .config import get_db_connection
import psycopg

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    hashed_pw = generate_password_hash(password)
    
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, pw) VALUES (%s, %s) RETURNING user_id", 
                            (username, hashed_pw))
                user_id = cur.fetchone()[0]
                conn.commit()
    except psycopg.errors.UniqueViolation:
        return jsonify({"error": "Username already exists"}), 409

    return jsonify({"message": "User registered successfully", "user_id": user_id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id, pw FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
    
    if user and check_password_hash(user[1], password):
        session['user_id'] = user[0]
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"}), 200
