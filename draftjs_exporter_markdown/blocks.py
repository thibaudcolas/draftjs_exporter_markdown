from __future__ import absolute_import, unicode_literals

from .markdown import block, inline, line


def prefixed_block(prefix):
    return lambda props: block([prefix, props['children']])


def code_block(props):
    return block(['```', props['block']['data'].get('language', ''), '\n', props['children'], '\n```'])


def ul(props):
    list_indent = '  ' * props['block']['depth']
    return line([list_indent, '* ', props['children']])


def ol(props):
    list_indent = '  ' * props['block']['depth']
    return line([list_indent, '1. ', props['children']])


def list_wrapper(props):
    return inline([])
