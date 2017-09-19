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

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.transforms import SphinxTransform

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
    node['title'] (environment node's option).  Note that it differs slightly
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
    textcolor_node.append(nodes.Text(text))
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

def TheoremDirectiveFactory(thmnode, envname, displayname, counter=None):
    """
    Function which returns a theorem class.

    Takes four arguments:
    thmnode         - node to insert in document tree
    envname         - name to use in source: rst directive, html classes and latex environment
    displayname     - name to display in output
    counter         - counter name (if enumerated)

    Given (envname,displayname,counter) = ('theorem','Satz',None) 
    will produce a directive to be used as::

        .. theorem:: TITLE

            CONTENT

    to produce in LaTeX::

        \begin{theorem}[TITLE]
            CONTENT
        \end{theorem}

    and in HTML::

        <div class='thm theorem'>
            <div class='thm_caption theorem_caption'>Satz <span class='thm_title theorem_title'>TITLE</span></div>
            <div class='thm_body theorem_body'>
                CONTENT
            </div>
        </div>

    Note that the latex environment is independent of the displayname 
    (name in output is controlled by LaTeX preamble), but that :numref: 
    references to it nevertheless still depends on displayname.
    """
    class TheoremDirective(Directive):

        # Accept one optional argument (whitespaces allowed) and content
        required_arguments = 0
        optional_arguments = 1
        final_argument_whitespace = True
        has_content = True

        def run(self):
            self.options['envname'] = envname
            self.options['displayname'] = displayname
            if counter:
                self.options['counter'] = counter
            if self.arguments:
                self.options['title'] = self.arguments[0]

            self.assert_has_content()
            node = thmnode(rawsource='\n'.join(self.content), **self.options)
            self.state.nested_parse(self.content, self.content_offset, node)
            return [node]

    return TheoremDirective

def visit_thm_latex(self, node):
    if 'title' in node:
        self.body.append('\n\\begin{%(envname)s}[{%(title)s}]' % node)
    else:
        self.body.append('\n\\begin{%(envname)s}' % node)

    # Node-registered and pending labels
    ids = set(node['ids'])
    if 'counter' in node:
        ids |= {id for id in self.pop_hyperlink_ids( node['counter'] )}
    if ids:
        labels = ''.join(self.hypertarget(id, anchor=False) for id in sorted(ids))
        self.body.append('\n' + labels)

def depart_thm_latex(self, node):
    self.body.append('\\end{%(envname)s}\n' % node)

def visit_thm_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='thm %(envname)s' % node))

    # Caption
    self.body.append('<div class="thm_caption %(envname)s_caption">' % node)
    env = self.builder.env
    std = env.get_domain('std')
    if std.is_enumerable_node(node):
        if env.config.numfig:
            self.add_fignumber(node)
        elif not env.config.thm_no_displayname:
            figtype = std.get_figtype(node)
            self.body.append('<span class="caption-number">')
            prefix = self.builder.config.numfig_format.get(figtype)
            self.body.append(prefix % '' + ' ')
            self.body.append('</span>')
    elif not env.config.thm_no_displayname:
        self.body.append('%(displayname)s' % node)
    if 'title' in node:
        self.body.append('<span class="thm_title %(envname)s_title"> %(title)s </span>' % node)
    self.body.append('</div>\n')

    # Body
    self.body.append('<div class="thm_body %(envname)s_body">' % node)

def depart_thm_html(self, node):
    self.body.append('</div>')
    self.body.append('</div>\n')

class TheoremNode(nodes.Element):
    pass

def get_thmnode_title(thmnode):
    return thmnode.get('title',None)

