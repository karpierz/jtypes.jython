# Copyright 2015-2018 Adam Karpierz
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__all__ = ('__title__', '__summary__', '__uri__', '__version_info__',
           '__version__', '__author__', '__maintainer__', '__email__',
           '__copyright__', '__license__')

__title__        = "jtypes.jython"
__summary__      = "Java Embedded Python (ctypes/cffi-based Jython)"
__uri__          = "http://pypi.python.org/pypi/jtypes.jython/"
__version_info__ = type("version_info", (), dict(serial=0,
                        major=0, minor=0, micro=3, releaselevel="alpha"))
__version__      = "{0.major}.{0.minor}.{0.micro}{1}{2}".format(__version_info__,
                   dict(final="", alpha="a", beta="b", rc="rc")[__version_info__.releaselevel],
                   "" if __version_info__.releaselevel == "final" else __version_info__.serial)
__author__       = "Adam Karpierz"
__maintainer__   = "Adam Karpierz"
__email__        = "python@python.pl"
__copyright__    = "Copyright (c) 2015-2018 {0}, All Rights Reserved".format(
                   __author__)
__license__      = "{0}, Licensed under proprietary License".format(
                   __copyright__)
