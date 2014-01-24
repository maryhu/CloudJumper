#import sys
from cx_Freeze import setup, Executable


executables = [
    Executable('CloudJumper.py'

setup(
    name='Cloud Jumper',
      version='0.1.6',
      description='Doodle Jump clone',
      executables=executables
      )