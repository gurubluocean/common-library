from setuptools import setup

setup(
    name='s3datacleaner',
    version='0.1.0',    
    description='A example Python package',
    license='MIT',
    packages=['s3datacleaner'],
    install_requires=[
      'pandas==1.3.5',
      'boto3==1.26.98'
    ]
)
