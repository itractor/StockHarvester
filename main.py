# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PyPDF2
from tabula import read_pdf
from tabulate import tabulate


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def find_key_figures_page(pdf_file):

    #WIP use PyPDF2 to find the page with the key figures then use the page number with tabula
    #reader = PyPDF2.PdfReader(pdf_file)
    #page = reader.pages[30]
    #print(page.extract_text())


    # reads table from pdf file
    df = read_pdf(pdf_file, pages="31")  # address of pdf file
    print(tabulate(df))


if __name__ == '__main__':
    find_key_figures_page("example.pdf")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
