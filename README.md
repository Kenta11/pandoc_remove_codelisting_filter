# pandoc_remove_codelisting_filter

[![LICENSE](https://img.shields.io/github/license/Kenta11/pandoc_remove_codelisting_filter)](LICENSE)

## Overview

pandoc_remove_codelisting_filter is the filter in order to render code blocks into multiple pages of a PDF file. If using pandoc and [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref), perhaps code blocks go out of pages due to `codelisting` commands in a LaTeX file. Therefore the filter replaces `codelisting` commands with `lstlisting` commands.

## Requirements

- Python 3.8
- pandocfilters

## Install

You can install executable `pandoc_remove_codelisting_filter` via pip.

```
$ pip install git+https://github.com/Kenta11/pandoc_remove_codelisting_filter
```

## Usage

Set `pandoc_remove_codelisting_filter` in an argument `--filter`. You must set the filter after `pandoc-crossref`.

```
$ pandoc sample.md -o sample.pdf --filter=pandoc-crossref --filter=pandoc_remove_codelisting_filter
```

If LaTeX commands require listings package, add the following YAML block in your markdown file.

```
---
header-includes:
    - \usepackage{listings}
---
```

## Tutorial

Refer [tutorial](tutorial).

## Contact

- Author: Kenta Arai
    - Twitter: [@isKenta14](https://twitter.com/isKenta14)
