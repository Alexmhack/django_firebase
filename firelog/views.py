import pyrebase

config = {
	apiKey: "AIzaSyCT2VKf1_P7gBfecoi_umWXAAT4uA59OFo",
	authDomain: "django-project-dc6f8.firebaseapp.com",
	databaseURL: "https://django-project-dc6f8.firebaseio.com",
	projectId: "django-project-dc6f8",
	storageBucket: "django-project-dc6f8.appspot.com",
	messagingSenderId: "457756878283"
}

firebase = pyrebase.initialize_app(config)