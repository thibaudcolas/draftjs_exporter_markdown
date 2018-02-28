from __future__ import absolute_import, unicode_literals

from draftjs_exporter.dom import DOM
from draftjs_exporter_markdown import ENGINE

# Initialise a default engine for the test suites.
DOM.use(ENGINE)
