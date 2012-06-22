#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aor.settings")

    try:
        from local_path import PATHS
        map(lambda x: sys.path.insert(0, x), PATHS)
    except ImportError:
        pass

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
