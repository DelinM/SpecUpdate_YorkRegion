import SysTools as sysTools
import SpecData as data
"""
spec container: hashmap <String, list>

key: spec number -> String

values:
value 0: div_number -> integer
value 1: div_name -> string
value 2: Name (full name of the spec) -> string
value 3: york_true (if this is an original york region spec) -> boolean
value 4: eto_true (if ETO folder has this spec) -> boolean
value 5: bid_true (should it included in Bid form) -> boolean
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

