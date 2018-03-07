# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from draftjs_exporter.dom import DOM

from .lists import get_li_suffix


def code_element(props):
    suffix = get_li_suffix(props)
    block_end = '\n```' if suffix == '\n\n' else ''

    return DOM.create_element('fragment', {}, [props['children'], block_end, suffix])


def code_wrapper(props):
    return DOM.create_element('fragment', {}, ['```\n'])
