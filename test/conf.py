# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(0, os.path.abspath('..'))
import setup as setupfile
latex_engine = 'xelatex'
extensions = ['sphinxcontrib.thm', 'sphinx.ext.mathjax']
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
%preamble for sphinxcontrib-thm
\usepackage{amsmath}
\usepackage{unicode-math}
\usepackage{amsthm}%\usepackage{ntheorem} works too
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
\newtheorem{instruction}{Instruction}%because we used .. environment:: instruction
%\newtheorem{proof}{Proof} for ntheorem
''',
}
latex_documents = [
  ('index', 'thm.tex', 'thm Sphinx Extension Documentation',
   'Roland Puntaier', 'howto'),
]
def custom_css(app,exception):
    with open(exclude_patterns[0]+'/html/'+html_static_path[0]+'/custom.css','a') as f:
        f.write("""
div.thm_caption{
    padding-top: 0.3ex;
    font-weight: bold;
}
span.thm_counter{
    padding-left: 4px;
}
span.thm_title{
    font-weight: bold;
    font-style: italic;
}
div.thm_body{
    padding-left: 1em;
}
div.instruction::before{
    content:"Instruction:";
    font-weight: bold;
}
div.instruction_title{
    font-weight: bold;
    font-style: italic;
}
div.instruction_body{
    padding-left: 1em;
}
p.flushleft{
    text-align: left;
}
p.flushright{
    text-align: right;
}
p.center{
    text-align: center;
}
        """);
def setup(app):
    app.connect('build-finished', custom_css)

