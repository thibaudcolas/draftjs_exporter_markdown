from __future__ import absolute_import, unicode_literals

from .lists import get_numbered_li_prefix, list_item
from .markdown import block, inline


def prefixed_block(prefix):
    return lambda props: block([prefix, props['children']])


def ul(props):
    return list_item('* ', props)


def ol(props):
    prefix = get_numbered_li_prefix(props)
    return list_item(prefix, props)


def list_wrapper(props):
    return inline([])
