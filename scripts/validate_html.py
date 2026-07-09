#!/usr/bin/env python3
"""Lightweight HTML sanity check for the Lantern brochure.

Fails (exit 1) if the document does not parse, any required interactive
hook id is missing, or any block-level tag is left unbalanced. This is the
gate that runs in CI on every push so a broken deploy never reaches Vercel.

Usage: python scripts/validate_html.py [path]
"""
import html.parser
import sys
from pathlib import Path

REQUIRED_IDS = {"nodes", "incident", "simBtn", "resetBtn", "ts", "mo", "yr"}
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


class Checker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"Unexpected </{tag}> with empty stack")
            return
        if self.stack[-1] != tag:
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.errors.append(f"Unclosed <{self.stack[-1]}> before </{tag}>")
                    self.stack.pop()
                if self.stack:
                    self.stack.pop()
            else:
                self.errors.append(f"Stray </{tag}>")
        else:
            self.stack.pop()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("index.html")
    text = path.read_text(encoding="utf-8")
    c = Checker()
    c.feed(text)
    c.close()

    ok = True
    if c.stack:
        print("ERROR: unclosed tags at EOF ->", c.stack)
        ok = False
    for e in c.errors:
        print("ERROR:", e)
        ok = False
    missing = REQUIRED_IDS - c.ids
    if missing:
        print("ERROR: missing required interactive hook ids ->", missing)
        ok = False

    if ok:
        print(f"OK: {path} parsed cleanly; all interactive hooks present.")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
