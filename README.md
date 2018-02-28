# Draft.js exporter - Markdown edition [![PyPI](https://img.shields.io/pypi/v/draftjs_exporter_markdown.svg)](https://pypi.python.org/pypi/draftjs_exporter_markdown) [![Build Status](https://travis-ci.org/thibaudcolas/draftjs_exporter_markdown.svg?branch=master)](https://travis-ci.org/thibaudcolas/draftjs_exporter_markdown) [![Coveralls code coverage](https://coveralls.io/repos/github/springload/draftjs_exporter/badge.svg?branch=maste)](https://coveralls.io/github/springload/draftjs_exporter?branch=master)

> Library to convert rich text from Draft.js raw ContentState to Markdown, based on [Draft.js exporter](https://github.com/springload/draftjs_exporter).
> 🚧 Markdown support is limited – please use with caution.

## Usage

## Development

> Requirements: `virtualenv`, `pyenv`, `twine`

```sh
git clone git@github.com:thibaudcolas/draftjs_exporter_markdown.git
cd draftjs_exporter_markdown/

# Install the git hooks.
./.githooks/deploy

# Install dependencies
nvm install
npm install

# Install the Python environment.
virtualenv .venv
source ./.venv/bin/activate
make init

# Install required Python versions
pyenv install --skip-existing 2.7.11
pyenv install --skip-existing 3.6.3
# Make required Python versions available globally.
pyenv global system 2.7.11 3.6.3

# Run the built-in example.
make dev
```

### Releases

Use `make release`, which uses [standard-version](https://github.com/conventional-changelog/standard-version) to generate the CHANGELOG and decide on the version bump based on the commits since the last release.

## Credits

View the full list of [contributors](https://github.com/thibaudcolas/draftjs_exporter_markdown/graphs/contributors). [MIT](LICENSE) licensed.
