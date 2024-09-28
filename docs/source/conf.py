# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Arcane Engine"
copyright = "2024, Arcane Engineering"
author = "Marco Lamina"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_material"
html_static_path = ["_static"]
html_theme_options = {
    "base_url": "https://docs.arcane.engineer",
    "repo_url": "https://github.com/arc-eng/engine",
    "repo_name": "Arcane Engine",
    "color_primary": "white",
    "color_accent": "blue",
    "html_minify": True,
    "css_minify": True,
    "nav_title": "Arcane Engine",
    "google_analytics_account": "G-86FJ02W45S",
    "logo_icon": "⚙️",
    "globaltoc_depth": 1,
    "master_doc": False,
    "nav_links": [
        {
            "href": "https://arcane.engineer/",
            "internal": False,
            "title": "About Us",
        },
        {
            "href": "https://arcane.engineer/dashboard/tasks/",
            "internal": False,
            "title": "Dashboard",
        },
        {
            "href": "https://arcane.engineer/development-kit/",
            "internal": False,
            "title": "Dev Kit",
        },
        {
            "href": "https://arcane.engineer/studio/",
            "internal": False,
            "title": "Arcane Studio",
        },
    ],
    "heroes": {
        "index": "Boosting developer productivity with smart automation.",
    },
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
