from src import WordTools as wTools
from src.WordContent import get_ETOSpec_SummarySheets
from src import SysTools


def Update_Date_ContractNumber(spec_path, contractNo, date):
    folder_list = SysTools.getFolderNames(spec_path)
    word_dic = SysTools.getWordNames(folder_list)

    for key, values in word_dic.items():
        folder = SysTools.checkResultPath("".join([key, 'Updated/']))
        for value in values:
            path = key + value
            name = folder + value
            wTools.update_wordInfo(path, contractNo, date, name)


def get_summarySheet(path, result_path):
    get_ETOSpec_SummarySheets(path, result_path)
