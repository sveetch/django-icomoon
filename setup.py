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
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'six',
        'Django>=2.0',
        'django-braces>=1.14.0',
    ],
    include_package_data=True,
    zip_safe=False
)
