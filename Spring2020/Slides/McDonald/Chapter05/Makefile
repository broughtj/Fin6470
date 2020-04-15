all:
	Rscript -e 'rmarkdown::render("Chapter05.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter05.Rmd", output_format="beamer_presentation")'


ioChapter05:
	Rscript -e 'rmarkdown::render("Chapter05.Rmd", output_format="ioChapter05_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter05.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter05.pdf Chapter05.html
