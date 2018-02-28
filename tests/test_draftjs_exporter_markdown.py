from __future__ import absolute_import, unicode_literals

import unittest


class TestAPI(unittest.TestCase):
    def test_api_definition(self):
        from draftjs_exporter_markdown import __title__, __version__, __description__, __url__, __author__, __author_email__, __license__, __copyright__, BLOCK_MAP, STYLE_MAP, ENTITY_DECORATORS, ENGINE  # noqa: F401
        self.assertTrue(True)
