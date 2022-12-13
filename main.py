import os

import SysTools as sysTools
import WordTools as wTools

contractNo = "SSTR4559"
date = "Oct., 2022"


spec_path = sysTools.getFilePath()
folder_list = sysTools.getFolderNames(spec_path)
word_dic = sysTools.getWordNames(folder_list)
word_list = wTools.getWordPaths(word_dic)




for key, values in word_dic.items():
    folder = sysTools.checkResultPath("".join([key, 'Updated/']))
    for value in values:
        path = key + value
        name = folder + value
        print(name)
        wTools.update_wordInfo(path, contractNo, date, name)