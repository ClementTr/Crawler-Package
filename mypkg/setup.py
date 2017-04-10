from setuptools import find_packages
from setuptools import setup


setup(name='mypkg',
  #setup_requires=['setuptools_scm'],
  #use_scm_version={'write_to': 'mypkg/version.txt'},
  version = "1.0",    
  description="My Python package",
  packages=find_packages(),
  test_suite = 'tests',
  # include_package_data: to install data from MANIFEST.in
  include_package_data=True,
  scripts=['scripts/mypkg-run'],
  zip_safe=False)
