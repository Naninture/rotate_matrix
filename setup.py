from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 



setup(
  name='rotate_matrix',
  version='0.0.6',
  description='Rotate any matrix of any type, either clockwise or anti-clockwise instantly.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/Naninture/rotate_matrix.git',  
  download_url = 'https://github.com/Naninture/rotate_matrix/archive/0.0.6.tar.gz',
  author='Udipta/Naninture',
  author_email='uddipta2255@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['matrix','rotate matrix','rotate 2D array','rotate array','matrix rotation','2-D array rotation','rotate 2-D array','array rotation','2-D array rotation','rotation','clockwise','anticlockwise','clockwise rotation','anti-clockwise rotation'], 
  packages=find_packages(),
  install_requires=[''],
)
