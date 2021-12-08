#! /usr/bin/env python3.7
import os
import json
import sys

from jinja2 import Template


def main():
    os.chdir(os.path.dirname(__file__))

    projs = json.load(open("projects.json"))
    tag_count = {}

    for p in projs:
        for tag in p['tags']:
            if tag not in tag_count:
                tag_count[tag] = 0
            tag_count[tag] += 1
        if 'url' not in p:
            p['url'] = "https://github.com/kign/" + p['name']
        if 'img' not in p:
            p['img'] = f"img/{p['name']}.png"

    tag_name = json.load(open("tags.json"))
    missing = [tag for tag in tag_count if tag not in tag_name]

    if len(missing) > 0:
        print("Missing mapping:", ", ".join(missing), file=sys.stderr)
        exit(1)

    with open("index.jinja2") as fh:
        t = Template(fh.read())

    with open("../index.html", "w") as fh:
        fh.write(t.render(projects=projs, 
                          tags=sorted(tag_count.keys(), key=lambda x: -tag_count[x]),
                          tag_name=tag_name,
                          tag_count=tag_count))


main()
