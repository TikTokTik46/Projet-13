# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# Path to the Python source files
import os
import sys
import sphinx_rtd_theme
import django

# Chemin vers le répertoire racine du projet Django
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, '..')
sys.path.insert(0, PROJECT_DIR)

# Configurez le module à utiliser pour Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

project = 'OC-Lettings'
copyright = '2023, Quentin Molières'
author = 'Quentin Molières'
release = '03/10/2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.autodoc',
              'sphinx_rtd_theme',
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'FR'

# Configuration for autodoc
autodoc_member_order = 'bysource'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
