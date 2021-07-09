from setuptools import setup

setup(name='types-portage',
      version='0.0.1',
      description='Typing stubs for Portage',
      long_description='',
      url='https://github.com/Tatsh/types-portage',
      packages=['portage-stubs'],
      package_data={'portage-stubs': ['__init__.pyi', 'versions.pyi', 'METADATA.toml']},
      license='MIT',
      classifiers=['Typing :: Typed'],
)
