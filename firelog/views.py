import pyrebase

from django.shortcuts import render

config = {
	'apiKey': "AIzaSyCT2VKf1_P7gBfecoi_umWXAAT4uA59OFo",
	'authDomain': "django-project-dc6f8.firebaseapp.com",
	'databaseURL': "https://django-project-dc6f8.firebaseio.com",
	'projectId': "django-project-dc6f8",
	'storageBucket': "django-project-dc6f8.appspot.com",
	'messagingSenderId': "457756878283"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def sign_in(request):
	return render(request, 'sign_in.html')


def post_sign(request):
	email = request.POST.get('email')
	password = request.POST.get('pass')

	try:
		user = auth.sign_in_with_email_and_password(email, password)
	except Exception as e:
		message = "Invalid Credentials"
		print(e)
		return render(request, 'sign_in.html', {'msg': message})

	print(user)
	return render(request, 'welcome.html', {"email": email})