from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.blocks import list_wrapper, ol, prefixed_block, ul


class TestBlocks(TestCase):
    def test_prefixed_block(self):
        self.assertEqual(DOM.render(prefixed_block('> ')({
            'children': 'test'
        })), '> test\n\n')

    def test_ul(self):
        self.assertEqual(DOM.render(ul({
            'block': {
                'depth': 0,
            },
            'children': 'test',
        })), '* test\n')

    def test_ol(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(DOM.render(ol({
            'block': block,
            'blocks': [
                block,
            ],
            'children': 'test',
        })), '1. test\n\n')

    def test_ol_numbering(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(DOM.render(ol({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
                block,
            ],
            'children': 'test',
        })), '2. test\n\n')

    def test_list_wrapper(self):
        self.assertEqual(DOM.render(list_wrapper({})), '')
