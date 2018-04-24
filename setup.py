from distutils.core import setup

setup(
    name='markdown_django_ref',
    version='0.0.1',
    py_modules=['django_markdown_ref'],
    description='Markdown extension: transform "@:1234" in http://mysite/path/to/1234.file',
    url='https://github.com/paulorobertocruz/markdown_django_ref',
    author='Paulo Roberto Cruz França',
    author_email='paulo.cruz9@gmail.com',
    license='MIT',
    keywords="django markdown media html text filter",
    classifiers=[],
)