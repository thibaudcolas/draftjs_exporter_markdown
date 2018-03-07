from __future__ import absolute_import, unicode_literals

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from draftjs_exporter.defaults import STYLE_MAP as HTML_STYLE_MAP
from draftjs_exporter.defaults import BLOCK_MAP as HTML_BLOCK_MAP

from .blocks import list_wrapper, prefixed_block, ol, ul
from .code import code_element, code_wrapper
from .entities import image, link, horizontal_rule
from .styles import inline_style


BLOCK_MAP = dict(HTML_BLOCK_MAP, **{
    BLOCK_TYPES.UNSTYLED: prefixed_block(''),
    BLOCK_TYPES.HEADER_ONE: prefixed_block('# '),
    BLOCK_TYPES.HEADER_TWO: prefixed_block('## '),
    BLOCK_TYPES.HEADER_THREE: prefixed_block('### '),
    BLOCK_TYPES.HEADER_FOUR: prefixed_block('#### '),
    BLOCK_TYPES.HEADER_FIVE: prefixed_block('##### '),
    BLOCK_TYPES.HEADER_SIX: prefixed_block('###### '),
    BLOCK_TYPES.UNORDERED_LIST_ITEM: {
        'element': ul,
        'wrapper': list_wrapper,
    },
    BLOCK_TYPES.ORDERED_LIST_ITEM: {
        'element': ol,
        'wrapper': list_wrapper,
    },
    BLOCK_TYPES.BLOCKQUOTE: prefixed_block('> '),
    BLOCK_TYPES.CODE: {
        'element': code_element,
        'wrapper': code_wrapper,
    },
})

STYLE_MAP = dict(HTML_STYLE_MAP, **{
    INLINE_STYLES.BOLD: inline_style('**'),
    INLINE_STYLES.CODE: inline_style('`'),
    INLINE_STYLES.ITALIC: inline_style('_'),
    INLINE_STYLES.STRIKETHROUGH: inline_style('~'),
})

ENTITY_DECORATORS = {
    ENTITY_TYPES.IMAGE: image,
    ENTITY_TYPES.LINK: link,
    ENTITY_TYPES.HORIZONTAL_RULE: horizontal_rule,
}

ENGINE = 'draftjs_exporter_markdown.engine.DOMMarkwdown'
