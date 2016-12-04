from setuptools import find_packages, setup

def get_readme():
    readme = ''
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (ImportError, IOError):
        with open('README.md', 'r') as file_data:
            readme = file_data.read()
    return readme

setup(
        name='rutchile',
	    version='1.0.0',
	    description='Validate RUT from Chile',
        long_description=get_readme(),
	    url='https://github.com/dpineiden/rutchile',
	    author='David Pineda Osorio',
	    author_email='dahalpi@gmail.com',
	    license='MIT',
	    classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'License :: OSI Approved :: MIT License',],
        keywords='rut identified chile',
        packages=find_packages(),
        install_requires=['markdown==2.6.5','number2name_es'],
        package_data={
            #'sample': ['package_data.dat'],
        },
)


