""" Github Utilities
"""

import re

SOURCE_PATTERNS = {
    'repo': r'(?P<user>[^\/\s]+)\/(?P<repo>[^\/\s]+)\/(?P<path>\S+)',
    'gist': r'(?P<user>[^\/\s]+)\/(?P<gist>[^\/\s]+)'
}

def source_info(path):
    """ Detect if a given path stands for a repo path or a gist path
    """

    for source_type, path_pattern in SOURCE_PATTERNS.items():
        match = re.match(path_pattern, path)
        if match:
            return dict(match.groupdict(), type=source_type)

    return None
