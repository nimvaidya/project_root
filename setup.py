from setuptools import setup

setup(
    name="pfr_package",
    version="0.0.1",
    description="pfr_package utilities",
    maintainer="Nimish Vaidya",
    maintainer_email="nvaidya@cmu.edu",
    license="MIT",
    packages=["pfr_package"],
    entry_points={"console_scripts": ["oa = pfr_package.main:main"]},
    long_description="""A long
      multiline description.""",
)
