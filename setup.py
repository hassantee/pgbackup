from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='pgbackup',
    version='0.1.0',
    author='Hassan Tariq',
    author_email='hassan.tariq@wholefoods.com',
    description='A utility for backing up the PostgreSQL databases',
    long_descrition=long_descrition,
    long_descrition_content_type='text/markdown',
    url='https://github.com/hassantee',
    packages=find_packages('src')
)
