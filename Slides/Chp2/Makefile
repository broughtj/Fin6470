all:
	Rscript -e 'rmarkdown::render("Chapter2.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter2.Rmd", output_format="beamer_presentation")'


ioChapter2:
	Rscript -e 'rmarkdown::render("Chapter2.Rmd", output_format="ioChapter2_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter2.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter2.pdf Chapter2.html Chapter2.tex
