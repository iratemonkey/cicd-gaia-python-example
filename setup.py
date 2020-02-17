from setuptools import setup

setup(name='testpipeline',
      description='Gaia Basic Pipeline using Python',
      packages=['pipeline'],
      author='ruanbekker',
      author_email='ruan@ruanbekker.com',
      install_requires=[
            'gaiasdk>=0.0.16',
      ])
