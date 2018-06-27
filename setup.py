import codecs
import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


setup(
    name='django-ga-intl-app',
    version='4.3.0',
    description=('Django Google Analytics app allowing for server side/non-js (fork with international url support)'
                 'tracking.'),
    long_description=read('README.rst'),
    author='Praekelt.org',
    author_email='dev@praekelt.org',
    license='BSD',
    url='https://github.com/LaurenBenoit/django-google-analytics-international.git',
    packages=find_packages(),
    install_requires=[
        'django<2.0',
        'django-celery',
        'celery<4.0',
        'requests',
        'beautifulsoup4',
        'six',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