def newtheorem(app, envname, displayname, counter=None):
    """
    Add new theorem.  It is thought as an analog to latex::
        \\newtheorem{envname}[counter]{displayname}

    If the counter is None (the default),
    the constructed theorem will not be counted.
    """

    clsname = 'thmnode_%s' % envname
    thmnode = type(clsname, (TheoremNode,), {})
    globals()[clsname]=thmnode # important for pickling

    if counter:
        if app.config.thm_no_displayname:
            app.config.numfig_format.setdefault(envname, '%s')
        else:
            app.config.numfig_format.setdefault(envname, displayname+' %s')
        app.add_enumerable_node(thmnode, counter, get_thmnode_title,
            html = (visit_thm_html, depart_thm_html),
            latex = (visit_thm_latex, depart_thm_latex))
    else:
        app.add_node(thmnode, 
                        html = (visit_thm_html, depart_thm_html),
                        latex = (visit_thm_latex, depart_thm_latex))

    TheoremDirective = TheoremDirectiveFactory(thmnode, envname, displayname, counter)
    app.add_directive(envname, TheoremDirective)

class TheoremAutoNumbering(SphinxTransform):
    """
    Register nonempty IDs of enumerable nodes 
    (for some reason sphinx/transforms/__init__.py skips nodes without title
    making LaTeX and HTML theorem numbering different)
    """
    default_priority = 210

    def apply(self):
        # type: () -> None
        domain = self.env.get_domain('std')  # type: StandardDomain

        for node in self.document.traverse(TheoremNode):
            if domain.is_enumerable_node(node):
                self.document.note_implicit_target(node)


def install_extension(app):
    if app.config['thm_use_environment']:
        app.add_directive('environment', EnvironmentDirective)
        app.add_node(environment,
            html = (visit_environment_html, depart_environment_html),
            latex = (visit_environment_latex, depart_environment_latex))

    if app.config['thm_use_align']:
        app.add_directive('align', AlignDirective)
        app.add_node(align,
            html = (visit_align_html, depart_align_html),
            latex = (visit_align_latex, depart_align_latex))

    if app.config['thm_use_textcolor']:
        app.add_directive('textcolor', TextColorDirective)
        app.add_role('textcolor', textcolor_role)
        app.add_node(textcolor,
            html = (visit_textcolor_html, depart_textcolor_html),
            latex = (visit_textcolor_latex, depart_textcolor_latex))

    for t in app.config['thm_theorems']:
        newtheorem(app, *t)


def setup(app):
    app.add_config_value('thm_use_environment', False, 'env')
    app.add_config_value('thm_use_textcolor', False, 'env')
    app.add_config_value('thm_use_align', False, 'env')
    app.add_config_value('thm_no_displayname', False, 'env')
    app.add_config_value('thm_theorems', [], 'env')
    app.connect('builder-inited', install_extension)
    app.add_transform(TheoremAutoNumbering)
    return {'version':'1.2'}

    ############################
    # conf.py example setting
    ############################
    # thm_use_environment = True
    # thm_use_textcolor = True
    # thm_use_align = True
    # thm_no_displayname = True
    # thm_theorems = [
    #     ('theorem','Theorem','theorem'),
    #     ('lemma','Lemma','lemma'),
    #     ('corollary','Corollary','corollary'),
    #     ('proposition','Proposition','proposition'),
    #     ('conjecture','Conjecture','conjecture'),
    #     ('criterion','Criterion','criterion'),
    #     ('assertion','Assertion','assertion'),
    #     ('definition','Definition','definition'),
    #     ('condition','Condition','condition'),
    #     ('problem','Problem','problem'),
    #     ('example','Example','example'),
    #     ('exercise','Exercise','exercise'),
    #     ('algorithm','Algorithm','algorithm'),
    #     ('question','Question','question'),
    #     ('axiom','Axiom','axiom'),
    #     ('property','Property','property'),
    #     ('assumption','Assumption','assumption'),
    #     ('hypothesis','Hypothesis','hypothesis'),
    #     ('remark','Remark','remark'),
    #     ('notation','Notation','notation'),
    #     ('claim','Claim','claim'),
    #     ('summary','Summary','summary'),
    #     ('acknowledgment','Acknowledgment','acknowledgment'),
    #     ('case','Case','case'),
    #     ('conclusion','Conclusion','conclusion'),
    #     ('proof','Proof')
    # ]
    


# test if there is no global name which starts with 'thmnode_', 
# these names are reserved for thmnodes (newtheorem()).
for name in globals().copy():
    if name.startswith('thmnode_'):
        raise TheoremException('Theorem Internal Error: "%s" in globals()' % name)


    
