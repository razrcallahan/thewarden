from setuptools import find_packages, setup

setup(
    name='The WARden',
    version='0.11',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
