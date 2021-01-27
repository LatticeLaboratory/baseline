import os.path

import setuptools

DIR = os.path.abspath(os.path.dirname(__file__))
requirements = open(os.path.join(DIR, 'requirements.txt')).read().splitlines()
version = open(os.path.join(DIR, 'starkware/cairo/lang/VERSION')).read().strip()
long_description = open('README.md', 'r', encoding='utf-8').read()

setuptools.setup(
    name='cairo-lang',
    version=version,
    author='Starkware',
    author_email='info@starkware.co',
    description='Compiler and runner for the Cairo language',
    install_requires=requirements,
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    setup_requires=['wheel'],
    url='https://cairo-lang.org/',
    package_data={
        'starkware.cairo.lang': ['VERSION'],
        'starkware.cairo.lang.compiler': ['cairo.ebnf'],
        'starkware.cairo.lang.tracer': ['*.html', '*.css', '*.js', '*.png'],
        'starkware.cairo.common': ['*.cairo'],
        'starkware.crypto.signature': ['pedersen_params.json'],
    },
    scripts=[
        'starkware/cairo/lang/scripts/cairo-format',
        'starkware/cairo/lang/scripts/cairo-compile',
        'starkware/cairo/lang/scripts/cairo-run',
        'starkware/cairo/lang/scripts/cairo-hash-program',
    ]
)
