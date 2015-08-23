# -*- coding: utf-8 -*-

import os

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

extensions = []

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Ichnaea'
copyright = u'2013-2015, Mozilla'

# The short X.Y version.
version = '1.3'
# The full version, including alpha/beta/rc tags.
release = '1.3'

exclude_patterns = []

pygments_style = 'sphinx'
html_static_path = []

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
