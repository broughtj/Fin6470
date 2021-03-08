all:
	Rscript -e 'rmarkdown::render("Chapter03.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter03.Rmd", output_format="beamer_presentation")'


slidy:
	Rscript -e 'rmarkdown::render("Chapter03.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter03.pdf Chapter03.html
