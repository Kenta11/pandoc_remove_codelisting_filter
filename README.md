# pandoc_remove_codelisting_filter

## Overview

pandoc_remove_codelisting_filter is a filter for removing `codelisting` command of LaTeX.
List may be cut off since [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) uses the `codelisting` command for lists.
pandoc-remove-codelisting-filter ensure that lists in PDF are displayed properly.

## Requirements

- Python3.x
- pandocfilters

## Install

```
$ pip install https://github.com/Kenta11/pandoc_remove_codelisting_filter
```

## Usage

```
$ pandoc sample.md -o sample.pdf\
         --pdf-engine=lualatex\
         --filter=pandoc-crossref --filter=pandoc_remove_codelisting_filter
```

## Tutorial

Refer [tutorial](tutorial).

## License

[MIT License](LICENSE)

## Contact

Author: Kenta Arai
Twitter: [@isKenta14](https://twitter.com/isKenta14)
