import docx
from docx import Document
import WordContentUpdate as wordu

def getWordPaths(dic):
    word_path = []

    for key, values in dic.items():
        for value in values:
            word_path.append(key + value)
    return word_path

def update_wordInfo(wordPath, contractNo, date):
    file = open(wordPath, 'rb')
    document = Document(file)

    section = document.sections[0]

    # update odd page header
    wordu.update_oddHeader(section, contractNo, date)
    wordu.add_page_number_odd(section.header.paragraphs[2], date)

    # update even page header
    wordu.update_evenHeader(section, contractNo)
    wordu.add_page_number_even(section.even_page_header.paragraphs[2], date)

    document.save("your_docdsad.docx")
    file.close()
