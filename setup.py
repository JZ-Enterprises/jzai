from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jzai',
    version='59.84.01',
    author="Zack Allen",
    author_email='zjacka01@sfx.act.edu.au',
    packages=find_packages(),
    url='https://github.com/JZ-Enterprises/jzai/',
    install_requires=[
        'nltk',
        'textblob',
        'click',
        'requests',
        'setuptools',
        'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'jzai=jzai.cli:run',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    description="Next Gen AI Bot",
    keywords=["AI", "Bot", "GPT"],
        classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license="MIT"
)
