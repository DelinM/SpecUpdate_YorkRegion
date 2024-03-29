import pip

from src import WordTools as wTools
from src.WordContent import get_ETOSpecSummary
from src import SysTools


def Update_Date_ContractNumber(spec_path, contractNo, date):
    try:
        import docx
    except ModuleNotFoundError:
        print("module 'mutagen' is not installed")
        # or
        pip.main(['install', 'docx'])

    folder_list = SysTools.getFolderNames(spec_path)
    word_dic = SysTools.getWordNames(folder_list)

    for key, values in word_dic.items():
        folder = SysTools.checkResultPath("".join([key, 'Updated/']))
        for value in values:
            path = key + value
            name = folder + value
            wTools.update_wordInfo(path, contractNo, date, name)


def get_summarySheet(path, result_path):
    try:
        import docx
    except ModuleNotFoundError:
        print("module 'mutagen' is not installed")
        # or
        pip.main(['install', 'docx'])
    get_ETOSpecSummary(path, result_path)
