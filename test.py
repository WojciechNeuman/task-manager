from app import app, db

# Use the Flask application context
with app.app_context():
    # Create all database tables
    db.create_all()
