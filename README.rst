
===========================================
Description of the Theorem Sphinx Extension
===========================================

This extension to `Sphinx <http://sphinx.pocoo.org/>`__ 
that adds directives mentioned in the latex 
`amsthm <http://mirror.easyname.at/ctan/macros/latex/required/amscls/doc/amsthdoc.pdf>`_
package: theorem, example, exercise,...and more.

----

:Version: 0.1
:Author: Roland Puntaier ``roland.puntaier@gmail.com``
:License: `BSD License <http://opensource.org/licenses/bsd-license.html>`__
:Git Repository: https://github.com/rpuntaie/sphinxcontrib-thm
:PyPI Package: http://pypi.python.org/pypi/sphinxcontrib-thm

Prerequisites and Configuration
===============================


This extension relies on software packages being installed on your computer:

- LaTeX with the ``amsthm`` package.

If you have installed the *thm* Sphinx extension e.g. using `PyPI
<http://pypi.python.org/pypi/sphinxcontrib-thm>`__, then you have to load the
extension in the Sphinx project configuration file ``conf.py`` by::

  extensions = ['sphinxcontrib.thm']

Usage
=====

The extension adds a

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


  You need to define these in ``conf.py`` via ``\newtheorem`` in the LATEX preamble. See below.

- *environment* directive::

    .. environment::
	:class: ENV_CLASS
	:name: Definition
	:html_title: title used by html builder
	:latex_title: title used by latex builder

  You can also use `:title:` if both `:html_title:` and `:latex_title:` should to be the same.  

- *textcolor* directive and role::

    .. textcolor:: #00FF00

            This text is green

    :textcolor:`<#FF0000> this text is red`.

  Roles are not recursive. They can only contain
  text, no other nodes. Directives are recursive, though.

- *endpar* directive::

    .. endpar::

  It puts r'\n\n' in LaTeX and <br> in html.
  There is no other way to end a paragraph between two environments.

- *align* directive::

    .. align:: center
    .. align:: left
    .. align:: flushleft
    .. align:: right
    .. align:: flushright

  Each of them has a separate numbering.


Here is an example `conf.py`:

.. literalinclude:: test/conf.py
   :language: python


