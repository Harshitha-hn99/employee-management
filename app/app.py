from flask import Flask

from config import Config
from database import db
from models import Employee
from routes import employee_bp
from flask import Flask, render_template


app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)
app.register_blueprint(employee_bp)

# Create database tables (only if they don't already exist)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
