from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, static_url_path='', static_folder='.')

# --- Database Setup ---
# Get the database URL from the environment variable set in Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Submission database model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Submission {self.name}>'
# --- End of Setup ---

@app.route('/')
def home():
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a new submission object and add it to the database
        new_submission = Submission(name=name, email=email, message=message)
        db.session.add(new_submission)
        db.session.commit()

        return """
        <html>
            <head><title>Thank You</title></head>
            <body>
                <h2>Thank you for your message!</h2>
                <p>I will get back to you soon.</p>
                <a href="/">Return to homepage</a>
            </body>
        </html>
        """

if __name__ == '__main__':
    app.run()