
.. toctree::
   :maxdepth: 2

.. include:: ../README.rst

----

.. theorem:: 

   Theorem without title.


The extension adds a

.. _`theorem1`:

.. theorem:: title of theorem
      :thmnode: thmnode
      :envname: envname
      :displayname: Satz
      :counter: 1

   This is a *theorem*.

.. lemma:: title of lemma

   This is a *lemma*.

.. corollary:: title of corollary

   This is a *corollary*.

.. proposition:: title of proposition

   This is a *proposition*.

.. conjecture:: title of conjecture

   This is a *conjecture*.

.. criterion:: title of criterion

   This is a *criterion*.

.. assertion:: title of assertion

   This is a *assertion*.

.. definition:: title of definition

   This is a *definition*.

.. condition:: title of condition

   This is a *condition*.

.. problem:: title of problem

   This is a *problem*.

.. example:: title of example

   This is a *example*.

.. exercise:: title of exercise

   This is a *exercise*.

.. algorithm:: title of algorithm

   This is a *algorithm*.

.. question:: title of question

   This is a *question*.

.. axiom:: title of axiom

   This is a *axiom*.

.. property:: title of property

   This is a *property*.

.. assumption:: title of assumption

   This is a *assumption*.

.. hypothesis:: title of hypothesis

   This is a *hypothesis*.

.. remark:: title of remark

   This is a *remark*.

.. notation:: title of notation

   This is a *notation*.

.. claim:: title of claim

   This is a *claim*.

.. summary:: title of summary

   This is a *summary*.

.. acknowledgment:: title of acknowledgment

   This is a *acknowledgment*.

.. case:: title of case

   This is a *case*.

.. conclusion:: title of conclusion

   This is a *conclusion*.

.. proof:: title of proof

   This is a *proof*.

.. theorem:: title of theorem

   This is a *theorem*.

.. lemma:: title of lemma

   This is a *lemma*.

.. corollary:: title of corollary

   This is a *corollary*.

.. proposition:: title of proposition

   This is a *proposition*.

.. conjecture:: title of conjecture

   This is a *conjecture*.

.. criterion:: title of criterion

   This is a *criterion*.

.. assertion:: title of assertion

   This is a *assertion*.

.. definition:: title of definition

   This is a *definition*.

.. condition:: title of condition

   This is a *condition*.

.. problem:: title of problem

   This is a *problem*.

.. example:: title of example

   This is a *example*.

.. exercise:: title of exercise

   This is a *exercise*.

.. algorithm:: title of algorithm

   This is a *algorithm*.

.. question:: title of question

   This is a *question*.

.. axiom:: title of axiom

   This is a *axiom*.

.. property:: title of property

   This is a *property*.

.. assumption:: title of assumption

   This is a *assumption*.

.. hypothesis:: title of hypothesis

   This is a *hypothesis*.

.. remark:: title of remark

   This is a *remark*.

.. notation:: title of notation

   This is a *notation*.

.. claim:: title of claim

   This is a *claim*.

.. summary:: title of summary

   This is a *summary*.

.. acknowledgment:: title of acknowledgment

   This is a *acknowledgment*.

.. case:: title of case

   This is a *case*.

.. conclusion:: title of conclusion

   This is a *conclusion*.

.. proof:: title of proof

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

   Use `:title:` if you want `:html_title:` and `:latex_title:` to be the same.  
   Replace ``instruction``. It is a mandatory argument. 
   Read the source in test/index.rst to understand this.
   In LaTex you must have ``newtheorem{instruction}{Instruction}``,
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

