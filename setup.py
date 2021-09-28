# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'readme.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'nr.parsing.core >=2.0.2,<3.0.0',
  'nr.pylang.ast >=0.0.5,<0.1.0',
  'dataclasses >=0.6.0,<1.0.0',
  'nr.functional >=0.1.0,<1.0.0',
]
test_requirements = [
  'astor',
  'types-termcolor',
]
extras_require = {}
extras_require['colors'] = [
  'termcolor >=1.1.0,<2.0.0',
]
extras_require['codegen'] = [
  'astor >=0.8.1,<1.0.0',
]
extras_require['test'] = test_requirements

setuptools.setup(
  name = 'craftr-dsl',
  version = '0.5.0',
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'Parser and transpiler for the Craftr DSL.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/craftr-build/craftr-dsl',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = extras_require,
  tests_require = test_requirements,
  python_requires = '>=3.8.0,<4.0.0',
  data_files = [],
  entry_points = {},
  cmdclass = {},
  keywords = [],
  classifiers = [],
  zip_safe = False,
)
