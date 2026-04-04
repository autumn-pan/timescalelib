from setuptools import setup, find_packages

setup(
  name="timescalelib",
  version="0.1.0",
  packages=find_packages(),
  install_requires=["numpy", "scipy"],  
  python_requires=">=3.10",
  description="Time-Scale Calculus made simple.",
)