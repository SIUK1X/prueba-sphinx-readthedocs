import os 
import sys
sys.path.insert(0, os.path.abspath('../..'))


project = 'Prueba'
copyright = '2025, Roy J'
author = 'Roy J'
release = '0.0.1'

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              ]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Para incluir módulos
#napoleon_google_docstring = True
#napoleon_numpy_docstring = True

