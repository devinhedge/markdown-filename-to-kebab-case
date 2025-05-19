from setuptools import setup, find_packages

setup(
    name='markdown-filename-to-kebab-case',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to rename markdown files to kebab-case based on their H1 headers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/markdown-filename-to-kebab-case',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add any dependencies your project needs here
    ],
    entry_points={
        'console_scripts': [
            'convert-to-kebab-case=convert_to_kebab_case:main',
        ],
    },
)
