import SysTools as sysTools
import WordTools as wTools

spec_path = sysTools.getFilePath()
folder_list = sysTools.getFolderNames(spec_path)
word_dic = sysTools.getWordNames(folder_list)
word_list = wTools.getWordPaths(word_dic)


wordPath = '/Users/delinmu/Documents/GitHub/ETO_Specification/Files/DIV2/02241 Provide Water Control Plan Dewatering and Discharge Plan.DOCX'
contractNo = "SSTR4559"
date = "Oct., 2022"

wTools.update_wordInfo(wordPath, contractNo, date)
