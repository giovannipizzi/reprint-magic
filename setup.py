import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

modulename = 'reprint_magic'
the_license = "The MIT license"

# Get the version number in a dirty way
folder = os.path.split(os.path.abspath(__file__))[0]
fname = os.path.join(folder, modulename, '__init__.py')
with open(fname) as init:
    ns = {}
    # Get lines that match, remove comment part
    # (assuming it's not in the string...)
    versionlines = [
        l.partition('#')[0]
        for l in init.readlines()
        if l.startswith('__version__')
    ]
if len(versionlines) != 1:
    raise ValueError("Unable to detect the version lines")
versionline = versionlines[0]
version = versionline.partition('=')[2].replace('"', '').strip()

setup(
    name=modulename,
    description=
    "A module that registers and defines a jupyter ipython magic to run and reprint on output the code",
    url='http://github.com/giovannipizzi/reprint-magic',
    license=the_license,
    author='Giovanni Pizzi',
    version=version,
    # Abstract dependencies.  Concrete versions are listed in
    # requirements.txt
    # See https://caremad.io/2013/07/setup-vs-requirement/ for an explanation
    # of the difference and
    # http://blog.miguelgrinberg.com/post/the-package-dependency-blues
    # for a useful dicussion
    install_requires=[
        'IPython'
    ],
    packages=find_packages(),
    # Needed to include some static files declared in MANIFEST.in
    download_url='https://github.com/giovannipizzi/reprint-magic/archive/v{}.tar.gz'.
    format(version),
    keywords=[
        'jupyter', 'ipython', 'magic', 'reprint', 'appmode'
    ],
    long_description=open(os.path.join(folder, 'README.rst')).read(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: IPython"
    ],
)
