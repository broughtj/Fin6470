all:
	Rscript -e 'rmarkdown::render("Chapter9.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter9.Rmd", output_format="beamer_presentation")'


ioChapter9:
	Rscript -e 'rmarkdown::render("Chapter9.Rmd", output_format="ioChapter9_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter9.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter9.pdf Chapter9.html
