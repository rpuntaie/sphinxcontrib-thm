
===========================================
Description of the Theorem Sphinx Extension
===========================================

This extension to `Sphinx <http://sphinx.pocoo.org/>`_ 
adds directives mentioned in the LaTeX 
`amsthm <http://mirror.easyname.at/ctan/macros/latex/required/amscls/doc/amsthdoc.pdf>`_
package: theorem, example, exercise,...and more.

Sphinx has no directive that would well fit such items.

For LaTeX these are translated to ``\begin{theorem}{title}`` and so on. 

----

:Version: 1.0
:Author: Roland Puntaier ``roland.puntaier@gmail.com``
:License: `BSD License <http://opensource.org/licenses/bsd-license.html>`_
:Git Repository: https://github.com/rpuntaie/sphinxcontrib-thm
:PyPI Package: http://pypi.python.org/pypi/sphinxcontrib-thm

Prerequisites and Configuration
===============================

This Sphinx extension must installed. Use::

  pip install sphinxcontrib-thm 

This takes it from `PyPI <http://pypi.python.org/pypi/sphinxcontrib-thm>`_.

To install it from the `github <https://github.com/rpuntaie/sphinxcontrib-thm>`_ repository::

  git clone https://github.com/rpuntaie/sphinxcontrib-thm
  cd sphinxcontrib-thm
  #don't use install here! It would produce a second sphinxcontrib folder
  python setup.py sdist 
  pip install dist/sphinxcontrib-thm*tar.gz

For LaTeX output ``amsthm`` (or ``ntheorem``) is needed.
For the example in the test folder also ``unicode-math`` is needed.

For HTML output ``sphinx.ext.mathjax`` should probably be in `conf.py`_,
because this extension is aimed at math authoring with Sphinx, 
but it is not a requirement.

You have to load the extension in `conf.py`_::

  extensions = ['sphinxcontrib.thm',``sphinx.ext.mathjax``,...]

Usage
=====

The extension adds 

- several directives mentioned in `amsthm <http://mirror.easyname.at/ctan/macros/latex/required/amscls/doc/amsthdoc.pdf>`_::

    .. theorem:: title
    .. lemma:: title
    .. corollary:: title
    .. proposition:: title
    .. conjecture:: title
    .. criterion:: title
    .. assertion:: title
    .. definition:: title
    .. condition:: title
    .. problem:: title
    .. example:: title
    .. exercise:: title
    .. algorithm:: title
    .. question:: title
    .. axiom:: title
    .. property:: title
    .. assumption:: title
    .. hypothesis:: title
    .. remark:: title
    .. notation:: title
    .. claim:: title
    .. summary:: title
    .. acknowledgment:: title
    .. case:: title
    .. conclusion:: title
    .. proof:: title


  For LaTeX you need to define these in `conf.py`_ via ``\newtheorem`` in the LaTeX preamble. See below__.

  While ``.. note::`` and others use ``\begin{sphinxadmonition}{title}``, these directives
  are translated to ``\begin{theorem}{title}`` and so on. 

__ `conf.py`_

- *environment* directive::

    .. environment:: instruction
	:name: Instruction
	:html_title: title used by html builder
	:latex_title: title used by LaTeX builder

  You can also use `:title:` if both `:html_title:` and `:latex_title:` should to be the same.  
  Replace ``instruction``. It is a mandatory argument. In LaTeX you must have ``newtheorem{instruction}{Instruction}``,
  unless it is an available LaTeX environment, like ``equation``.

- *textcolor* directive and role::

    .. textcolor:: #00FF00

            This text is green

    :textcolor:`<#FF0000> this text is red`.

  Roles are not recursive. They can only contain
  text, no other nodes. Directives are recursive, though.

- *align* directive::

    .. align:: center
    .. align:: left
    .. align:: flushleft
    .. align:: right
    .. align:: flushright

  Each of them has a separate numbering.

For refs use the normal sphinx refs like::

    .. _`theorem1`:

    .. theorem:: title

    Text here: By using backticks one can find the matching parts more easily in the editor.

    See `theorem1`_. 

In HTML one needs to provide formating via ``css``.
This can be done using `conf.py`_.

.. _`conf.py`:

Here is an example `conf.py`:

.. literalinclude:: ../test/conf.py
   :language: python


