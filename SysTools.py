from glob import glob
import os
import re


def getFilePath():
    filePath = input("Please provide file path\n")
    return filePath


def getFolderNames(filepath):
    folders = os.listdir(filepath)
    folders = [filepath + "/" + f + "/" for f in folders if os.path.isdir(os.path.join(filepath, f))]
    return folders


def getWordNames(filepath):
    '''method to extract word names with ext: .docx adn .DOCX'''

    word_dic = {}

    for path in filepath:
        files = os.listdir(path)
        word_files = [f for f in files if re.search(r'.docx$', f, flags=re.IGNORECASE)]
        word_dic[path] = word_files
    return word_dic
