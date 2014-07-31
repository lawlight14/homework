# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for, render_template
from apps import app
from database import Database

dataStorage = Database()
isReverse = True

@app.route('/', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	storage={}
	storage['num'] = dataStorage.num
	storage['count'] = 0
	storage['title'] = request.form['title']
	storage['contents'] = request.form['contents']
	dataStorage.put(storage)

	dataStorage.num += 1
	return redirect(url_for('show_entries'))

@app.route('/asc')
def asc_entry():
	global isReverse
	isReverse = False
	dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'], reverse=isReverse)
	return redirect(url_for('show_entries'))

@app.route('/desc')
def desc_entry():
	global isReverse
	isReverse = True
	dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'], reverse=isReverse)
	return redirect(url_for('show_entries'))

@app.route('/del/<idx>')
def del_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			dataStorage.database.remove(data)
			break

	return redirect(url_for('show_entries'))

@app.route('/plus/<idx>')
def plus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['count'] += 1
			break

	dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'], reverse=isReverse)
	return redirect(url_for('show_entries'))

@app.route('/minus/<idx>')
def minus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			if data['count'] != 0:
				data['count'] -= 1
			break

	dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'], reverse=isReverse)
	return redirect(url_for('show_entries'))
			
@app.route('/modify/<idx>')
def modify_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['title'] = request.args['title']
			data['contents'] = request.args['contents']
			break

	return redirect(url_for('show_entries'))