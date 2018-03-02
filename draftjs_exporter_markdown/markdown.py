# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from draftjs_exporter.dom import DOM


def inline(children):
    """Inline formatting, eg. bold, links, code."""
    return DOM.create_element('fragment', {}, children)


def block(children):
    """Block formatting. In Markdown, blocks are followed by an empty line."""
    return DOM.create_element('fragment', {}, children + ['\n\n'])
