#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Panta'
SITENAME = 'PyPanta'
SITEURL = 'https://pypanta.github.io'
#SITEURL = 'http://localhost:8000/'
#RELATIVE_URLS = True
PATH = 'content'

TIMEZONE = 'Europe/Belgrade'

DEFAULT_DATE_FORMAT = "%d %m %Y"

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'default'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DIRECT_TEMPLATES = ['index', 'categories']

THEME = "theme/pypanta"
#THEME = "/home/myuser/projects/mysite/themes/mycustomtheme"

SUMMARY_MAX_LENGTH = 30
