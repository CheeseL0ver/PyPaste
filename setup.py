from setuptools import setup

setup(
        name = 'Pypaste',
        version = '0.0.1',
        packages = ['pypaste'],
        entry_points = {
            'console_scripts': [
                'pypaste = pypaste.__main__:main'
                ],
            },
        install_requires = ['requests']
        )
