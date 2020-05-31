# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

is_release_build = os.environ.get('READTHEDOCS') == 'True'

project = 'Game Manual 0'
author = 'Game Manual 0 Contributors'

copyright_year = 2020

copyright = str(copyright_year) + ", " + str(author)

highlight_language = "java"

# The full version, including alpha/beta/rc tags
release = re.sub('^v', '', os.popen('git describe').read().strip())

# The short X.Y version
version = release



# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinx_sitemap'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'custom_sphinx_rtd_theme'
html_theme_path = ["_themes", ]
html_logo = "assets/gm0-logo.png"
html_favicon = "assets/gm0-logo.ico"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GameManual0Sitedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_logo = 'assets/gm0-logo.png'

latex_engine = 'xelatex'

latex_show_urls = 'footnote'

latex_show_pagerefs = True

latex_elements = {
    'releasename':"Game Manual 0",

    'papersize': 'letterpaper',

    'fontpkg': r'''
        \setmainfont{Roboto}
        \setsansfont{Roboto}
        \setmonofont{DejaVu Sans Mono}
    ''',

        'preamble': r'''
        \usepackage[titles]{tocloft}
        \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
        \setlength{\cftchapnumwidth}{0.75cm}
        \setlength{\cftsecindent}{\cftchapnumwidth}
        \setlength{\cftsecnumwidth}{1.25cm}
	''',

    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',

    'preamble': r'''
        \usepackage{datetime}

        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}

        \usepackage{placeins}

        \let\Oldsection\section
        \renewcommand{\section}{\FloatBarrier\Oldsection}

        \let\Oldsubsection\subsection
        \renewcommand{\subsection}{\FloatBarrier\Oldsubsection}

        \let\Oldsubsubsection\subsubsection
        \renewcommand{\subsubsection}{\FloatBarrier\Oldsubsubsection}
    ''',

    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{30mm} %%% * is used to give space from top

            \vspace{0mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=0.25]{gm0-logo.png}
            \end{figure}
            \begin{flushright}
                \textbf{\Huge {"Game Manual 0"}}
                \\
                \textbf{\Large {a guide for FTC teams\\enjoy!}}
            \end{flushright}

            \vspace{0mm}

            \vfill
            \small Published on : September, 2019

            \vspace*{0mm}
            \small  Last updated : \MonthYearFormat\today

        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \clearpage
        \pagenumbering{arabic}

    ''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GameManual0.tex', 'Game Manual 0',
     'Game Manual 0 Contributors', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gamemanual0', 'Game Manual 0',
     [author], 1)
]

linkcheck_ignore = ["https://workbench.grabcad.com/workbench/projects/*"]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GameManual0', 'Game Manual 0',
     author, 'GameManual0', 'A guide for FTC teams.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


def setup(app):
    app.add_stylesheet('css/gm0-rtd.css')

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = not is_release_build

# -- Options for imgmath extension -------------------------------------------

# Changes imgmath_image_format to svg (default png)
imgmath_image_format = 'svg'

rst_epilog = """
.. |gm0| replace:: Game Manual 0
.. |gm1| replace:: Game Manual Part 1
.. |gm2| replace:: Game Manual Part 2
.. |EN| replace:: Engineering Notebook
"""
