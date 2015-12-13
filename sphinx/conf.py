# -*- coding: utf-8 -*-
#
# BurnMan documentation build configuration file, created by
# sphinx-quickstart on Mon Apr 21 16:47:58 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

sys.path.insert(0, os.path.abspath('..'))
import burnman
import burnman.version

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'sphinx.ext.mathjax',
              'numpydoc', 'sphinx.ext.intersphinx', 'sphinx.ext.ifconfig', 'sphinx.ext.inheritance_diagram',
              'sphinx.ext.viewcode','sphinxcontrib.bibtex']
numpydoc_show_class_members = False

autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance', 'inherited-members']
autodoc_member_order = 'bysource'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'BurnMan'
copyright = u'2014, Sanne Cottaar, Timo Heister, Robert Myhill, Ian Rose, Cayman Unterborn'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = burnman.version.short_version
# The full version, including alpha/beta/rc tags.
release = burnman.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'BurnMandoc'


# -- Options for LaTeX output --------------------------------------------------

preamble1 = '''
\\newcommand{{\\burnmanversion}}{{{0}}}
'''.format(release)
preamble = preamble1 + r'''
\usepackage{textpos}

\newcommand{\burnman}{\texttt{\bf BurnMan}}

\renewcommand{\maketitle}{

\definecolor{dark_grey}{gray}{0.3}
\definecolor{aspect_blue}{rgb}{0.9,0.35,0.3}

%LINE 1%
{
\renewcommand{\familydefault}{\sfdefault}

\pagenumbering{gobble}
\begin{center}
\resizebox{\textwidth}{!}{\textcolor{dark_grey}{\fontfamily{\sfdefault}\selectfont
COMPUTATIONAL INFRASTRUCTURE FOR GEODYNAMICS (CIG)
}}

\hrule

%LINE 2%
\color{dark_grey}
\rule{\textwidth}{2pt}

%LINE 3%
\color{dark_grey}
% FILL: additional organizations
% e.g.: {\Large Organization 1\\Organization 2}
{\Large }
\end{center}

%COLOR AND CODENAME BLOCK%
\begin{center}
\resizebox{\textwidth}{!}{\colorbox
% FILL: color of code name text box
% e.g. blue
{aspect_blue}{\fontfamily{\rmdefault}\selectfont \textcolor{white} {
% FILL: name of the code
% You may want to add \hspace to both sides of the codename to better center it, such as:
% \newcommand{\codename}{\hspace{0.1in}CodeName\hspace{0.1in}}
\hspace{0.1in}\burnman{}\hspace{0.1in}
}}}
\\[12pt]
{\Large a thermodynamics and thermoelasticity toolkit}
\end{center}

%MAIN PICTURE%
\begin{textblock*}{5.in}(0.3in,0.3in)
% FILL: image height
% e.g. height=6.5in
\begin{center}
\vspace{.5in}
\includegraphics[height=4.5in]{../../burnjack-small.png}
% FILL: image file name
% e.g. cover_image.png
\end{center}
\end{textblock*}

%USER MANUAL%
\color{dark_grey}
\hfill{\Huge \fontfamily{\sfdefault}\selectfont User Manual \\
% FILL: manual version
% e.g. 1.0
\raggedleft \huge \fontfamily{\sfdefault}\selectfont Version {\burnmanversion}\\
%\\\large(generated from subversion: $Revision: 2568 $)\\
}

%AUTHOR(S) & WEBSITE%
\null
\vfill
\color{dark_grey}
\Large \hfill {\raggedleft \fontfamily{\sfdefault}\selectfont
% FILL: author list
% e.g. Author One\\Author Two\\Author Three\\
% be sure to have a newline (\\) after the final author
Sanne Cottaar\\Timo Heister\\Robert Myhill\\Ian Rose\\Cayman Unterborn\\
}

{\fontfamily{\sfdefault}\selectfont \href{http://geodynamics.org}{http://geodynamics.org}}


%LINE%
\color{dark_grey}
\rule{\textwidth}{2pt}

}

\pagebreak
}
  '''

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',
    'babel': '\usepackage[english]{babel}',
# The font size ('10pt', '11pt' or '12pt').
'pointsize': '11pt',
'classoptions': ',openany',
'preamble': preamble
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'BurnMan.tex', u'BurnMan Documentation',
   u'Sanne Cottaar, Timo Heister, Robert Myhill, Ian Rose, Cayman Unterborn', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'burnman', u'BurnMan Documentation',
     [u'Sanne Cottaar, Timo Heister, Robert Myhill, Ian rose, Cayman Unterborn'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'BurnMan', u'BurnMan Documentation',
   u'Sanne Cottaar, Timo Heister, Robert Myhill, Ian rose, Cayman Unterborn', 'BurnMan', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
