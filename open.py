num = 100


def main():
    open_path = "D:\\Test\\"
    count = 0
    for i in range(num):
        full_path = open_path + "blush_" + str(count) + '.txt'
        fail = open(full_path, 'w')
        fail.write('Hello python!')
        count += 1


if __name__ == '__main__':
    main()
import subprocess
input_file = 'input.mp4'
output_file = 'output.avi'
 # 调用 FFmpeg 命令行工具进行视频格式转换
subprocess.run(['ffmpeg', '-i', input_file, output_file])
print('视频格式转换完成！')