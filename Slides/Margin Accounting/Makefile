all:
	Rscript -e 'rmarkdown::render("Margin-Accounting.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Margin-Accounting.Rmd", output_format="beamer_presentation")'


slidy:
	Rscript -e 'rmarkdown::render("Margin-Accounting.Rmd", output_format="slidy_presentation")'


clean:
	rm Margin-Accounting.pdf Margin-Accounting.html
