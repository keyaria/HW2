## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required
import requests
#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

class AlbumEntryForm():

	name = StringField('Enter the name of an album:', validators.Datarequired())
	rate = RadioField('How much do you like this album? (1 low, 3 high)', choices=[('1'),('2'),('3')],validators.Datarequired())


####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform', methods = ['POST', 'GET'])
def artistform():
	#form = ReusableForm(request.form)
	return render_template('artistform.html')

@app.route('/artistinfo', methods = ['POST', 'GET'])
def artistinfo():
	if request.method == 'GET':
		url = "https://itunes.apple.com/search"
		name = request.args['artist']
		param = {'term': name,}
		search = (requests.get(url=url, params=param)).json()
		#print(search)
		return render_template('artist_info.html', objects=search['results'])

@app.route('/artistlinks')
def artistlinks():
	return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>')
def specific(artist_name):
	url = "https://itunes.apple.com/search"
	param = {'term': artist_name,}
	search = (requests.get(url=url, params=param)).json()
	return render_template('specific_artist.html',results=search['results'])

@app.route('/album_entry')
def albumentry():
	form = AlbumEntryForm(request.form)
	return render_template('album_data.html', form=form)

@app.route('/album_result')
def album_result():
	form = AlbumEntryForm(request.form)
	return render_template('album_data.html', form=form)
if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
