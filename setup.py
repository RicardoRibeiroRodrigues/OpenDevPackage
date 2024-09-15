from setuptools import setup

# which argument is for supported operating systems?
setup(
    name="dev_aberto_ricardorr",
    version="0.1",
    packages=["dev_aberto"],
    author="Ricardo Rodrigues",
    platforms=["Linux", "MacOS", "Windows"],
    install_requires=["requests", "Babel"],
    scripts=["scripts/hello.py"],
)
