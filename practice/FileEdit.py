# encoding:utf-8
# author:wwg
import os
import xlrd
class FileEdit():
    """
    注意事项：
        1、图片存储路径和excel存储路径不要放到同一个文件夹下。
        2、存储图片的文件夹不要放其他东西，只放图片。
        3、图片文件夹下文件的数量和excel中学号的数量要一致
    """
    #获取文件夹下文件
    def getFileList(self,DIR):
        DIR = DIR
        file_list = []
        iterms = os.listdir(DIR)
        iterms.sort
        for iterm in iterms:
            file_list.append(DIR + "\\" +iterm)
        return file_list


    #获取excel数据
    def getExcelData(self,excel_path):
        excel_data_list=[]
        excel_path = excel_path
        data = xlrd.open_workbook(excel_path)
        sheet = data.sheet_by_index(0)
        rows = sheet.nrows
        for row_number in range(1,rows):
            # print str(int(sheet.cell_value(row_number, 1)))
            excel_data_list.append(str(int(sheet.cell_value(row_number, 1))))
        return excel_data_list

if __name__=="__main__":
    DIR = "G:\\pic"    #图片存储路径
    excel_path = "G:\\excel\\student_data.xls"          #excel存储路径
    houzhui_list=[]
    new_data_list=[]
    file_list=FileEdit().getFileList(DIR)
    excel_data_list=FileEdit().getExcelData(excel_path)
    if file_list.__len__()==excel_data_list.__len__():
        for m in file_list:
            houzhui_list.append(m.split(".")[1])
        for i in range(excel_data_list.__len__()):
            new_data_list.append(DIR + "\\" +excel_data_list[i]+"."+houzhui_list[i])
        for pp in range(file_list.__len__()):
            os.rename(file_list[pp],new_data_list[pp])
        print "everything is ok!!!"
    else:
        print "The length is not equal,please check it"