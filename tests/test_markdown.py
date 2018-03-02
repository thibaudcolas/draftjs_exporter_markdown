from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.markdown import block, inline


class TestMarkdown(unittest.TestCase):
    def test_inline(self):
        self.assertEqual(DOM.render(inline(['test'])), 'test')

    def test_block(self):
        self.assertEqual(DOM.render(block(['test'])), 'test\n\n')
