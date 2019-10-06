#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandocfilters import toJSONFilter, CodeBlock

def myfilter(key, value, format_, meta):
    if key != 'Div':
        return

    for content in value:
        if type(content[0]) != dict:
            continue

        for sub_content in content:
            if sub_content['t'] == 'CodeBlock':
                return CodeBlock(*sub_content['c'])

def main():
    toJSONFilter(myfilter)

if __name__ == "__main__":
    main()
