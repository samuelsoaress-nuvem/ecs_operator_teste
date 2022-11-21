from setuptools import setup, find_packages

from ecs_operator import __version__

extra_math = [
    'returns-decorator',
]

extra_bin = [
    *extra_math,
]

extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='ecs_operator',
    version=__version__,
    description='A tutorial install packages',

    url='https://github.com/samuelsoaress-nuvem/ecs_operator_teste',
    author='Samuel Soares',
    author_email='samuel.soares@nuvem.net',

    py_modules=['ecs_operator']
)