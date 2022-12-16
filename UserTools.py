import os

import SysTools as sysTools
import WordTools as wTools
from WordContent import get_ETOSpec_SummarySheets


def Update_Date_ContractNumber(spec_path, contractNo, date):
    folder_list = sysTools.getFolderNames(spec_path)
    word_dic = sysTools.getWordNames(folder_list)

    for key, values in word_dic.items():
        folder = sysTools.checkResultPath("".join([key, 'Updated/']))
        for value in values:
            path = key + value
            name = folder + value
            wTools.update_wordInfo(path, contractNo, date, name)


def update_BidNumber(path, result_path):
    get_ETOSpec_SummarySheets(path, result_path)

# path = '/Users/delinmu/Documents/GitHub/ETO_Specification/Spec'
# update_BidNumber(path, path)