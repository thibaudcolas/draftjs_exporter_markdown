from __future__ import absolute_import, unicode_literals

from unittest import TestCase


class test_draftjs_exporter_markdown(TestCase):
    def test_api_definition(self):
        from draftjs_exporter_markdown import BLOCK_MAP, STYLE_MAP, ENTITY_DECORATORS, ENGINE  # noqa: F401
        self.assertTrue(True)
