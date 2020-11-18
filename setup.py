from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='rotate_matrix',
  version='0.0.2',
  description='Rotate any matrix of any type, either clockwise or anti-clockwise instantly.',
  long_description='''ROTATE MATRIX:

Rotate any matrix of any type, either clockwise or anti-clockwise instantly. 

Contains two functions:

1) clockwise: Takes l as parameter which is of type list, and pases the clockwised rotated version list l.

2) anti-clockwise: Takes l as parameter which is of type list, and passes the anti-clockwise rotated version of list l.

''',
  url='',  
  author='Udipta/Naninture',
  author_email='uddipta2255@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='rotate matrix', 
  packages=find_packages(),
  install_requires=[''],
)