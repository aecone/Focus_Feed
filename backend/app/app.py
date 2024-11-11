from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from .auth_routes import auth_bp
from .subscription_routes import subscription_bp
from .user_routes import user_bp
from .scrape_routes import scrape_bp
from .proxy_routes import proxy_bp


load_dotenv(os.path.join(os.path.dirname(__file__), '../local.env'))

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SESSION_COOKIE_SAMESITE'] = "Lax"
app.config['SESSION_COOKIE_SECURE'] = False
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(subscription_bp)
app.register_blueprint(user_bp)
app.register_blueprint(scrape_bp)
app.register_blueprint(proxy_bp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

