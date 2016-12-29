
.. toctree::
   :maxdepth: 2

.. include:: ../README.rst

----

.. theorem:: 

   Theorem without title.


The extension adds a

.. _`theorem1`:

.. theorem:: title

   This is a *theorem*.

.. lemma:: title

   This is a *lemma*.

.. corollary:: title

   This is a *corollary*.

.. proposition:: title

   This is a *proposition*.

.. conjecture:: title

   This is a *conjecture*.

.. criterion:: title

   This is a *criterion*.

.. assertion:: title

   This is a *assertion*.

.. definition:: title

   This is a *definition*.

.. condition:: title

   This is a *condition*.

.. problem:: title

   This is a *problem*.

.. example:: title

   This is a *example*.

.. exercise:: title

   This is a *exercise*.

.. algorithm:: title

   This is a *algorithm*.

.. question:: title

   This is a *question*.

.. axiom:: title

   This is a *axiom*.

.. property:: title

   This is a *property*.

.. assumption:: title

   This is a *assumption*.

.. hypothesis:: title

   This is a *hypothesis*.

.. remark:: title

   This is a *remark*.

.. notation:: title

   This is a *notation*.

.. claim:: title

   This is a *claim*.

.. summary:: title

   This is a *summary*.

.. acknowledgment:: title

   This is a *acknowledgment*.

.. case:: title

   This is a *case*.

.. conclusion:: title

   This is a *conclusion*.

.. proof:: title

   This is a *proof*.

.. theorem:: title

   This is a *theorem*.

.. lemma:: title

   This is a *lemma*.

.. corollary:: title

   This is a *corollary*.

.. proposition:: title

   This is a *proposition*.

.. conjecture:: title

   This is a *conjecture*.

.. criterion:: title

   This is a *criterion*.

.. assertion:: title

   This is a *assertion*.

.. definition:: title

   This is a *definition*.

.. condition:: title

   This is a *condition*.

.. problem:: title

   This is a *problem*.

.. example:: title

   This is a *example*.

.. exercise:: title

   This is a *exercise*.

.. algorithm:: title

   This is a *algorithm*.

.. question:: title

   This is a *question*.

.. axiom:: title

   This is a *axiom*.

.. property:: title

   This is a *property*.

.. assumption:: title

   This is a *assumption*.

.. hypothesis:: title

   This is a *hypothesis*.

.. remark:: title

   This is a *remark*.

.. notation:: title

   This is a *notation*.

.. claim:: title

   This is a *claim*.

.. summary:: title

   This is a *summary*.

.. acknowledgment:: title

   This is a *acknowledgment*.

.. case:: title

   This is a *case*.


.. conclusion:: title

   This is a *conclusion*.

.. proof:: title

   This is a *proof*.

   These classical Maxwell equations are written with unicode and converted by ``unicode-math`` for LaTex and 
   by ``mathjax`` for HTML.

   .. math::

       ∇ × E = −∂B/∂t   \\
       ∇ × H = J+ ∂D/∂t \\
       ∇ · D = ρ        \\
       ∇ · B = 0        \\
       D = εE           \\
       B = μH          


.. environment:: instruction
   :name: Instruction
   :html_title: title used by html builder
   :latex_title: title used by latex builder

   You can also use `:title:` if both `:html_title:` and `:latex_title:` should to be the same.  
   Replace ``instruction``. It is a mandatory argument. In latex you must have ``newtheorem{instruction}{Instruction}``,
   unless it is an available LaTeX environment, like ``equation``.

.. align:: center

   align is center

.. align:: left

   align is left

.. align:: flushleft

   align is flushleft

.. align:: right

   align is right

.. align:: flushright

   align is flushright

.. textcolor:: #00FF00

   This text is green

Some text here is different: :textcolor:`<#FF0000> this text is red` and this is not.


For refs use the normal sphinx refs like: see `theorem1`_.

In HTML one needs to provide formating via ``css``::
This can be done using ``conf.py``. See `conf.py`_.

