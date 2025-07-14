# setup.py
from setuptools import setup
from Cython.Build import cythonize

plugin_sources = [
    "plugins_src/network_plugin.pyx",
    "plugins_src/auth_plugin.pyx",
    "plugins_src/db_plugin.pyx",
    "plugins_src/analysis_plugin.pyx"
]

setup(
    name="datalab_plugins",
    ext_modules=cythonize(plugin_sources, language_level="3"),
)
