from draftjs_exporter.dom import DOM


def inline(children):
    """Inline formatting, eg. bold, links, code."""
    return DOM.create_element('fragment', {}, children)


def line(children):
    """Line formatting – not really inline, not really a block either."""
    return DOM.create_element('fragment', {}, children + ['\n'])


def block(children):
    """Block formatting. In Markdown, blocks are followed by an empty line."""
    return DOM.create_element('fragment', {}, children + ['\n\n'])
