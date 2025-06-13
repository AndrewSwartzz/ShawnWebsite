from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'dev-secret-key'

# Sample data (replace with your own)
dad_info = {
    "name": "Shawn Swartz",
    "bio": "World's greatest dad",
    "interests": ["Umping", "Sports", "Cooking"]
}

@app.route("/")
def home():
    return render_template("index.html", dad=dad_info)

@app.route("/about")
def about():
    return render_template("about.html", dad=dad_info)


@app.route("/gallery")
def gallery():
    try:
        images = os.listdir('/Users/andrewswartz/PycharmProjects/DadWebsite/app/static/images')
    except FileNotFoundError:
        images = []

    return render_template("gallery.html", images=images)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Add email sending or database storage here
        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)