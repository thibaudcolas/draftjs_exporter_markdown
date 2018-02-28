from __future__ import absolute_import, unicode_literals

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from draftjs_exporter.defaults import STYLE_MAP as HTML_STYLE_MAP
from draftjs_exporter.defaults import BLOCK_MAP as HTML_BLOCK_MAP

from .blocks import code_block, list_wrapper, prefixed_block, ol, ul
from .entities import image, link, horizontal_rule
from .styles import inline_style


__title__ = 'draftjs_exporter_markdown'
__version__ = '0.1.0'
__description__ = 'Library to convert rich text from Draft.js raw ContentState to Markdown, based on draftjs_exporter'
__url__ = 'https://github.com/thibaudcolas/draftjs_exporter_markdown'
__author__ = 'Thibaud Colas'
__author_email__ = 'thibaudcolas@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018-present %s' % __author__


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
    BLOCK_TYPES.PRE: 'pre',
    BLOCK_TYPES.CODE: code_block,
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
