"""App configuration."""
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()

requires = [
    'Flask>=0.12.1',
    'jinja2',
    'flask_sqlalchemy',
]

setup(name='flask_tut',
      version='0.0',
      description='flask_tut',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg flask',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='flask_tut',
      install_requires=requires,
      )
