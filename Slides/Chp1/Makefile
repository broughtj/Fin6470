all:
	Rscript -e 'rmarkdown::render("Chapter1.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter1.Rmd", output_format="beamer_presentation")'


ioChapter1:
	Rscript -e 'rmarkdown::render("Chapter1.Rmd", output_format="ioChapter1_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter1.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter1.pdf Chapter1.html
