# -*- coding: utf-8 -*-
#
# Processor SDK documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# pylint: disable=C0103

import sys
import os
import importlib
from datetime import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
rootdir = os.environ.get('ROOTDIR')
sys.path.insert(0, os.path.abspath(rootdir))

from scripts import interpretvalues, sectinc, replacevars

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx_rtd_theme',
    'sphinx_tabs.tabs',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# A dictionary mapping the file extensions (suffixes) of source files to their file types. Sphinx
# considers all files files with suffixes in source_suffix to be source files.
source_suffix = {
    '.rst': 'restructuredtext'
}

# The encoding of source files.
#source_encoding = 'utf-8-sig'
author = 'Texas Instruments Incorporated'
project_copyright = f"1995-{datetime.now().year} {author}, CC-BY-SA-4.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# The reST default role (used for this markup: `text`) to use for all
# documents.
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
highlight_language = 'text'
numfig = True

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = rootdir + '_static/img/ti_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = rootdir + '_static/img/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [rootdir + '_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html',
                         'searchbox.html'], }

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {'index': 'index.html'}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If True, the reStructuredText sources are included in the HTML build as _sources/docname.
html_copy_source = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
html_search_scorer = ''

# Read the Docs specific parameters for the "Edit on GitHub" button
html_context = {
    "display_github": True,
    "github_user": "texasinstruments",
    "github_repo": "processor-sdk-doc",
    "github_version": "master",
    "conf_py_path": "/source/",
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

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

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}

# Suppress warnings about excluded documents because every device gets a different toc tree
suppress_warnings = ['toc.excluded']

# -- Tag file loader ------------------------------------------------------

# Defaults
exclude_patterns = []

FAMILY = os.environ.get("DEVFAMILY", "")
OS = os.environ.get("OS", "")
try:
    globals().update(importlib.import_module(f"configs.{FAMILY}.{FAMILY}_{OS}_tags").__dict__)
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError("Configuration not supported!") from exc

# -- Family setup ---------------------------------------------------------

# List of Inclusion TOC files to use
family_tocfiles = [f"{FAMILY}/{FAMILY}_{OS}_toc.txt"]
# Family Configuration file to use
family_config_inputfile = f"{FAMILY}/{FAMILY}_{OS}_config.txt"

# Hash table for Replacement Variables and Config Values
family_replacevars, family_configvals = interpretvalues.read_familyvals(family_config_inputfile)

# Unpack replacement variables and place them in the preamble for all documents
rst_prolog = replacevars.unpack_replacevars(family_replacevars)
print(f'rst_prolog = """{rst_prolog}"""')

def setup(app):
    """
    Sphinx application entrypoint
    """

    # Load overrides
    app.add_css_file("css/theme_overrides.css")

    print("Build setup: Filled Replacement Variables (family_replacevars)"
            "and Configuration Values (family_configvals) hash tables")
    print("family_replacevars = ")
    print(family_replacevars)
    print("family_configvals = ")
    print(family_configvals)

    # Determine which sections need to be excluded
    sectinc.find_all_rst_files(app, exclude_patterns)
    sectinc.fill_docs_to_keep(app, family_tocfiles, 0)
    sectinc.set_excluded_docs(app, exclude_patterns)
    print(FAMILY + " exclude_patterns is:")
    print('[')
    for elem in exclude_patterns:
        print(elem)
    print(']')

    # Load family config values into application context
    for key, value in family_configvals.items():
        app.add_config_value(key, value, 'env')

    print("Device Family Build setup completed")
