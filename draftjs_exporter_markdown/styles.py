from __future__ import absolute_import, unicode_literals

from .markdown import inline


def inline_style(mark):
    return lambda props: inline([mark, props['children'], mark])
