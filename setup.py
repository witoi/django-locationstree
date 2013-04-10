# encoding=UTF-8
import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-locationstree',
    version=__import__('locationstree').__version__,
    author=u'Witoi.com',
    author_email='dev@witoi.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/witoi/django-locationstree',
    description=u' '.join(__import__('locationstree').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'Django>=1.4',
        'django-mptt>=0.5.5',
    ],
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
)
