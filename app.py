from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from pytz import timezone  # <-- ADD THIS IMPORT

app = Flask(__name__, static_url_path='', static_folder='.')

# --- Database Setup ---
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False) # We will set the default in the route

    def __repr__(self):
        return f'<Submission {self.name}>'
# --- End of Setup ---

@app.route('/')
def home():
    with app.app_context():
        db.create_all()
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # --- CHANGE THIS LINE ---
        # Get the current time in the 'Asia/Kolkata' timezone
        india_time = datetime.now(timezone('Asia/Kolkata'))
        
        # Create a new submission object and add it to the database
        new_submission = Submission(name=name, email=email, message=message, timestamp=india_time)
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