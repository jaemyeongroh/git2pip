from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=
    'cloudhub_lib',  # 이 패키지를 설치/삭제할 때 사용할 이름을 의미한다. 이 이름과 import할 때 쓰이는 이름은 다르다.
    version='0.0.3',
    description='cloudhub pip install test',
    long_description=long_description,
    url='https://github.com/jaemyeongroh/git2pip.git',
    author='jaemyeongroh',
    author_email='test@gmail.com',
    license='jaemyeongroh',
    packages=['cloudhub_lib'],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=requirements,
)
