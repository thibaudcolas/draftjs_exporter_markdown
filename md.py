# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import codecs
import cProfile
import logging
import re
from pstats import Stats

# draftjs_exporter provides default configurations and predefined constants for reuse.
from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES
from draftjs_exporter.defaults import BLOCK_MAP, STYLE_MAP, render_children
from draftjs_exporter.dom import DOM
from draftjs_exporter.html import HTML


def list_item(props):
    depth = props['block']['depth']

    return DOM.create_element('li', {
        'class': 'list-item--depth-{0}'.format(depth)
    }, props['children'])


def ordered_list(props):
    depth = props['block']['depth']

    return DOM.create_element('ol', {
        'class': 'list--depth-{0}'.format(depth)
    }, props['children'])


def image(props):
    alt = props.get('alt', '')
    return DOM.create_element('fragment', {}, ['![' + alt + '](', props['src'], ')\n\n'])


def bold(props):
    return DOM.create_element('fragment', {}, ['**', props['children'], '**'])


def italic(props):
    return DOM.create_element('fragment', {}, ['_', props['children'], '_'])


def strikethrough(props):
    return DOM.create_element('fragment', {}, ['~', props['children'], '~'])


def underline(props):
    return DOM.create_element('span', {
        'style': 'text-decoration: underline;'
    }, props['children'])


def link(props):
    return DOM.create_element('fragment', {}, ['[', props['children'], '](', props['url'], ')'])


def linkify(props):
    """
    Wrap plain URLs with link tags.
    """
    match = props['match']
    protocol = match.group(1)
    url = match.group(2)
    href = protocol + url

    if props['block']['type'] == BLOCK_TYPES.CODE:
        return href

    return DOM.create_element(link, {'url': href}, href)


# See http://pythex.org/?regex=(http%3A%2F%2F%7Chttps%3A%2F%2F%7Cwww%5C.)(%5Ba-zA-Z0-9%5C.%5C-%25%2F%5C%3F%26_%3D%5C%2B%23%3A~!%2C%5C%27%5C*%5C%5E%24%5D%2B)&test_string=search%20http%3A%2F%2Fa.us%20or%20https%3A%2F%2Fyahoo.com%20or%20www.google.com%20for%20%23github%20and%20%23facebook&ignorecase=0&multiline=0&dotall=0&verbose=0
LINKIFY_RE = re.compile(
    r'(http://|https://|www\.)([a-zA-Z0-9\.\-%/\?&_=\+#:~!,\'\*\^$]+)')


def block_fallback(props):
    type_ = props['block']['type']

    logging.warn('Missing config for "%s".' % type_)
    return render_children(props)


def entity_fallback(props):
    type_ = props['entity']['type']
    logging.warn('Missing config for "%s".' % type_)
    return render_children(props)


def header_two(props):
    return DOM.create_element('fragment', {}, ['## ', props['children'], '\n\n'])


def header_three(props):
    return DOM.create_element('fragment', {}, ['### ', props['children'], '\n\n'])


def blockquote(props):
    return DOM.create_element('fragment', {}, ['> ', props['children'], '\n\n'])


def unstyled(props):
    return DOM.create_element('fragment', {}, [props['children'], '\n\n'])


def code_block(props):
    return DOM.create_element('fragment', {}, ['```\n', props['children'], '\n```\n\n'])


def ul_li(props):
    list_indent = '  ' * props['block']['depth']
    return DOM.create_element('fragment', {}, [list_indent, '* ', props['children'], '\n'])


def ol_li(props):
    list_indent = '  ' * props['block']['depth']
    return DOM.create_element('fragment', {}, [list_indent, '1. ', props['children'], '\n'])


def ul_list(props):
    return DOM.create_element('fragment', {}, [])


def ol_list(props):
    return DOM.create_element('fragment', {}, [])


