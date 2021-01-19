all:
	Rscript -e 'rmarkdown::render("Chapter09.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter09.Rmd", output_format="beamer_presentation")'


ioChapter09:
	Rscript -e 'rmarkdown::render("Chapter09.Rmd", output_format="ioChapter09_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter09.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter09.pdf Chapter09.html
