"""extract_es_grammar.py - Extract the grammar from the ECMAScript spec

To run this script, you first need to get the source of the version of
the ECMAScript spec you're interested in.

    cd ../..
    mkdir tc39
    cd tc39
    git clone git@github.com:tc39/ecma262.git

Then set up python:

    cd ../jsparagus
    python3 -m venv venv
    . venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

Finally:

    make js_parser/es.esgrammar

"""

import html5lib
from textwrap import dedent


def extract(filename):
    with open(filename, "rb") as f:
        document = html5lib.parse(f)

    for e in document.iter("{http://www.w3.org/1999/xhtml}emu-grammar"):
        if e.attrib.get("type") == "definition":
            print(dedent(e.text))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("usage:  python -m js_parser.extract_es_grammar path/to/tc39/ecma262/spec.html")
    else:
        extract(sys.argv[1])
