from setuptools import setup, find_packages

setup(
    name='Litter',
    version='0.1.0',
    packages=find_packages(),
    author='moisentinel, yukinotenshi',
    author_email='nibir@nibirsan.org, gabriel.bentara@gmail.com',
    license='MIT',
    url='https://github.com/moiSentineL/litter',
    install_requires=[
        'requests',
        'requests-toolbelt',
        'click'
    ],
    description='CLI tool to upload file to litterbox/catbox',
    keywords='direct upload cli',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': ['pyupload=pyupload.main:upload']
    }
)