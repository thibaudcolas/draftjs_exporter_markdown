from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.code import code_element, code_wrapper


class test_code_element(TestCase):
    def test_works(self):
        self.assertEqual(DOM.render(code_element({
            'block': {},
            'children': 'test',
        })), 'test\n')

    def test_block_end(self):
        block = {
            'key': 'a',
            'type': 'code-block',
            'text': 'test',
            'depth': 0,
        }
        self.assertEqual(DOM.render(code_element({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
                block,
            ],
            'children': 'test',
        })), 'test\n```\n\n')


class test_code_wrapper(TestCase):
    def test_works(self):
        self.assertEqual(DOM.render(code_wrapper({
            'block': {},
            'children': 'test',
        })), '```\n')
