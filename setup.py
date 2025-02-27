from setuptools import setup, find_packages
setup(
 name='how_long',
 version='1.0.3',
 packages=find_packages(),
 install_requires=[
     'opencv-python',
     'loguru',
 ],
 entry_points={
     'console_scripts':[
         'how-long = how_long:run'
     ],
 },
 author='matin1099',
 )