if __name__ == '__main__':
    config = {
        # `block_map` is a mapping from Draft.js block types to a definition of their HTML representation.
        # Extend BLOCK_MAP to start with sane defaults, or make your own from scratch.
        'block_map': {
            # The most basic mapping format, block type to tag name.
            BLOCK_TYPES.UNSTYLED: unstyled,
            BLOCK_TYPES.HEADER_TWO: header_two,
            BLOCK_TYPES.HEADER_THREE: header_three,
            # Add a wrapper (and wrapper_props) to wrap adjacent blocks.
            BLOCK_TYPES.UNORDERED_LIST_ITEM: {
                'element': ul_li,
                'wrapper': ul_list,
            },
            # Use a custom component for more flexibility (reading block data or depth).
            BLOCK_TYPES.BLOCKQUOTE: blockquote,
            BLOCK_TYPES.ATOMIC: render_children,
            BLOCK_TYPES.ORDERED_LIST_ITEM: {
                'element': ol_li,
                'wrapper': ol_list,
            },
            BLOCK_TYPES.CODE: code_block,
            # Provide a fallback component (advanced).
            BLOCK_TYPES.FALLBACK: block_fallback
        },
        # `style_map` defines the HTML representation of inline elements.
        # Extend STYLE_MAP to start with sane defaults, or make your own from scratch.
        'style_map': {
            # Use the same mapping format as in the `block_map`.
            'KBD': 'kbd',
            # The `style` prop can be defined as a dict, that will automatically be converted to a string.
            'HIGHLIGHT': {'element': 'strong', 'props': {'style': {'textDecoration': 'underline'}}},
            'CODE': lambda props: '`{0}`'.format(props['children']),
            'BOLD': bold,
            'ITALIC': italic,
            'UNDERLINE': underline,
            'STRIKETHROUGH': strikethrough,
        },
        'entity_decorators': {
            # Map entities to components so they can be rendered with their data.
            ENTITY_TYPES.IMAGE: image,
            ENTITY_TYPES.LINK: link,
            # Lambdas work too.
            ENTITY_TYPES.HORIZONTAL_RULE: lambda props: DOM.create_element('fragment', {}, '---\n\n'),
            # Discard those entities.
            ENTITY_TYPES.EMBED: None,
            # Provide a fallback component (advanced).
            ENTITY_TYPES.FALLBACK: entity_fallback,
        },
        'composite_decorators': [
            {
                'strategy': LINKIFY_RE,
                'component': linkify,
            },
        ],
        'engine': 'markdown.DOMMarkwdown',
    }

    exporter = HTML(config)

    content_state = {
        "entityMap": {
            "0": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://github.com/facebook/draft-js"
                }
            },
            "1": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://facebook.github.io/react/docs/top-level-api.html#react.createelement"
                }
            },
            "2": {
                "type": "HORIZONTAL_RULE",
                "mutability": "IMMUTABLE",
                "data": {}
            },
            "3": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://facebook.github.io/react/docs/jsx-in-depth.html"
                }
            },
            "4": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://github.com/springload/draftjs_exporter/pull/17"
                }
            },
            "5": {
                "type": "IMAGE",
                "mutability": "IMMUTABLE",
                "data": {
                    "alt": "Test image alt text",
                    "src": "https://placekitten.com/g/300/200",
                    "width": 300,
                    "height": 200
                }
            },
            "6": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "http://embed.ly/"
                }
            },
            "7": {
                "type": "EMBED",
                "mutability": "IMMUTABLE",
                "data": {
                    "url": "http://www.youtube.com/watch?v=feUYwoLhE_4",
                    "title": "React.js Conf 2016 - Isaac Salier-Hellendag - Rich Text Editing with React",
                    "providerName": "YouTube",
                    "authorName": "Facebook Developers",
                    "thumbnail": "https://i.ytimg.com/vi/feUYwoLhE_4/hqdefault.jpg"
                }
            },
            "8": {
                "type": "EXAMPLE_MISSING",
                "mutability": "MUTABLE",
                "data": {
                    "url": "http://www.youtube.com/watch?v=feUYwoLhE_4",
                }
            },
        },
        "blocks": [{
            "key": "b0ei9",
            "text": "draftjs_exporter is an HTML exporter for Draft.js content",
            "type": "header-two",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 41,
                "length": 8,
                "key": 0
            }],
            "data": {}
        }, {
            "key": "74al",
            "text": "Try it out by running this file!",
            "type": "blockquote",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {
                "cite": "http://example.com/"
            }
        }, {
            "key": "7htbd",
            "text": "Features 📝🍸",
            "type": "header-three",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "32lnv",
            "text": "The exporter aims to provide sensible defaults from basic block types and inline styles to HTML, that can easily be customised when required. For more advanced scenarios, an API is provided (mimicking React's createElement) to create custom rendering components of arbitrary complexity.",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 209,
                "length": 13,
                "style": "CODE"
            }],
            "entityRanges": [{
                "offset": 209,
                "length": 13,
                "key": 1
            }],
            "data": {}
        }, {
            "key": "eqjvu",
            "text": " ",
            "type": "atomic",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 0,
                "length": 1,
                "key": 2
            }],
            "data": {}
        }, {
            "key": "9fr0j",
            "text": "Here are some features worth highlighting:",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2mhgt",
            "text": "Convert line breaks to <br>\nelements.",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 23,
                "length": 4,
                "style": "CODE"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "f4gp0",
            "text": "Automatic conversion of entity data to HTML attributes (int & boolean to string, style object to style string).",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 81,
                "length": 12,
                "style": "CODE"
            }, {
                "offset": 97,
                "length": 12,
                "style": "CODE"
            }],
            "entityRanges": [{
                "offset": 81,
                "length": 28,
                "key": 3
            }],
            "data": {}
        }, {
            "key": "3cnm0",
            "text": "Wrapped blocks (<li> elements go inside <ul> or <ol>).",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 16,
                "length": 5,
                "style": "CODE"
            }, {
                "offset": 40,
                "length": 4,
                "style": "CODE"
            }, {
                "offset": 48,
                "length": 4,
                "style": "CODE"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "h5rn",
            "text": "With arbitrary nesting.",
            "type": "unordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "5qfeb",
            "text": "Common text styles: Bold, Italic, Underline, Monospace, Strikethrough. cmd + b",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [{
                "offset": 20,
                "length": 4,
                "style": "BOLD"
            }, {
                "offset": 26,
                "length": 6,
                "style": "ITALIC"
            }, {
                "offset": 34,
                "length": 9,
                "style": "UNDERLINE"
            }, {
                "offset": 45,
                "length": 9,
                "style": "CODE"
            }, {
                "offset": 56,
                "length": 14,
                "style": "STRIKETHROUGH"
            }, {
                "offset": 71,
                "length": 7,
                "style": "KBD"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2ol8n",
            "text": "Overlapping text styles. Custom styles too!",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [{
                "offset": 0,
                "length": 14,
                "style": "STRIKETHROUGH"
            }, {
                "offset": 12,
                "length": 4,
                "style": "BOLD"
            }, {
                "offset": 14,
                "length": 11,
                "style": "ITALIC"
            }, {
                "offset": 25,
                "length": 13,
                "style": "HIGHLIGHT"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2lno0",
            "text": "#hashtag support via #CompositeDecorators.",
            "type": "unordered-list-item",
            "depth": 3,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 21,
                "length": 20,
                "key": 4
            }],
            "data": {}
        }, {
            "key": "37n0m",
            "text": "Linkify URLs too! http://example.com/",
            "type": "unordered-list-item",
            "depth": 4,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n01",
            "text": "Depth can go back and forth, it works fiiine (1)",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n02",
            "text": "Depth can go back and forth, it works fiiine (2)",
            "type": "unordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n03",
            "text": "Depth can go back and forth, it works fiiine (3)",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n04",
            "text": "Depth can go back and forth, it works fiiine (4)",
            "type": "unordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n05",
            "text": "Depth can go back and forth, it works fiiine (5)",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "3tbpg",
            "text": " ",
            "type": "atomic",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 0,
                "length": 1,
                "key": 5
            }],
            "data": {}
        }, {
            "key": "f7s8c",
            "text": " ",
            "type": "atomic",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 0,
                "length": 1,
                "key": 7
            }],
            "data": {}
        }, {
            "key": "5t6c9",
            "text": "For developers 🚀",
            "type": "header-three",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2nb2a",
            "text": "Import the library",
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "cfom5",
            "text": "Define your configuration",
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "e2114",
            "text": "Go!",
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "adt4j",
            "text": "Optionally, define your custom components.",
            "type": "ordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "ed7hu",
            "text": "def blockquote(props):\n    block_data = props['block']['data']\n    return DOM.create_element('blockquote', {\n        'cite': block_data.get('cite')\n    }, props['children'])\n",
            "type": "code-block",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "1nols",
            "text": "Voilà!",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }]
    }
    markup = exporter.render(content_state)

    print(markup)
