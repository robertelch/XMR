from setuptools import setup, find_packages

setup(
    name='XRM',  # Change to your package name
    version='0.1.27',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4', 
        'lxml'# Add other external dependencies you use here
        # e.g. 'typing-extensions' if needed
    ],
    author='Crumbling',
    author_email='crumblingcookie666@gmail.com',
    description='Describe your package',
)

