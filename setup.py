import setuptools

setuptools.setup(
    name='write1',
    version='2024.03.01',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
