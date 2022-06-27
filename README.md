# chromeutil
`chromeutil` is a self-contained, third-party utility for working with data saved by the Chrome browser. It was created by Gabriel Konar-Steenberg as a side project in the summer of 2022. The goal is to 

`chromeutil` should only be used if you know what you're doing and have backed up your data! Though I aim to avoid data loss, the nature of the program is such that if it is used in certain ways or if Chrome changes how it deals with its data, data loss may occur. See the disclaimer below.

## Features
Currently, `chromeutil` can:
 * List the profiles a user has installed and what directories they correspond to

Planned features for `chromeutil` include:
 * Given the appropriate credentials, provide access to the passwords database even if it was created on a different computer
 * Disable and reenable profiles
 * Export a profile's history, bookmarks, etc. databases to a more human-readable file format

## Installation
The only dependency is a recent version of Python 3. `chromeutil` is then installed by cloning the repository or simply downloading the `chromeutil.py` file.

## Usage
```
usage: chromeutil.py [-h] [-r PATH] subcommand ...

A self-contained, third-party utility for working with data saved by the Chrome browser. Created by Gabriel Konar-Steenberg.

positional arguments:
  subcommand
    profiles            List the profiles ("people") installed

options:
  -h, --help            show this help message and exit
  -r PATH, --root PATH  Path to the 'Chrome' root directory to use if it is not located in the usual place.
```

## Disclaimer
THIS WORK IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. THE ENTIRE RISK OF USING THIS WORK IS WITH YOU, INCLUDING BUT NOT LIMITED TO LOSS OF DATA. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM THE USE OF THIS WORK, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH. ALL RIGHTS RESERVED.
