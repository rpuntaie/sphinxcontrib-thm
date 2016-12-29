# -*- coding: utf-8 -*-

# Author: Roland Puntaier <roland.puntaier@gmail.com>
# Based on sphinx_latex by Marcin Szamotulski.

# Copyright (c) 2012-2015 by Roland Puntaier. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.

#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY ROLAND PUNTAIER ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL ROLAND PUNTAIER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of Roland Puntaier.


"""
sphinxcontrib.thm
~~~~~~~~~~~~~~~~~~~~~

Sphinx extension for directives mentioned in amsthm (theorem, example, exercise,...) and more.

*environment* directive::

    .. environment:: Theorem
        :title: Grothendick-Galois Theorem

        Let ...

*textcolor* directive and role::

    .. textcolor:: #00FF00

            This text is green

    :textcolor:`<#FF0000> this text is red`.

Roles are not recursive. They can only contain
text, no other nodes. Directives are recursive, though.

*align* directive::

    .. align:: center
    .. align:: left
    .. align:: flushleft
    .. align:: right
    .. align:: flushright

See README.rst file for details

"""

import tempfile
import shutil
import os
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from docutils import nodes

__all__ = [ 'newtheorem', 'EnvironmentDirective', 'AlignDirective', 'TextColorDirective', 'TheoremDirectiveFactory']


class TheoremException(Exception): pass

# EnvironmentDirective:
class environment(nodes.Element):
    pass

class EnvironmentDirective(Directive):

    required_arguments = 1
    optional_arguments = 0

    # final_argument_whitespace = True
    # directive arguments are white space separated.

    option_spec = {
                   'class': directives.class_option,
                   'name': directives.unchanged,
                   'title' : directives.unchanged,
                   'html_title' : directives.unchanged,
                   'latex_title' : directives.unchanged,
                   }

    has_content = True

    def run(self):

        self.options['envname'] = self.arguments[0]

        self.assert_has_content()
        environment_node = environment(rawsource='\n'.join(self.content), **self.options)
        self.state.nested_parse(self.content, self.content_offset, environment_node)
        self.add_name(environment_node)
        return [environment_node]

def visit_environment_latex(self, node):
    if 'latex_title' in node:
        self.body.append('\n\\begin{%s}[{%s}]' % (node['envname'], node['latex_title']))
    elif 'title' in node:
        self.body.append('\n\\begin{%s}[{%s}]' % (node['envname'], node['title']))
    else:
        self.body.append('\n\\begin{%s}' % (node['envname']))

def depart_environment_latex(self, node):
    self.body.append('\\end{%s}\n' % node['envname'])

def visit_environment_html(self, node):
    """
    This visit method produces the following html:

    The 'theorem' below will be substituted with node['envname'] and title with
    node['title'] (environment node's option).  Note that it differe slightly
    from how LaTeX works::

        <div class='environment theorem'>
            <div class='environment_title theorem_title'>title</div>
            <div class='environment_body theorem_body'>
              ...
            </div>
        </div>

    The title does not allow math roles.
    """
    if 'label' in node:
        ids = [ node['label'] ]
    else:
        ids = []
    self.body.append(self.starttag(node, 'div', CLASS='environment %s' % node['envname'], IDS = ids))
    self.body.append('<div class="environment_title %s_title">' % node['envname'])
    if 'html_title' in node:
        self.body.append(node['html_title'])
    if 'title' in node:
        self.body.append(node['title'])
    self.body.append('</div>')
    self.body.append('<div class="environment_body %s_body">' % node['envname'])
    self.set_first_last(node)

def depart_environment_html(self, node):
    self.body.append('</div>')
    self.body.append('</div>')

# AlignDirective:
class align(nodes.Element):
    pass

class AlignDirective(Directive):
    """
    *align* directive::

        .. align:: center
        .. align:: left
        .. align:: flushleft
        .. align:: right
        .. align:: flushright
    """

    required_arguments = 1
    optional_arguments = 0

    has_content = True

    def run(self):

        if self.arguments[0] in ('left', 'flushleft'):
            align_type = 'flushleft'
        elif self.arguments[0] in ('right', 'flushright'):
            align_type = 'flushright'
        else:
            align_type = 'center'
        self.options['align_type'] = align_type
        self.options['classes'] = directives.class_option(align_type)


        self.assert_has_content()
        align_node = align(rawsource='\n'.join(self.content), **self.options)
        self.state.nested_parse(self.content, self.content_offset, align_node)
        for node in align_node:
            node['classes'].extend(directives.class_option(align_type))
            if ('center' not in node['classes'] and
                    'flushleft' not in node['classes'] and
                    'flushright' not in node['classes'] ):
                node['classes'].extend(directives.class_option(align_type))
        return [align_node]

