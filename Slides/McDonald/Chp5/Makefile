all:
	Rscript -e 'rmarkdown::render("Chapter5.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter5.Rmd", output_format="beamer_presentation")'


ioChapter5:
	Rscript -e 'rmarkdown::render("Chapter5.Rmd", output_format="ioChapter5_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter5.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter5.pdf Chapter5.html
