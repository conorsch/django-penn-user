# Django Penn CoSign Custom User Template

## Installing CoSign and Setting Up Apache
* Please see ISC's instructions here: http://www.upenn.edu/computing/weblogin/docs/apache_installation.html
* An example Apache httpd conf file is located in examples/

## Installing the Django App
* Add this line to the requirements.txt of your Django project:
git+https://github.com/wharton/django-penn-user.git

* Or, install via pip:
pip install git+https://github.com/wharton/django-penn-user.git

## Modifying Your Settings Files to add the Middleware and Backends

In order to integrate CoSign with the Django auth system, we have to tell Django to use the REMOTE_USER server variable. This is done by add the RemoteUserMiddleware module to the MIDDLEWARE_CLASSES setting, and setting the RemoteUserBackend as the default AUTHENTICATION_BACKEND. In your appropriate settings file (settings/base.py, or only in settings/prod.py if you don't have access to the CoSign server on dev) file, add the line 'django.contrib.auth.middleware.RemoteUserMiddleware' after the 'django.contrib.auth.middleware.AuthenticationMiddleware' line in your MIDDLEWARE_CLASSES setting. Also, add the variable "AUTHENTICATION_BACKENDS" as a tuple, and add 'django.contrib.auth.backends.RemoteUserBackend' as the first entry.

You must also add this app to your installed apps. Before doing so, make sure you have done your initial migration of your Django project to create the user and group table in the database, or there will be nothing to inherit from and the app will error.

Here is an example of this configuration:

```
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

CUSTOM_USER_MODEL = 'pennuser.PennUser'

INSTALLED_APPS = (
    'bootstrap3',
    'pennuser',
)
```

Or, for prod.py only (handy, if you want to use Django's auth for local dev):

```
MIDDLEWARE_CLASSES += (
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

AUTHENTICATION_BACKENDS += (
    'django.contrib.auth.backends.RemoteUserBackend',
)

INSTALLED_APPS += (
    'pennuser',
)
```

Then, you can begin to customize the models.py (and auth_backend.py if necessary).

Don't forget to run this to create the necessary pennuser_pennuser table in your Django Project's database after adding the pennuser app to INSTALLED_APPS:

```
python manage.py migrate
```

Feel free to contact me with questions: tallen@upenn.edu

TODO
----
* bootstrap tests
* write custom backend for Cosign support
* Shibb support?
* more validators for PennUser model attributes

CONTRIBUTORS:
-------------
* Conor Schaefer
* Tim Allen

THANK YOU:
----------
* To the fine people of Information & Systems Computing at the University of Pennsylvania.
* To the fine people of University of Michigan, who's (now deprecated) article got this started in Django 1.4.
