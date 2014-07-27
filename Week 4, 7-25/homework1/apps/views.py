from flask import render_template, Flask, request, url_for
from apps import app

from google.appengine.ext import db

class TextDB(db.Model):
	textdb = db.StringProperty()

@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload_db():
	upload_text = request.form['text']

	upload_data = TextDB()
	upload_data.textdb = upload_text
	upload_data.put()

	uploaded_data = db.get(upload_data.key())

	loaded_text = uploaded_data.textdb

	return render_template("upload.html", text=loaded_text)
	