#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Suhas'
SITENAME = u'The Coder Earth Blog'
SITEURL = ''

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["render_math"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

# Blogroll
LINKS = (('Suhas', 'http://suhas.co'),
         ('Kunal', 'https://github.com/patelkunal'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/coderorg'),
          ('Github', 'https://github.com/coderearth'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-41102923-3'
DISQUS_SITENAME = 'coderearth'
