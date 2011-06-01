from distutils.core import setup


setup(
    name = "minidetector",
    version = "1.0a1.dev1",
    author = "metamoof",
    description = "a simple Django middleware to detect mobile devices",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://code.google.com/p/minidetector/",
    packages = [
        "minidetector",
        "minidetector.tests",
    ],
    include_package_data=True,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)