from setuptools import setup, find_packages

setup(
  name="timescalelib",
  version="0.1.0",
  package_dir={"": "src"},
  packages=find_packages(where="src"),
  install_requires=["numpy", "scipy"],  
  python_requires=">=3.10",
  description="Time-Scale Calculus made simple.",
)
