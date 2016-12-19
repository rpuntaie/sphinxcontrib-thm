# -*- coding: utf-8 -*-

DESCRIPTION      = 'Sphinx extension for directives mentioned in amsthm (theorem, example, exercise,...) and more'
LONG_DESCRIPTION = DESCRIPTION
NAME             = 'sphinxcontrib-thm'
VERSION          = '0.1'
AUTHOR           = 'Marcin Szamotulski, Roland Puntaier'
AUTHOR_EMAIL     = 'coot@riseup.net, roland.puntaier@gmail.com'
URL              = 'https://www.github.com/rpuntaie/sphinxcontrib-thm',
DOWNLOAD         = 'http://pypi.python.org/pypi/sphinxcontrib-thm'
LICENSE          = 'BSD'
REQUIRES         = ['Sphinx']
CLASSIFIERS      = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Topic :: Documentation',
    'Topic :: Utilities',
    ]

if __name__ == "__main__":

    from setuptools import setup, find_packages
    import sys

    setup(
        name=NAME,
        version=VERSION,
        url=URL,
        download_url=DOWNLOAD,
        license=LICENSE,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        zip_safe=False,
        classifiers=CLASSIFIERS,
        platforms='any',
        packages=find_packages(),
        include_package_data=True,
        install_requires=REQUIRES,
        namespace_packages=['sphinxcontrib']
        )

