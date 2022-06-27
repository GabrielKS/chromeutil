#!/usr/bin/env python3
"""chromeutil: a self-contained, third-party utility for working with data saved by the Chrome browser.
Created by Gabriel Konar-Steenberg."""

import sys
import argparse
from pathlib import Path
import json

defaults = {
    "root": Path("~/Library/Application Support/Google/Chrome")
}

def get_local_state(root):
    """Get the contents of the relevant 'Local State' file"""
    lspath = root.expanduser() / "Local State"
    if lspath.exists():
        with open(lspath, 'r', encoding="utf8") as lsfile:
            lsdata = json.load(lsfile)
            return lsdata
    else:
        print(f"Could not find the necessary file '{lspath}'. Please check your root.")
        sys.exit(1)
        return None

def list_profiles(args):
    """List the profiles ("people") installed"""
    local_state = get_local_state(args.root)
    profiles = local_state["profile"]["info_cache"]
    if len(profiles) == 0:
        print("No profiles found")
        return
    print(f"{len(profiles)} profiles found:")

    names = []
    for dir_name in profiles:
        pcontents = profiles[dir_name]

        # This logic was inferred from not too many samples; it might be incorrect
        if len(pcontents["gaia_given_name"]) > 0:
            if pcontents["is_using_default_name"]:
                menu_name = pcontents['gaia_given_name']
            else:
                menu_name = f"{pcontents['gaia_given_name']} ({pcontents['name']})"
        else: menu_name = pcontents["name"]

        title_name = pcontents["name"]
        names.append((dir_name, menu_name, title_name))

    # Sort by directory as if profile numbers were zero-padded to three digits
    # names.sort(key=lambda e: f"Profile {int(e[0].split(' ')[1]):03d}" if e[0].startswith("Profile ") else e[0])
    # Sort by menu name, as the menu does
    names.sort(key=lambda e: e[1])
    # Ad-hoc pretty printing
    min_col_length = 12
    col_lengths = [max([len(e[n]) for e in names]+[min_col_length]) for n in range(len(names[0]))]
    row_format = f"{{:<{col_lengths[0]}}} {{:<{col_lengths[1]}}} {{:<{col_lengths[2]}}}"
    print(row_format.replace('<', '^').format("Directory", "Menu Name", "Display Name"))
    # print("-"*(sum(col_lengths)+6))
    for row in names:
        print(row_format.format(*row))

def parse_args():
    """Parse the command-line arguments"""
    superparser = argparse.ArgumentParser(description="""A self-contained, third-party utility for working with data\
        saved by the Chrome browser. Created by Gabriel Konar-Steenberg.""")
    superparser.add_argument("-r", "--root", type=Path, metavar="PATH", default = defaults["root"],
        help="path to the 'Chrome' root directory to use if it is not located in the usual place.")
    subparsers = superparser.add_subparsers(dest="subcommand", metavar="subcommand")
    subparsers.required = True

    # PROFILES
    parser_list_profiles = subparsers.add_parser("profiles", help="list the profiles (\"people\") installed")
    parser_list_profiles.set_defaults(func=list_profiles)

    args = superparser.parse_args()
    return args

def main():
    """Get the command-line arguments and delegate to the appropriate subcommand"""
    args = parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
