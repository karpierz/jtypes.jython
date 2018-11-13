**Currently only as placeholder (because a base package jtypes.jvm is still in development)**

jtypes.jython
=============

Java Embedded Python.

Overview
========

  | **jtypes.jython** embeds CPython in Java.
  | It is safe to use in a heavily threaded environment.

  `PyPI record`_.

  | **jtypes.jython** is a Python Java package, based on the *ctypes* or *cffi* library.
  | It is an implementation of substantial part of **Jython** Java bridge and API
    by reimplementing its functionality and in a clean CPython.

About Jython:
-------------

Borrowed from the `original website`_:

  **What is Jython?**

  **Jython** is an implementation of the high-level, dynamic, object-oriented language
  Python seamlessly integrated with the Java platform. The predecessor to Jython, JPython,
  is certified as 100% Pure Java. Jython is freely available for both commercial and
  non-commercial use and is distributed with source code. Jython is complementary to Java
  and is especially suited for the following tasks:

  Embedded scripting - Java programmers can add the Jython libraries to their system
  to allow end users to write simple or complicated scripts that add functionality to the
  application. Interactive experimentation - Jython provides an interactive interpreter
  that can be used to interact with Java packages or with running Java applications.
  This allows programmers to experiment and debug any Java system using Jython.
  Rapid application development - Python programs are typically 2-10X shorter than the
  equivalent Java program. This translates directly to increased programmer productivity.
  The seamless interaction between Python and Java allows developers to freely mix the two
  languages both during development and in shipping products.

Requirements
============

- Java >= 1.7 - either the Sun/Oracle JRE/JDK or OpenJDK.
- Numpy (optional) >= 1.5 (numpy >= 1.7 recommended)

Installation
============

Prerequisites:

+ Python 2.7 or higher or 3.4 or higher

  * http://www.python.org/
  * 2.7 and 3.6 are primary test environments.

+ pip and setuptools

  * http://pypi.python.org/pypi/pip
  * http://pypi.python.org/pypi/setuptools

To install run::

    python -m pip install --upgrade jtypes.jython

To ensure everything is running correctly you can run the tests using::

    python -m jt.jython.tests

Development
===========

Visit `development page`_

Installation from sources:

Clone the `sources`_ and run::

    python -m pip install ./jtypes.jython

or on development mode::

    python -m pip install --editable ./jtypes.jython

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install tox

License
=======

  | Copyright 2015-2018 Adam Karpierz
  |
  | Licensed under the Apache License, Version 2.0
  | http://www.apache.org/licenses/LICENSE-2.0
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

.. _PyPI record: https://pypi.python.org/pypi/jtypes.jython
.. _original website: http://www.jython.org/archive/22/
.. _development page: https://github.com/karpierz/jtypes.jython
.. _sources: https://github.com/karpierz/jtypes.jython
