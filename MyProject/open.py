# num = 1
#
#
# def main():
#     desktop_path = "E:\\tests\\文档\\"   # 存放路径
#     count = 0
#     for i in :
#         full_path = desktop_path + "blxw_" + str(count) + f'.{}'    # 命名方式定义
#         file = open(full_path, 'w')     # 以写入的方式打开文件
#         file.write("hello python!")     # 写入的内容
#         print(full_path)
#         count += 1
#
#
# if __name__ == '__main__':
#     main()

# ws = open('E:/MP3/Layla蕾拉.mp3', 'rb')
# fp = ws.read()
# # print(fp)
# asd = open('E:/MP3/text.mp3', 'wb')
# asd.write(fp)
import moviepy.editor as mp
import pyflac
# 音频文件转换
clip = mp.AudioFileClip(r'E:/MP3/test.mp3')  # 替换实际路径
clip.write_audiofile(r'E:/MP3/test_bak.wav')  # 替换实际路径
# csv转xlsx
# from pptx import Presentation
#
# # 打开PPTX文件
# prs = Presentation('E:/tests/文档/test1.pptx')
# # 保存为PDF文件
# prs.save('E:/tests/文档/test1.dpss')
