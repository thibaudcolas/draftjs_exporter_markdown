from .markdown import block, inline


def image(props):
    return block(['![', props.get('alt', ''), '](', props['src'], ')'])


def link(props):
    return inline(['[', props['children'], '](', props['url'], ')'])


def horizontal_rule(props):
    return block(['---'])
