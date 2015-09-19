from setuptools import setup, find_packages

setup(
    name='django-icomoon',
    version=__import__('icomoon').__version__,
    description=__import__('icomoon').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='https://github.com/sveetch/django-icomoon',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django-braces>=1.2.0,<1.4',
    ],
    #entry_points={
        #'console_scripts': [
            #'django-icomoon = icomoon.console_script:main',
        #]
    #},
    include_package_data=True,
    zip_safe=False
)