def visit_align_latex(self, node):
    self.body.append('\n\\begin{%s}' % node['align_type'])

def depart_align_latex(self, node):
    self.body.append('\\end{%s}\n' % node['align_type'])

def visit_align_html(self, node):
    self.body.append(self.starttag(node, 'p', CLASS=node['align_type']))

def depart_align_html(self, node):
    self.body.append('</p>')

# TextColorDirective:
class TextColorDirective(Directive):

    required_arguments = 1
    optional_arguments = 0

    has_content = True

    def run(self):

        self.assert_has_content()
        textcolor_node = textcolor(rawsource='\n'.join(self.content), **self.options)
        textcolor_node['color_spec'] = self.arguments[0]
        self.state.nested_parse(self.content, self.content_offset, textcolor_node)
        self.add_name(textcolor_node)
        return [textcolor_node]

class textcolor(nodes.Element):
    pass

def textcolor_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    The *textcolor* role is interpreted in the following way::

        :textcolor:`<color_spec> text `

    where color spec is in HTML model, e.g. #FFFFFF, ...

    In latex::

        \\textcolor[HTML]{color_spec}{text}

    The leading # is removed from color_spec in html::

        <font color="color_spec">text</font>
    """
    color_spec = text[1:text.index('>')]
    text = (text[text.index('>')+1:]).strip()
    textcolor_node = textcolor()
    textcolor_node.children.append(nodes.Text(text))
    textcolor_node['color_spec'] = color_spec

    return [textcolor_node], []

def visit_textcolor_html(self, node):
    self.body.append('<font color="%s">' % node['color_spec'])

def depart_textcolor_html(self, node):
    self.body.append('</font>')

def visit_textcolor_latex(self, node):
    color_spec = node['color_spec'][1:]
    self.body.append('\n\\textcolor[HTML]{%s}{' % color_spec)

def depart_textcolor_latex(self, node):
    self.body.append('}')

# TheoremDirectiveFactory:
def TheoremDirectiveFactory(thmname, thmcaption, thmnode, counter=None):
    """
    Function which returns a theorem class.

    Takes four arguments:
    thmname         - name of the directive
    thmcaption      - caption name to use
    thmnode         - node to write to
    counter         - counter name, if None do not count

    thmname='theorem', thmcaption='Theorem' will produce a directive::

        .. theorem:: theorem_title

            content

    Note that caption is only used in html.  
    
    The directive will produce:

    in LaTeX::

        \begin{theorem}[{theorem_title}] %  theorem_title will be put inside {}.
            content
        \end{theorem}

    in HTML::

        <div class='environment theorem'>
            <div class='environment_caption theorem_caption'>Theorem</div> <div class='environment_title theorem_title'>title</div>
            <div class='environment_body theorem_body'>
                content
            </div>
        </div>
    """
    class TheoremDirective(Directive):

        def __init__(self, *args, **kwargs):
            self.counter = Counter(counter)
            super(self.__class__, self).__init__(*args, **kwargs)

        required_arguments = 0
        optional_arguments = 1

        final_argument_whitespace = True
        # directive arguments are white space separated.

        option_spec = {
                    'class': directives.class_option,
                    'name': directives.unchanged,
                    }

        has_content = True

        def run(self):

            if counter:
                self.counter.stepcounter()
                self.options['counter'] = self.counter.value
            else:
                self.options['counter'] = ''

            self.options['thmname'] = thmname
            self.options['thmcaption'] = thmcaption
            if self.arguments:
                self.options['thmtitle'] = self.arguments[0]

            self.assert_has_content()
            node = thmnode(rawsource='\n'.join(self.content), **self.options)
            self.state.nested_parse(self.content, self.content_offset, node)
            self.add_name(node)
            return [node]

    return TheoremDirective

def visit_thm_latex(self, node):
    if 'thmtitle' in node:
        self.body.append('\n\\begin{%(thmname)s}[{%(thmtitle)s}]' % node)
    else:
        self.body.append('\n\\begin{%(thmname)s}' % node)

def depart_thm_latex(self, node):
    self.body.append('\\end{%(thmname)s}\n' % node)

def visit_thm_html(self, node):
    """
    This visit method produces the following html:

    The 'theorem' below will be substituted with node['envname'] and title with
    node['title'] (environment node's option).  Note that it differs slightly
    from how LaTeX works.

    For how it it constructed see the ``__doc__`` of TheoremDirectiveFactory.

    You cannot use math in the title.
    """
    if 'label' in node:
        ids = [ node['label'] ]
    else:
        ids = []

    self.body.append(self.starttag(node, 'div', CLASS='thm %(thmname)s' % node, IDS = ids))
    self.body.append('<div class="thm_caption %(thmname)s_caption">%(thmcaption)s<span class="thm_counter %(thmname)s_counter">%(counter)s</span>' % node)
    if 'thmtitle' in node:
        self.body.append('<span class="thm_title %(thmname)s_title"> %(thmtitle)s </span>' % node)
    self.body.append('</div>\n')
    self.body.append('<div class="thm_body %(thmname)s_body">' % node)
    self.set_first_last(node)

def depart_thm_html(self, node):
    self.body.append('</div>')
    self.body.append('</div>\n')

class Counter(object):
    """
    Base class for counters.  There is only one instance for a given name.

        >>> c=Counter('counter')
        >>> d=Counter('counter')
        >>> c id d
        True

    This is done using ``__new__`` method.
    """

    registered_counters = {}

    def __new__(cls, name, value=0, within=None):
        if name in cls.registered_counters:
            instance = cls.registered_counters[name]
            instance._init = False
            return instance
        else:
            instance = super(Counter, cls).__new__(cls)
            instance.name = name
            instance.value = value
            instance._init = True
            return instance

    def __init__(self, name, value=0, within=None):
        if not self._init:
            # __init__ once
            return
        self.name = name
        self.value = value

        self.register()

    def register(self):
        Counter.registered_counters[self.name] = self

    def stepcounter(self):
        self.value += 1

    def addtocounter(self, value=1):
        self.value += value

    def setcounter(self, value):
        self.value = value

    def __str__(self):
        return str(self.value) if self.name else ""

    def __unicode__(self):
        return str(self.value) if self.name else ""

class TheoremNode(nodes.Element):
    pass

# newtheorem:
def newtheorem(app, thmname, thmcaption, counter=None):
    """
    Add new theorem.  It is thought as an analog to latex::

        \\newtheorem{theorem_name}{caption}

    counter is an instance of Counter.  If None (the default),
    the constructed theorem will not be counted.
    """

    nodename = 'thmnode_%s' % thmname
    thmnode = type(nodename, (TheoremNode,), {})
    globals()[nodename]=thmnode # important for pickling
    app.add_node(thmnode,
                    html = (visit_thm_html, depart_thm_html),
                    latex = (visit_thm_latex, depart_thm_latex),
                )
    TheoremDirective = TheoremDirectiveFactory(thmname, thmcaption, thmnode, counter)
    app.add_directive(thmname, TheoremDirective)


# setup:
def setup(app):

    app.add_directive('environment', EnvironmentDirective)
    app.add_node(environment,
                html = (visit_environment_html, depart_environment_html),
                latex = (visit_environment_latex, depart_environment_latex),
            )

    app.add_directive('align', AlignDirective)
    app.add_node(align,
                html =  (visit_align_html, depart_align_html),
                latex = (visit_align_latex, depart_align_latex),
            )

    app.add_directive('textcolor', TextColorDirective)
    app.add_role('textcolor', textcolor_role)
    app.add_node(textcolor,
            html = (visit_textcolor_html, depart_textcolor_html),
            latex = (visit_textcolor_latex, depart_textcolor_latex)
            )

    # Add theorems from amsthm
    newtheorem(app,'theorem','Theorem','theorem')
    newtheorem(app,'lemma','Lemma','lemma')
    newtheorem(app,'corollary','Corollary','corollary')
    newtheorem(app,'proposition','Proposition','proposition')
    newtheorem(app,'conjecture','Conjecture','conjecture')
    newtheorem(app,'criterion','Criterion','criterion')
    newtheorem(app,'assertion','Assertion','assertion')
    newtheorem(app,'definition','Definition','definition')
    newtheorem(app,'condition','Condition','condition')
    newtheorem(app,'problem','Problem','problem')
    newtheorem(app,'example','Example','example')
    newtheorem(app,'exercise','Exercise','exercise')
    newtheorem(app,'algorithm','Algorithm','algorithm')
    newtheorem(app,'question','Question','question')
    newtheorem(app,'axiom','Axiom','axiom')
    newtheorem(app,'property','Property','property')
    newtheorem(app,'assumption','Assumption','assumption')
    newtheorem(app,'hypothesis','Hypothesis','hypothesis')
    newtheorem(app,'remark','Remark','remark')
    newtheorem(app,'notation','Notation','notation')
    newtheorem(app,'claim','Claim','claim')
    newtheorem(app,'summary','Summary','summary')
    newtheorem(app,'acknowledgment','Acknowledgment','acknowledgment')
    newtheorem(app,'case','Case','case')
    newtheorem(app,'conclusion','Conclusion','conclusion')
    newtheorem(app,'proof','Proof','proof')


# test if there is no global name which starts with 'thmnode_', 
# these names are reserved for thmnodes (newtheorem()).
for name in globals().copy():
    if name.startswith('thmnode_'):
        raise TheoremException('Theorem Internal Error: "%s" in globals()' % name)


    
