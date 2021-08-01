from setuptools import setup

setup(
    name='GraphQLxFlask',
    version='0.1',
    long_description=__doc__,
    packages=['api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'ariadne', 'Flask-SQLAlchemy', 'Flask-Cors']
)