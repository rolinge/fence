from setuptools import setup, find_packages

setup(
    name='fence',
    version='0.2.0',
    install_requires=[
        "oauth2client<4.0dev,>=2.0.0",
        "addict==2.1.1",
        "cirrus",
        "cdispyutils",
        "cryptography==2.1.2",
        "Flask==0.10.1",
        "Flask-CORS==3.0.3",
        "Flask_OAuthlib==0.9.4",
        "flask_postgres_session",
        "Flask_SQLAlchemy_Session==1.1",
        "google_api_python_client==1.6.4",
        "httplib2==0.10.3",
        "oauthlib==2.0.6",
        "pysftp==0.2.9",
        "pytest-flask==0.10.0",
        "pytest==3.2.3",
        "python_bcrypt==0.3.2",
        "python_dateutil==2.6.1",
        "PyJWT==1.5.3",
        "requests==2.18.4",
        "setuptools==36.6.0",
        "six==1.11.0",
        "SQLAlchemy==0.9.9",
        "temps==0.3.0",
        "userdatamodel",
        "Werkzeug==0.12.2",
        "storageclient",
        "pyyaml"
    ],
    dependency_links=[
        "git+https://github.com/uc-cdis/flask-postgres-session.git@68bf5a9723a351729855c429eca8a0f4bbb830c7#egg=flask_postgres_session-0.1.3",
        "git+https://github.com/uc-cdis/storage-client.git@0.1.5#egg=storageclient-0.1.4",
        "git+https://github.com/uc-cdis/userdatamodel.git@1.0.2#egg=userdatamodel",
        "git+https://github.com/uc-cdis/cdis-python-utils.git@0.2.1#egg=cdispyutils",
        "git+https://github.com/uc-cdis/cirrus.git@1a40b1518606d3963f6d40f8ac611fde1d95c814#egg=cirrus",
    ],
    scripts=[
        "bin/fence-create",
    ],
    packages=find_packages(),
)
