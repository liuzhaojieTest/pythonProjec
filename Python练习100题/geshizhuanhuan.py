import os
import comtypes.client


def ppt_to_pptx(input_file_path, output_file_path):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    # 打开PPT文件
    ppt = powerpoint.Presentations.Open(input_file_path)
    # 将PPT文件另存为PPTX文件
    ppt.SaveAs(output_file_path, FileFormat=24)
    # 关闭PPT文件和Powerpoint应用程序
    ppt.Close()
    powerpoint.Quit()


# 示例用法
input_file_path = "D:/Test/files/CSS提升.pptx"
output_file_path = "D:/Test/files/example.pot"
ppt_to_pptx(input_file_path, output_file_path)
