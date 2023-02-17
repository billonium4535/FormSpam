from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Spam google forms'
LONG_DESCRIPTION = 'This is a package to spam google forms with responses'

setup(
        name="GoogleFormSpam",
        version=VERSION,
        author="Joe",
        author_email="alex.riddell88@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'Google'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)
