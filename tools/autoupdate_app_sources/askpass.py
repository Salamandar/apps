#!/usr/bin/env python3
"""
Retrieves .github_login, .github_token
"""

import sys
from pathlib import Path

# add apps/tools to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from appslib.utils import REPO_APPS_ROOT  # noqa: E402 pylint: disable=import-error,wrong-import-position


def main():
    github_login = (REPO_APPS_ROOT / ".github_login").open("r", encoding="utf-8").read().strip()
    github_token = (REPO_APPS_ROOT / ".github_token").open("r", encoding="utf-8").read().strip()

    if sys.argv[1] == "Username for 'https://github.com': ":
        print(github_login)

    elif sys.argv[1] == f"Password for 'https://{github_login}@github.com': ":
        print(github_token)

    else:
        raise RuntimeError("Unknown mode")


if __name__ == "__main__":
    main()
