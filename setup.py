import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-penn_user',
    version='0.1',
    packages=['penn_user'],
    include_package_data=True,
    license='BSD License',
    description="A simple Django app to use the University of Pennsylvania''s CoSign auth and extend Django's base user.",
    long_description=README,
    url='http://stash.wharton.upenn.edu/',
    author='Timothy Allen, the Wharton School',
    author_email='tallen@wharton.upenn.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
