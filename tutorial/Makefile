MANUSCRIPT = sample.md
DOCUMENT   = $(subst .md,.pdf,$(MANUSCRIPT))

FILTER     = pandoc-crossref pandoc_remove_codelisting_filter 
OPTIONS    = --pdf-engine=lualatex\
             --listings\
             $(addprefix --filter=,$(FILTER))

.SUFFIXES: .md .pdf

.PHONY: all clean

all: $(DOCUMENT)

$(DOCUMENT): $(MANUSCRIPT)
	pandoc $< -o $@ $(OPTIONS)

clean:
	rm -rf *.aux *.log $(DOCUMENT)
