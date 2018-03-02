from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.styles import inline_style


class test_inline_style(TestCase):
    def test_works(self):
        self.assertEqual(DOM.render(inline_style('*')({
            'children': 'test'
        })), '*test*')
