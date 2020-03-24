all:
	Rscript -e 'rmarkdown::render("Simulating-Supply.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Simulating-Supply.Rmd", output_format="beamer_presentation")'


slidy:
	Rscript -e 'rmarkdown::render("Simulating-Supply.Rmd", output_format="slidy_presentation")'


clean:
	rm Simulating-Supply.pdf Simulating-Supply.html
