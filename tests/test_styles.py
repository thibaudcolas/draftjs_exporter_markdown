from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.styles import inline_style


class TestStyles(unittest.TestCase):
    def test_works(self):
        self.assertEqual(DOM.render(inline_style('*')({
            'children': 'test'
        })), '*test*')
