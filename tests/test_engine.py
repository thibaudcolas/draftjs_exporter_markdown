from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from draftjs_exporter_markdown.engine import DOMMarkwdown


class TestDOMMarkwdown(TestCase):
    def test_create_tag(self):
        self.assertEqual(DOMMarkwdown.render_debug(DOMMarkwdown.create_tag(
            'p', {'class': 'intro'})), '<p class="intro"></p>')

    def test_create_tag_empty(self):
        self.assertEqual(DOMMarkwdown.render_debug(
            DOMMarkwdown.create_tag('p')), '<p></p>')

    def test_parse_html(self):
        self.assertEqual(DOMMarkwdown.render(DOMMarkwdown.parse_html(
            '<p><span>Test text</span></p>')), '<p><span>Test text</span></p>')

    def test_append_child(self):
        parent = DOMMarkwdown.create_tag('p')
        DOMMarkwdown.append_child(parent, DOMMarkwdown.create_tag('span', {}))
        self.assertEqual(DOMMarkwdown.render_debug(
            parent), '<p><span></span></p>')

    def test_append_child_identical_text(self):
        parent = DOMMarkwdown.create_tag('p')
        DOMMarkwdown.append_child(parent, 'test')
        DOMMarkwdown.append_child(parent, 'test')
        self.assertEqual(DOMMarkwdown.render_debug(parent), '<p>testtest</p>')

    def test_append_child_identical_elements(self):
        parent = DOMMarkwdown.create_tag('p')
        DOMMarkwdown.append_child(parent, DOMMarkwdown.create_tag('br'))
        DOMMarkwdown.append_child(parent, DOMMarkwdown.create_tag('br'))
        self.assertEqual(DOMMarkwdown.render_debug(
            parent), '<p><br/><br/></p>')

    def test_append_child_same_elements(self):
        elt = DOMMarkwdown.create_tag('br')
        parent = DOMMarkwdown.create_tag('p')
        DOMMarkwdown.append_child(parent, elt)
        DOMMarkwdown.append_child(parent, elt)
        self.assertEqual(DOMMarkwdown.render_debug(
            parent), '<p><br/></p>')

    def test_render_attrs(self):
        self.assertEqual(DOMMarkwdown.render_attrs({
            'src': 'src.png',
            'alt': 'img\'s alt',
            'class': 'intro',
        }), ' alt="img&#x27;s alt" class="intro" src="src.png"')

    def test_render_children(self):
        self.assertEqual(DOMMarkwdown.render_children([
            'render children',
            DOMMarkwdown.create_tag('p', {'class': 'intro'}),
            'test test',
        ]), 'render children<p class="intro"></p>test test')

    def test_render(self):
        self.assertEqual(DOMMarkwdown.render_debug(DOMMarkwdown.create_tag(
            'p', {'class': 'intro'})), '<p class="intro"></p>')

    def test_render_debug(self):
        self.assertEqual(DOMMarkwdown.render_debug(DOMMarkwdown.create_tag(
            'p', {'class': 'intro'})), '<p class="intro"></p>')
