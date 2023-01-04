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


def getFileNames(filepath):
    file_dic = {}
    for path in filepath:
        files = os.listdir(path)
        file_paths = [f for f in files if not f.startswith('.')]
        file_dic[path] = file_paths

    return file_dic


def checkResultPath(path):
    if not os.path.exists(path):
        # create directory
        os.makedirs(path)
    return path


def getSpecNumber(file_name):
    result = ""
    length = len(file_name)
    for i in range(length):
        char = file_name[i]
        if i < length - 1 and char.isalpha() == True and file_name[i + 1] == " ":
            result = result + char
            continue
        if i < length - 1 and char == '-' and file_name[i + 1] == " ":
            result = result.strip()
            return result
        else:
            if char.isalpha() == True or char == '_':
                result = result.strip()
                return result
            else:
                result = result + char
    result = result.strip()
    return result


def getSpecName(file_name, SpecNumber):
    file_name = file_name.replace(SpecNumber, "")
    file_name = file_name.split('.')[0]
    file_name = file_name.strip()
    return file_name
