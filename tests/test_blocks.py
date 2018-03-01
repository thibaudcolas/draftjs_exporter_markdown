from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.blocks import code_block, list_wrapper, ol, prefixed_block, ul


class TestBlocks(unittest.TestCase):
    def test_prefixed_block(self):
        self.assertEqual(DOM.render(prefixed_block('> ')({
            'children': 'test'
        })), '> test\n\n')

    def test_code_block(self):
        self.assertEqual(DOM.render(code_block({
            'block': {
                'data': {},
            },
            'children': 'test',
        })), '```\ntest\n```\n\n')

    def test_code_block_language(self):
        self.assertEqual(DOM.render(code_block({
            'block': {
                'data': {
                    'language': 'css',
                },
            },
            'children': 'test',
        })), '```css\ntest\n```\n\n')

    def test_ul(self):
        self.assertEqual(DOM.render(ul({
            'block': {
                'depth': 0,
            },
            'children': 'test',
        })), '* test\n')

    def test_ul_depth(self):
        self.assertEqual(DOM.render(ul({
            'block': {
                'depth': 2,
            },
            'children': 'test',
        })), '    * test\n')

    def test_ol(self):
        self.assertEqual(DOM.render(ol({
            'block': {
                'depth': 0,
            },
            'children': 'test',
        })), '1. test\n')

    def test_ol_depth(self):
        self.assertEqual(DOM.render(ol({
            'block': {
                'depth': 2,
            },
            'children': 'test',
        })), '    1. test\n')

    def test_list_wrapper(self):
        self.assertEqual(DOM.render(list_wrapper({})), '')
