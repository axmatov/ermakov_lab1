import requests
import json
from intro_to_flask import app
from flask import Flask, render_template, request, flash, redirect
from forms import ContactForm
 
auth = 0
access_token = None;
my_id ='9qan5tt0a0hh2fa52209tpc8la'

@app.route('/', methods = ['GET', 'POST'])
def home():
  global access_token
  global auth
  if auth == 77 and access_token == None: #obviously what should be tested is if the access token is still valid..but thats for another time
  	   xx = request.args.get('code')
           r = requests.post("https://secure.meetup.com/oauth2/access?client_id=9qan5tt0a0hh2fa52209tpc8la&client_secret=egllavke7je7ecfmdfkhnraaj0&grant_type=authorization_code&redirect_uri=http://localhost:5000&code="+str(xx))
	   rr = r.json()
	   access_token = rr['access_token']
	   auth = 0;
	   return redirect('/data')
  return render_template('home.html')
 
@app.route('/data')
def data():
  global access_tocken
  request_url_base  = 'https://api.meetup.com/' 
  ny_tech_url = request_url_base + '2/events?&group_urlname=ny-tech&sign=true'
  header1 = "Authorization" 
  header2 = "bearer " + access_token
  data_test = requests.get(ny_tech_url, headers = {header1 : header2})	
  data_test = data_test.json()
  flash(str(data_test))
  member_url = request_url_base + '2/member/?key='+ my_id  +'&member_id=self'
  data_test = requests.get('https://api.meetup.com/2/member/self?&sign=true&photo-host=public&page=20i', headers = {header1 : header2})	
  data_test = data_test.json()
  flash(str(data_test))
  return render_template('data.html')  

@app.route('/auth')
def auth():
  global auth
  auth = 77;
  return redirect("https://secure.meetup.com/oauth2/authorize?client_id=9qan5tt0a0hh2fa52209tpc8la&response_type=code&redirect_uri=http://localhost:5000", code=302)

@app.route('/about')
def about():
  return render_template('about.html')
"""
@app.route('/contact', methods= ['GET', 'POST'])
def contact():
   form = ContactForm()

   if request.method == 'POST':
	if form.validate() == False:
	   	flash('All fields are required.')
	   	return render_template('contact.html', form=form)
	else:
	   	return 'Form posted.'

   elif request.method == 'GET':
	return render_template('contact.html', form = form)

   return render_template('contact.html', form = form)
"""
if __name__ == '__main__':
  app.run(debug=True)



