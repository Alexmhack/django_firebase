import pyrebase

from django.shortcuts import render, redirect
from django.contrib import auth

firebase_api = open('../firebase_api.txt')

config = {
	'apiKey': firebase_api.read(),
	'authDomain': "django-project-dc6f8.firebaseapp.com",
	'databaseURL': "https://django-project-dc6f8.firebaseio.com",
	'projectId': "django-project-dc6f8",
	'storageBucket': "django-project-dc6f8.appspot.com",
	'messagingSenderId': "457756878283"
}

firebase = pyrebase.initialize_app(config)
fireauth = firebase.auth()
database = firebase.database()

def sign_in(request):
	return render(request, 'sign_in.html')


def post_sign(request):
	email = request.POST.get('email')
	password = request.POST.get('password')

	try:
		user = fireauth.sign_in_with_email_and_password(email, password)
	except Exception as e:
		message = "Invalid Credentials"
		print(e)
		return render(request, 'sign_in.html', {'msg': message})

	print(user['idToken'])
	session_id = user['idToken']
	request.session['uid'] = str(session_id)
	return render(request, 'welcome.html', {"email": email})


def logout(request):
	auth.logout(request)
	return render(request, 'sign_in.html')


def password_reset_view(request):
	return render(request, 'password_reset_form.html')


def password_reset_sent(request):
	try:
		email = request.POST.get('email')
		user = fireauth.send_password_reset_email(email)
	except Exception as e:
		message = "Please enter your email"
		print(e)
		return render(request, 'password_reset_form.html', {'msg': message})
	return render(request, 'password_reset_sent.html')


def signup(request):
	if request.method == 'POST':
		try:
			name = request.POST.get('name')
			email = request.POST.get('email')
			password = request.POST.get('password')
			user = fireauth.create_user_with_email_and_password(email, password)
			uid = user['localId']
			data = {'name': name, 'status': 1}
			database.child("users").child(uid).child("details").set(data)
			return redirect('sign_in')
		except Exception as e:
			message = "Unable to create account. Please Try again"
			print(e)
			# return render(request, 'sign_up.html', {'msg': message})
			return redirect('sign_in')
	else:
		return render(request, 'sign_up.html')