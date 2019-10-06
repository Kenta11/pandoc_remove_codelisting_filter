MANUSCRIPT  = sample.md
DOCUMENT    = $(subst .md,.pdf,$(MANUSCRIPT))

FILTER      = pandoc-crossref pandoc_remove_codelisting_filter 
OPTIONS     = $(addprefix --filter=,$(FILTER))

.SUFFIXES: .md .pdf

all: $(DOCUMENT)

$(DOCUMENT): $(MANUSCRIPT)
	pandoc $< -o $@\
		--pdf-engine=lualatex\
		$(OPTIONS)

clean:
	rm -rf *.aux *.log $(DOCUMENT)
