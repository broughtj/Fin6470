# Makefile for IEEE formatted annotated bibliography.
#
# Author: Titus Barik (titus@barik.net)

annot.pdf: annot.tex annot.bib
	pdflatex annot
	bibtex annot
	pdflatex annot
	pdflatex annot
	@echo "================================================"
	@echo "All done! annot.pdf has been created. - Titus"
	@echo "================================================"

clean:
	rm -rf annot.log annot.pdf annot.blg annot.bbl annot.aux
