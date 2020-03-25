all:
	Rscript -e 'rmarkdown::render("Mechanics.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Mechanics.Rmd", output_format="beamer_presentation")'


slidy:
	Rscript -e 'rmarkdown::render("Mechanics.Rmd", output_format="slidy_presentation")'


clean:
	rm Mechanics.pdf Mechanics.html
