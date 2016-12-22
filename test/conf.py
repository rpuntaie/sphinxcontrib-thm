# -*- coding: utf-8 -*-

import sys, os, re
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
htmlhelp_basename = 'thmdoc'
latex_preamble = r"""
%preamble for sphinxcontrib-thm
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
"""
latex_elements = {'preamble':latex_preamble}
latex_documents = [
  ('index', 'thm.tex', 'thm Sphinx Extension Documentation','Roland Puntaier', 'howto'),
]

thmstyle="""
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
"""

def custom_css(app,exception):
    "write additional thmstyle css into custom.css"
    with open('_build/html/_static/custom.css','a',encoding='utf-8') as f:
        f.write(thmstyle)

#def custom_css(app,exception):
#    "copy all css into the html"
#    prefx = '_build/html/'
#    docf = prefx + master_doc+'.html'
#    with open(docf,'r',encoding='utf-8') as f: 
#        doc = f.read()
#    restsh = re.compile(r'<link rel="stylesheet" href="([^"]+)"\s+type="text/css"\s*/>')
#    recss = re.compile(r'@import url\("([^"]+)"\);')
#    docs = re.split(restsh,doc)
#    for i in range(1,len(docs),2):
#        relpth = docs[i]
#        csspfx = relpth.rsplit('/')[0]
#        fn = prefx + relpth
#        if fn.find('custom.css')>0:
#            docs[i] = "<style>\n"+thmstyle+"\n</style>";
#        else:
#            with open(fn,'r',encoding='utf-8') as f:
#                css = f.read()
#                csses = re.split(recss,css)
#                for j in range(1,len(csses),2):
#                    ffn = prefx+csspfx+'/'+csses[i]
#                    with open(ffn,'r',encoding='utf-8') as ff:
#                        csses[i] = ff.read()
#                css = "\n".join(csses)
#                docs[i] = "<style>\n"+css+"\n</style>"
#    doc = "\n".join(docs)
#    with open(docf,'w',encoding='utf-8') as f:
#        f.write(doc)

def setup(app):
    app.connect('build-finished', custom_css)

