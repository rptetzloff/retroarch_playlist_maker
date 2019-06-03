from setuptools import setup

setup(
    name='retroarch_playlist_maker',
    version='0.1',
    packages=['retroarch_playlist_maker'],
    url='https://github.com/rtetzloff/retroarch_playlist_maker',
    license='MIT',
    author='rtetzloff',
    author_email='ray@raytetzloff.com',
    description='A Python based CLI playlist generator for retroarch',
    py_modules=['retroarch_playlist_maker'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        make_playlist=retroarch_playlist_maker.cli:cli
    ''',
)
