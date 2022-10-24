from setuptools import setup

setup(
    name='futcordd',
    version='0.0.1',
    packages=['futcord'],
    url="https://github.com/ReetVF/Futcord",
    license='MIT',
    author='ReetVF',
    author_email='wollenils@gmail.com',
    description='Python Package from me',
    include_package_data=True,
    install_requires=[
        'colorama>=0.3.7',
        'multidict>=5.1.0'
    ]
)



