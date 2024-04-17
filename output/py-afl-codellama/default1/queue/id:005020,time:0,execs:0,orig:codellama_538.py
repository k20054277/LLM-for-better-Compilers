#!/usr/bin/env python

import os

def main():
    # Get the current version number from the version control system
    current_version = get_current_version()

    # Check if the current version is a new version or not
    if current_version == None:
        print("This is a new version")
    else:
        print("This is an updated version")

def get_current_version():
    # Get the latest commit from the version control system
    commit = os.popen('git log -1').read().strip()

    # Parse the commit message to extract the version number
    match = re.search(r'^Version: (\d+)\.(\d+)\.(\d+)', commit)
    if match:
        return match.group(1) + "." + match.group(2) + "." + match.group(3)
    else:
        return None

if __name__ == '__main__':
    main()