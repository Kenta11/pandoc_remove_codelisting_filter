#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandocfilters import toJSONFilter, Div, RawInline, RawBlock, Plain

def extractParameters(token):
    ret = {}

    if token['c'][0][0] != "":
        ret["label"]       = token['c'][0][0]
    if len(token['c'][0][1]) == 2:
        ret["language"]    = token['c'][0][1][0]
        if token['c'][0][1][1] == "numberLines":
            ret["numbers"]     = "left"
    for label, data in token['c'][0][2]:
        if   "startFrom" == label:
            ret["firstnumber"] = data
        elif "caption" == label:
            ret["caption"] = data
        elif "frame" == label:
            ret["frame"] = data

    return ret

def replaceCodelistingForLstlisting(token):
    begin_token = RawBlock('latex', '\\begin{codelisting}')
    end_token   = RawBlock('latex', '\\end{codelisting}')

    if (begin_token, end_token) != (token[1][0], token[1][3]):
        return token

    ret = [token[0], [Plain([])]] # a content of `Div` token

    # set begin command
    line = '\\begin{lstlisting}['
    params = extractParameters(token[1][2])
    params_strings = ["{}={}".format(key, item) for key, item in params.items()]
    ret[1][0]['c'].append(RawInline('latex', line + ",".join(params_strings) + "]\n"))

    # set the source code
    for line in token[1][2]['c'][1].split('\n'):
        ret[1][0]['c'].append(RawInline('latex', line+"\n"))

    # set end command
    ret[1][0]['c'].append(RawInline('latex', '\\end{lstlisting}'))

    return Div(*ret)

def myaction(key, value, format_, meta):
    if key != 'Div':
        return

    for content in value:
        if type(content[0]) != dict:
            continue

        for sub_content in content:
            if sub_content['t'] == 'CodeBlock':
                if len(value[0]) != 3:
                    continue
                elif len(value[1]) != 4:
                    continue

                return replaceCodelistingForLstlisting(value)

def main():
    toJSONFilter(myaction)

if __name__ == "__main__":
    main()
