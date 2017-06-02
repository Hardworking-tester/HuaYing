# encoding:utf-8
# author:wwg
import os
import xlrd
DIR="G:\\pic"
file_list=[]
#按文件修改时间升序排列
def compare(x, y):
    stat_x = os.stat(DIR + "\\" + x)
    stat_y = os.stat(DIR + "\\" + y)
    if stat_x.st_mtime < stat_y.st_mtime:
        return -1
    elif stat_x.st_mtime > stat_y.st_mtime:
        return 1
    else:
        return 0
iterms = os.listdir(DIR)
iterms.sort(compare)
for iterm in iterms:
    print type(iterm)
    print iterm.split(".")[0]
    file_list.append(DIR + "\\" + iterm.split(".")[0])
print file_list


#修改文件名
# os.rename("G:\\pic\\1.png","G:\\pic\\wwg1.png")




#操作excel
def getData():
    excel_path="G:\\pic\\student_data.xls"
    data=xlrd.open_workbook(excel_path)
    sheet=data.sheet_by_index(0)
    rows=sheet.nrows
    cols=sheet.ncols
    for row_number in range(rows):
        print str(int(sheet.cell_value(row_number,1)))
# row_col_list=[]
# for row_number in range(rows):
#     for col_number in range(cols):
#         if sheet.cell_value(row_number,col_number)==key:
#             row_col_list.append(row_number)
#             row_col_list.append(col_number)
#             return row_col_list