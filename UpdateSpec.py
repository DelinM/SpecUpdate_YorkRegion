import os

import SysTools as sysTools
import WordTools as wTools

spec_path = "/Users/delinmu/Documents/GitHub/ETO_Specification/Spec"
contractNo = "SSTR4559"
date = "Oct., 2022"


def updateSpec(spec_path, contractNo, date):
    folder_list = sysTools.getFolderNames(spec_path)
    word_dic = sysTools.getWordNames(folder_list)

    for key, values in word_dic.items():
        folder = sysTools.checkResultPath("".join([key, 'Updated/']))
        for value in values:
            path = key + value
            name = folder + value
            wTools.update_wordInfo(path, contractNo, date, name)