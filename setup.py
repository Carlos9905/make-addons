from setuptools import find_packages, setup

setup(
    name='scaffold-custom',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'tqdm==4.65.0',
    ],
    entry_points={
        'console_scripts': [
            #nombre del comando: Nombre del paquete.Nombre del módulo
            'create-addons = scaffold-custom.cli:main'
        ]
    }
)
