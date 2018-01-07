from setuptools import setup

setup(
   name='rwutility',
   version='1.0',
   description='Simple little package for control of terminal input and output',
   author='Rasmus Westerlin',
   author_email='rasmuswesterlin@gmail.com',
   packages=['rwutility'],  #same as name
   install_requires=['os', 'sys','termios','platform','subprocess','tty','msvcrt'], #external packages as dependencies
)