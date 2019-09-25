

#c : carthage
#q : quartermark

rm := /bin/rm
perl := /usr/bin/env perl
view_pdf := @evince
#GRAYSCALE := --grayscale
GRAYSCALE :=


carthage : carthage.txt
	@$(perl) sec2pdf --data $< --output $@.pdf    \
                --paper 8.5x11 $(GRAYSCALE)  \
                --metadata carthage.meta     \
                --highlight --cleanup -b     \
                -s "Carthage"
	$(view_pdf) $@.pdf


quartermark : quartermark.txt
	@$(perl) sec2pdf --data $< --output $@.pdf \
                --paper 8.5x11 $(GRAYSCALE)        \
                --firsthex 0901                    \
                --metadata quartermark.meta        \
                --highlight --cleanup -b           \
                -s "Quartermark"
	$(view_pdf) $@.pdf


middle : middle.txt
	@$(perl) sec2pdf --data $< --output middle.pdf \
                --paper 8.5x11  \
                --firsthex 0301 \
                $(GRAYSCALE)    \
                --metadata middle.meta \
                --highlight --cleanup -b -s "Carthage / Quartermark"
	$(view_pdf) middle.pdf


both : large.txt
	@$(perl) sec2pdf --data $< --output $@.pdf    \
                -l $(GRAYSCALE)  \
                --metadata large.meta     \
                -t 16x10 \
                --highlight --cleanup -b     \
                -s "Carthage/Quartermark"
	$(view_pdf) $@.pdf


.PHONEY: clean
clean: ; $(rm) --force *.pdf
