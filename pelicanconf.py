#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vineed A'
SITENAME = "Vineed's (avvineed) Blog"
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Software Engineer'
SITEDESCRIPTION = '%s\'s (avvineed) Thoughts and Writings' % AUTHOR
SITELOGO = '/img/VA.png'

FAVICON = '/img/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'friendly'

ROBOTS = 'index, follow'


PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/avineed/'),
          ('github', 'https://github.com/avvineed'),
          ('twitter', 'https://twitter.com/WhimsyMind'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)



CC_LICENSE = {
}

COPYRIGHT_YEAR = "2018 Whimsy Mind Inc"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

#Pluigin jupyter
MARKUP = ( 'ipynb' , 'md')
# @todo change theme path
THEME = '../pelican-themes/Flex'
IPYNB_FIX_CSS = False
PLUGIN_PATHS = ['plugins','pelican-plugins']
PLUGINS = ['ipynb.markup','sitemap', 'post_stats', "i18n_subsites"]

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

IGNORE_FILES = ['.ipynb_checkpoints']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

STATIC_PATHS = [ 'img','extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'