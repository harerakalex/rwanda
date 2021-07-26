from setuptools import setup, find_packages

with open('README.md') as _readme_file:
    readme = _readme_file.read()

tests_require = ['pytest']

setup(
    name='rwanda',
    url='https://github.com/harerakalex/rwanda',
    version='0.0.1',
    author='Harerimana Carlos',
    author_email='hareraloston@gmail.com',
    maintainer='',
    keywords='rwanda, urwanda, intara, u rwanda, imirenge, utugari, imidugudu',
    license='Apache Software License',
    description=(
        "This python package that returns provinces, districts, sectors, villages and cells found in Rwanda."
    ),
    long_description=readme,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'six >= 1.10, < 2',
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'email': ['idna >= 2.0.0']
    },
    packages=find_packages(include="*"),
    package_data={
        '': ['*.pyi', 'py.typed'],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    test_suite='rwanda.tests.suite',
)