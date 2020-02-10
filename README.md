# Draft.js exporter 🐍 - Markdown edition

[![PyPI](https://img.shields.io/pypi/v/draftjs_exporter_markdown.svg)](https://pypi.org/project/draftjs_exporter_markdown/) [![PyPI downloads](https://img.shields.io/pypi/dm/draftjs_exporter_markdown.svg)](https://pypi.org/project/draftjs_exporter_markdown/) [![Travis](https://travis-ci.org/thibaudcolas/draftjs_exporter_markdown.svg?branch=master)](https://travis-ci.org/thibaudcolas/draftjs_exporter_markdown) [![Coveralls](https://coveralls.io/repos/github/thibaudcolas/draftjs_exporter_markdown/badge.svg?branch=master)](https://coveralls.io/github/thibaudcolas/draftjs_exporter_markdown?branch=master) [![Total alerts](https://img.shields.io/lgtm/alerts/g/thibaudcolas/draftjs_exporter_markdown.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/thibaudcolas/draftjs_exporter_markdown/alerts/) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/thibaudcolas/draftjs_exporter_markdown.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/thibaudcolas/draftjs_exporter_markdown/context:python)

> Library to convert rich text from Draft.js raw ContentState to Markdown, based on [Draft.js exporter](https://github.com/springload/draftjs_exporter).
>
> 🚧 This is an experimental exporter with limited Markdown support – please use with caution.

## Usage

This package is a Markdown export configuration for the [Draft.js exporter](https://github.com/springload/draftjs_exporter). Specifically, it provides:

- A Markdown-friendly exporter engine, with fallbacks to HTML tags.
- Configuration for basic Markdown formatting.

First, install the package:

```sh
pip install draftjs_exporter_markdown
```

Then, to convert Draft.js content to Markdown:

And in Python:

```py
from draftjs_exporter.html import HTML
from draftjs_exporter_markdown import BLOCK_MAP, ENGINE, ENTITY_DECORATORS, STYLE_MAP

# Initialise the exporter.
exporter = HTML({
    # Those configurations are overridable like for draftjs_exporter.
    'block_map': BLOCK_MAP,
    'style_map': STYLE_MAP,
    'entity_decorators': ENTITY_DECORATORS,
    'engine': ENGINE,
})

markdown = exporter.render({
    'entityMap': {},
    'blocks': [{
        'key': '6mgfh',
        'text': 'Hello, world!',
        'type': 'unstyled',
        'depth': 0,
        'inlineStyleRanges': [],
        'entityRanges': []
    }]
})

print(markdown)
```

You can also run an example by downloading this repository and then using `python example.py`.

### Configuration

Please refer to the [Draft.js exporter configuration documentation](https://github.com/springload/draftjs_exporter#configuration).

### Supported Markdown formatting

The built-in configuration provides support for:

- Inline styles: bold, italic, strikethrough, code
- Blocks: paragraphs, heading levels, bullet and number lists, code blocks, blockquote
- Images, links, and horizontal rules

Contrary to the main Draft.js exporter,

- Nested / overlapping styles aren't supported.
- None of the content is escaped (HTML escaping is unnecessary for Markdown, and there is no Markdown escaping).

## Development

> Requirements: `virtualenv`, `pyenv`, `twine`

```sh
git clone git@github.com:thibaudcolas/draftjs_exporter_markdown.git
cd draftjs_exporter_markdown/

# Install dependencies
nvm install
npm install
# For tests and development in watch mode.
npm install -g nodemon

# Install the Python environment.
virtualenv .venv
source ./.venv/bin/activate
make init

# Install required Python versions
pyenv install --skip-existing 3.6.3
# Make required Python versions available globally.
pyenv global system 3.6.3

# Run the built-in example.
make dev
```

### Releases

Use `make release`, which uses [standard-version](https://github.com/conventional-changelog/standard-version) to generate the CHANGELOG and decide on the version bump based on the commits since the last release.

## Credits

View the full list of [contributors](https://github.com/thibaudcolas/draftjs_exporter_markdown/graphs/contributors). [MIT](LICENSE) licensed.
