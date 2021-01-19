all:
	Rscript -e 'rmarkdown::render("Retrospect.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Retrospect.Rmd", output_format="beamer_presentation")'


ioRetrospect:
	Rscript -e 'rmarkdown::render("Retrospect.Rmd", output_format="ioRetrospect_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Retrospect.Rmd", output_format="slidy_presentation")'


clean:
	rm Retrospect.pdf Retrospect.html Retrospect.tex
