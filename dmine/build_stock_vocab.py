## To build vocabulary for stock market
##


import os
import sys
import csv
import PyPDF2
import tabula
import nltk
import pandas as pd
import numpy as np


class vocab:
    def __init__(self):
        print("Initing")

    def vReadPdfTables(self, fpath):
        pobj = open(fpath,'rb')
        pdfrd = PyPDF2.PdfFileReader(pobj)
        tables=tabula.read_pdf(fpath, pages="all", multiple_tables=True)
        return tables

    def vReadPdfText(self, fpath):
        txt = []
        pobj = open(fpath,'rb')
        pdfrd = PyPDF2.PdfFileReader(pobj)
        for i in range(0, pdfrd.numPages): 
          pg = pdfrd.getPage(i)
          txt.append(pg.extractText())
        return txt


## main ##

fpath = '/Users/tirmarri/Documents/technical/personal/investments/2020_picks.pdf'

vc = vocab()
txt = vc.vReadPdfText(fpath)
