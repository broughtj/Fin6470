all:
	Rscript -e 'rmarkdown::render("Chapter02.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter02.Rmd", output_format="beamer_presentation")'


ioChapter02:
	Rscript -e 'rmarkdown::render("Chapter02.Rmd", output_format="ioChapter02_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter02.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter02.pdf Chapter02.html Chapter02.tex
