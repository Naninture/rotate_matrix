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
  version='0.0.4',
  description='Rotate any matrix of any type, either clockwise or anti-clockwise instantly.',
  long_description= open('README.md').read(),
  url='https://github.com/Naninture/rotate_matrix.git',  
  download_url = 'https://github.com/Naninture/rotate_matrix/archive/0.0.2.tar.gz',
  author='Udipta/Naninture',
  author_email='uddipta2255@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['matrix','rotate matrix','rotate 2D array','rotate array'], 
  packages=find_packages(),
  install_requires=[''],
)
