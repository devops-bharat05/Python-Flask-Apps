from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import URL
import string, random

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Home route to display the URL shortener form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        url = URL(original_url=original_url, short_id=short_id)
        db.session.add(url)
        db.session.commit()

        return render_template('result.html', short_url=request.host_url + short_id)
    return render_template('home.html')

# Route to handle shortened URL redirection
@app.route('/<short_id>')
def redirect_to_url(short_id):
    url = URL.query.filter_by(short_id=short_id).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for the models
    app.run(host='0.0.0.0',port=5000)
