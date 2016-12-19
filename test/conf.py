# -*- coding: utf-8 -*-

import sys, os

sys.path.insert(0, os.path.abspath('..'))
import setup as setupfile

extensions = ['sphinxcontrib.thm']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'thm Sphinx Extension'
copyright = '2016, Roland Puntaier'

version = setupfile.VERSION
release = setupfile.VERSION

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_static_path = ['_static']
htmlhelp_basename = 'thmdoc'

latex_elements = {
'preamble': '''
\usepackage{amsmath}
\usepackage{unicode-math}
''',
}

latex_documents = [
  ('index', 'thm.tex', 'thm Sphinx Extension Documentation',
   'Roland Puntaier', 'howto'),
]

man_pages = [
    ('index', 'thm', 'thm Sphinx Extension Documentation',
     ['Roland Puntaier'], 1)
]

texinfo_documents = [
  ('index', 'thm', 'thm Sphinx Extension Documentation',
   'Roland Puntaier', 'thm', 'One line description of project.',
   'Miscellaneous'),
]
