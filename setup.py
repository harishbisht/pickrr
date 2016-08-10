from setuptools import setup

setup(name='pickrr',
      version='0.4',
      description='Pickrr order placing, order Cancellation and order tracking api',
      url='http://github.com/harishbisht/pickrr',
      author='Harish Bisht',
      author_email='harish@pickrr.com',
      license='MIT',
      packages=['pickrr'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)