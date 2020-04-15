all:
	Rscript -e 'rmarkdown::render("Culp-App.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Culp-App.Rmd", output_format="beamer_presentation")'


ioCulp-App:
	Rscript -e 'rmarkdown::render("Culp-App.Rmd", output_format="ioCulp-App_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Culp-App.Rmd", output_format="slidy_presentation")'


clean:
	rm Culp-App.pdf Culp-App.html Culp-App.tex
