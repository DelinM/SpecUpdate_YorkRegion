import SysTools as sysTools
import SpecData as data

import docx
from docx import Document
import WordContentUpdate as wordu
"""
spec container: hashmap <String, list>

key: spec number -> String

values:
value 0: div_number -> integer
value 1: div_name -> string
value 2: Name (full name of the spec) -> string
value 3: york_true (if this is an original york region spec) -> boolean
value 4: eto_true (if ETO folder has this spec) -> boolean
value 5: bid_true (should it included in Bid form) -> value
"""

"""

deleted item
01000
01720
01740
01770
07570
07900
Div 12
Div 14
"""

def getDivName(number):
    return data.div_dic.get(number)


def getYorkSpec():
    path = "/Users/delinmu/Documents/GitHub/ETO_Specification/YorkOriginal"
    folder_list = sysTools.getFolderNames(path)
    file_dic = sysTools.getFileNames(folder_list)
    spec_dic = {}
    for division, specs in file_dic.items():

        div_fullname = division.split('/')[-2]
        div_fullname = div_fullname.split(' ')

        # key
        for spec in specs:
            if len(spec) == 0:
                continue

            if len(spec) > 0 and spec[0].isalpha() == True:
                continue
            key = sysTools.getSpecNumber(spec)
            # value 0
            div_number = div_fullname[1]
            # value 1
            div_name = data.div_dic.get(div_number)
            # value 2
            spec_name = sysTools.getSpecName(spec, key)
            # value 3
            york_true = True
            #value 4
            eto_true = False
            #value 5
            bid_true= False
            spec_list = [div_number, div_name, spec_name, york_true, eto_true, bid_true]
            spec_dic[key] = spec_list

    return spec_dic

def getETOSpec(path):
    folder_list = sysTools.getFolderNames(path)
    file_dic = sysTools.getFileNames(folder_list)
    result_dic = data.yorkspec_dic

    for division, specs in file_dic.items():
        print(division)
        print(specs)
        for spec in specs:
            if len(spec) == 0:
                continue
            if len(spec) > 0 and spec[0].isalpha() == True:
                continue
            key = sysTools.getSpecNumber(spec)
            if key in result_dic:
                spec_list = result_dic.get(key)
                # value 4
                eto_true = True
                spec_list[4] = eto_true
                # value 5
                bid_true = checkBid()
                spec_list[5] = bid_true
                result_dic[key] = spec_list
            elif key not in result_dic:
                div_fullname = division.split('/')[-2]
                div_fullname = div_fullname.split(' ')
                # value 0
                div_number = div_fullname[1]
                # value 1
                div_name = data.div_dic.get(div_number)
                # value 2
                spec_name = sysTools.getSpecName(spec, key)
                # value 3
                york_true = False
                # value 4
                eto_true = True
                # value 5
                bid_true = checkBid()
                spec_list = [div_number, div_name, spec_name, york_true, eto_true, bid_true]
                result_dic[key] = spec_list
    return result_dic


def checkBid(path):
    file = open(path, 'rb')
    try:
        # avoid file is not word doc.
        document = Document(file)
    except:
        return

    n = 0

    for paragraph in document.paragraphs:
        print(n)
        if "all costs" in paragraph.text.lower() and "bid form" in paragraph.text.lower():
            paragraph.text = "small dick"
        n = n + 1

    for paragraph in document.paragraphs:
        print(n)
        print(paragraph.text)
        n = n + 1

    document.save(path)
    file.close()
checkBid('/Users/delinmu/Documents/GitHub/ETO_Specification/YorkOriginal/Division 01 - General Requirements/01820B Training Schedule.xlsx')