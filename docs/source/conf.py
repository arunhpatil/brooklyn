# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme
project = 'Brooklyn'
copyright = '2023, Arun H Patil and Marc K Halushka'
author = 'Arun H Patil and Marc K Halushka'
release = '0.0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark', 'sphinx_rtd_theme', 'nbsphinx']

source_suffix = {
                '.rst': 'restructuredtext',
                '.txt': 'markdown',
                '.md': 'markdown',
    }

language = 'python'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_static_path = ['_static']
html_context = {
                'display_github': True,
                'github_user': 'arunhpatil',
                'github_repo': 'brooklyn',
                'github_version': 'main/docs/source/',
    }
