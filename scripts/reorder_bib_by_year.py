#!/usr/bin/python3
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

import sys


if __name__ == "__main__":
    # This script takes in a bibtex file and arranges it by year reverse chronologically
    if len(sys.argv) < 2:
        print("Please enter the name of the bibtex file.")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as bib_file:
        bib_database = bibtexparser.load(bib_file)

    # Now sort in reverse chronological order.
    new_db = BibDatabase()
    new_db.entries = sorted(bib_database.entries, key=lambda x: -int(x["year"]))
    writer = BibTexWriter()
    writer.order_entries_by = "year"

    with open("out.bib", "w") as bib_file:
        bib_file.write(writer.write(new_db))
