from setuptools import find_packages, setup


def parse_requirements(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

# run via python setup.py install
setup(
    name='autoLinNote',
    version='0.1.0',
    description='Creates a transcript and summary of the watched learning materials/video so that there is enough freedom to focus on creative, non-linear note taking.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='René Lachmann',
    author_email='herr.rene.richter@gmail.com',
    url='https://github.com/renerichter/autoLinNote',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
