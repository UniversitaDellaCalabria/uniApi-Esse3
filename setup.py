from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='uniApiesse3',
      version='0.3',
      description="Custom interface to Cineca Esse3 API",
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python :: 3'],
      url='https://github.com/UniversitaDellaCalabria/uniApi-Esse3',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='BSD',
      scripts=['unie3api/unie3api.py'],
      packages=['unie3api'],
      install_requires=[
                      'requests'
                  ],
     )
