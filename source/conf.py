# #!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# extensions = ['sphinx.ext.autodoc']

# # Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# # The suffix(es) of source filenames.
# # You can specify multiple suffix as a list of string:
# #
# # source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# # The master toctree document.
# master_doc = 'index'

# version = '0.1'
# release = '0.1'

# language = 'en'

# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# pygments_style = 'sphinx'

# todo_include_todos = False

# html_sidebars = {
#     '**': [
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#     ]
# }

project = 'Figure-Captioning with Human Feedback (FigCaps-HF)'
copyright = '2023, Anonymous'
author = 'Anonymous'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']
