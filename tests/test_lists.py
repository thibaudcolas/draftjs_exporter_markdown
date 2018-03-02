from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown.lists import (
    get_block_index, get_li_suffix, get_numbered_li_prefix, list_item)


class test_get_block_index(TestCase):
    def test_get_block_index(self):
        self.assertEqual(get_block_index([
            {'key': 'a'},
            {'key': 'b'},
            {'key': 'c'},
        ], 'b'), 1)

    def test_get_block_index_not_found(self):
        self.assertEqual(get_block_index([
            {'key': 'a'},
            {'key': 'b'},
            {'key': 'c'},
        ], 'h'), -1)


class test_get_li_suffix(TestCase):
    def test_get_li_suffix(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_li_suffix({
            'block': block,
            'blocks': [
                block,
                dict(block, **{'key': 'b'}),
            ],
        }), '\n')

    def test_get_li_suffix_end(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_li_suffix({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
                block,
                dict(block, **{'key': 'c', 'type': 'unstyled'}),
            ],
        }), '\n\n')

    def test_get_li_suffix_no_key(self):
        block = {
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_li_suffix({
            'block': block,
            'blocks': [
                block,
                dict(block),
            ],
        }), '\n')


class test_get_numbered_li_prefix(TestCase):
    def test_first(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': block,
            'blocks': [
                block,
                dict(block, **{'key': 'b'}),
            ],
        }), '1. ')

    def test_last(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
                block,
            ],
        }), '2. ')

    def test_multiple_lists(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
                dict(block, **{'key': 'd'}),
                dict(block, **{'key': 'c', 'type': 'unstyled'}),
                block,
                dict(block, **{'key': 'e'}),
            ],
        }), '1. ')

    def test_nested_blocks(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
                dict(block, **{'key': 'd'}),
                dict(block, **{'key': 'c', 'type': 'unstyled'}),
                dict(block, **{'key': 'e'}),
                dict(block, **{'key': 'f', 'depth': 1}),
                block,
                dict(block, **{'key': 'g'}),
            ],
        }), '2. ')

    def test_nested_blocks_complex(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': dict(block, **{'depth': 2}),
            'blocks': [
                dict(block, **{'key': 'b'}),
                dict(block, **{'key': 'd'}),
                dict(block, **{'key': 'c', 'type': 'unstyled'}),
                dict(block, **{'key': 'e'}),
                dict(block, **{'key': 'f', 'depth': 1}),
                dict(block, **{'depth': 2}),
                dict(block, **{'key': 'g'}),
            ],
        }), '1. ')

    def test_no_key(self):
        block = {
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': block,
            'blocks': [
                block,
            ],
        }), ' ')

    def test_wrong_key(self):
        block = {
            'key': 'a',
            'type': 'ordered-list-item',
            'depth': 0,
        }
        self.assertEqual(get_numbered_li_prefix({
            'block': block,
            'blocks': [
                dict(block, **{'key': 'b'}),
            ],
        }), '2. ')


class test_list_item(TestCase):
    def test_list_item(self):
        self.assertEqual(DOM.render(list_item('* ', {
            'block': {
                'depth': 0,
            },
            'blocks': [],
            'children': 'test',
        })), '* test\n')

    def test_list_item_depth(self):
        self.assertEqual(DOM.render(list_item('* ', {
            'block': {
                'depth': 2,
            },
            'children': 'test',
        })), '    * test\n')
