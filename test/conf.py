# -*- coding: utf-8 -*-

import sys, os

sys.path.insert(0, os.path.abspath('..'))
import setup as setupfile

latex_engine = 'xelatex'

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
'preamble': r'''
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{unicode-math}
\theoremstyle{plain}                        
\newtheorem{theorem}{Theorem}               
\newtheorem{lemma}{Lemma}                   
\newtheorem{corollary}{Corollary}           
\newtheorem{proposition}{Proposition}       
\newtheorem{conjecture}{Conjecture}         
\newtheorem{criterion}{Criterion}           
\newtheorem{assertion}{Assertion}           
\theoremstyle{definition}                   
\newtheorem{definition}{Definition}         
\newtheorem{condition}{Condition}           
\newtheorem{problem}{Problem}               
\newtheorem{example}{Example}               
\newtheorem{exercise}{Exercise}             
\newtheorem{algorithm}{Algorithm}           
\newtheorem{question}{Question}             
\newtheorem{axiom}{Axiom}                   
\newtheorem{property}{Property}             
\newtheorem{assumption}{Assumption}         
\newtheorem{hypothesis}{Hypothesis}         
\theoremstyle{remark}                       
\newtheorem{remark}{Remark}                 
\newtheorem{notation}{Notation}             
\newtheorem{claim}{Claim}                   
\newtheorem{summary}{Summary}               
\newtheorem{acknowledgment}{Acknowledgment} 
\newtheorem{case}{Case}                     
\newtheorem{conclusion}{Conclusion}         
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

