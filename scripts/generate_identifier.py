#! /usr/bin/env python3

# Nadhif Ikbar Wibowo 2021
# Generate data-identifier identifier for a document

import sys
import os.path as path
from bs4 import BeautifulSoup


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No file specified")
        sys.exit(1)

    path = path.realpath(sys.argv[1])
    with open(path, 'r') as doc:
        soup = BeautifulSoup(doc, 'lxml')
        article = soup.body.article
        print(article.attrs)