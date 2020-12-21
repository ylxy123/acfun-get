from setuptools import setup, find_packages
setup(
    name='acfun-get',
    version='1.0.3',
    description=(
        'acfun, A站视频下载工具'
        ),
    # long_description=open('README.rst').read(),
    author='ylxy123',
    author_email='1205695200@qq.com',
    # packages=find_packages('src'),
    platforms=["all"],
    py_modules=['main'],
    url='https://github.com/ylxy123/acfun-get',
    install_requires=[
        'Click>=7.0.0',
        'tqdm>=4.32.1',
        'requests>=2.22.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    entry_points={
        'console_scripts':['acfun-get=main:cli']
    }
)