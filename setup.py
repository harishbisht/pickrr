from setuptools import setup
import os
here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except:
    README = """\
pip install pickrr"""


setup(name='pickrr',
      version='0.4.1',
      description='Pickrr order placing, order Cancellation and order tracking api',
      long_description=README,
      url='http://github.com/harishbisht/pickrr',
      author='Harish Bisht',
      author_email='harish@pickrr.com',
      license='MIT',
      packages=['pickrr'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)