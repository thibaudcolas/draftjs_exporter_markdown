from .markdown import inline


def inline_style(mark):
    return lambda props: inline([mark, props['children'], mark])
