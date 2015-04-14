import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='perpetualfailure',
    version='0.0',
    description='perpetualfailure',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='perpetualfailure',

    entry_points="""\
    [paste.app_factory]
    main = perpetualfailure:main
    [console_scripts]
    initialize_perpetualfailure_db = perpetualfailure.scripts.initializedb:main
    """,

    install_requires=[
        'pyramid>=1.5.1',
        'pyramid_chameleon',
        'pyramid_debugtoolbar',
        'pyramid_tm',
        'transaction',
        'zope.sqlalchemy>=0.7.5',
        'waitress',
        # Perpetual Failure-specific dependencies
        'Markdown>=2.6.1',
        'SQLAlchemy>=0.9.8',
        'bleach>=1.4',
        'pyramid-mako>=1.0.2',
        'pyramid-scss>=0.4',
        'passlib>=1.6.2',
        'pyramid-beaker>=0.8',
        # Should be made into optional dependencies
        'psycopg2>=2.5.4',
        'py-bcrypt>=0.4',
    ],
)
