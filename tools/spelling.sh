#!/bin/bash
LANGUAGE=$1
hunspell -d $LANGUAGE -u dump_biblical_text > biblical_text_unknowns
hunspell -d $LANGUAGE -u dump_header > header_unknowns
hunspell -d $LANGUAGE -u dump_part_titles > part_titles_unknowns
hunspell -d $LANGUAGE -u dump_section_titles > section_titles_unknowns
