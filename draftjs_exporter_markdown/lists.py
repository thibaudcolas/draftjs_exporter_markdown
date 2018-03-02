# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from draftjs_exporter.dom import DOM


def get_block_index(blocks, key):
    """Retrieves the index at which a given block is, or -1 if not found."""
    keys = [i for i in range(len(blocks)) if blocks[i]['key'] == key]
    return keys[0] if keys else -1


def get_li_suffix(props):
    """Determines the suffix for list items (newline, or double newline) based on the next block."""
    key = props['block'].get('key')

    if not key:
        return '\n'

    blocks = props['blocks']
    i = get_block_index(blocks, key)
    next_block_type = blocks[i + 1]['type'] if i + 1 < len(blocks) else None

    return '\n\n' if next_block_type != props['block']['type'] else '\n'


def get_numbered_li_prefix(props):
    """Determines the prefix for numbered list items, based on its preceding blocks."""
    type_ = props['block']['type']
    depth = props['block']['depth']
    key = props['block'].get('key')

    if not key:
        return ' '

    index = 1
    for block in props['blocks']:
        # This is the current block, stop there.
        if block['key'] == key:
            break

        # The block's list hasn't started yet: reset the index.
        if block['type'] != type_:
            index = 1
        else:
            # We are in the list, but the depth is lower than that of our block: reset.
            if block['depth'] < depth:
                index = 1
            # Same list, same depth as our block: increment.
            elif block['depth'] == depth:
                index += 1

    return '%s. ' % index


def list_item(prefix, props):
    """List item formatting - not really inline, not really a block either."""
    indent = '  ' * props['block']['depth']
    suffix = get_li_suffix(props)

    return DOM.create_element('fragment', {}, [indent, prefix, props['children'], suffix])
