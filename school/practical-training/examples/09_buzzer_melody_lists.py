#1、导入第三方库
import time
from MyClass import pymata4EX

#2、定义常量
TONE_PIN = 4  # 蜂鸣器连接的管脚
CL = [0, 262, 294, 330, 349, 392, 440, 494]  # C调音符（低音）
CM = [0, 523, 587, 659, 698, 784, 880, 988]  # C调音符（中音）
CH = [0, 1046, 1175, 1318, 1397, 1568, 1760, 1976]  # C调音符（高音）

#3、连接实验箱
board = pymata4EX.Pymata4EX()  # 创建Pymata4EX对象，连接到Arduino板子

#4、定义蜂鸣器管脚
board.set_pin_mode_tone(TONE_PIN)  # 设置管脚为蜂鸣器模式

#5、初始化，播放一个音符序列以测试蜂鸣器
print("正在测试蜂鸣器...")  # 打印正在播放的歌曲名称
for i in range(8):
    board.play_tone_continuously(TONE_PIN, CM[i])  # 持续播放音符
    time.sleep(0.5)  # 音符持续0.5秒
    board.play_tone_continuously(TONE_PIN, CL[0])  # 播放空音符
    time.sleep(0.1)  # 空音符持续0.1秒
time.sleep(2)
# 播放生日快乐
def play_happy_birthday():
    song_happy_birthday = [
        CL[5], CL[5], CL[6], CL[5], CM[1], CL[7],  # 祝你生日快乐
        CL[5], CL[5], CL[6], CL[5], CM[2], CM[1],  # 祝你生日快乐
        CL[5], CL[5], CM[5], CM[3], CM[1], CL[7], CL[6],  # 祝你生日快乐，亲爱的朋友
        CM[4], CM[4], CM[3], CM[1], CM[2], CM[1]   # 祝你生日快乐
    ]
    beat_happy_birthday = [
        1, 1, 2, 2, 2, 4,  # 祝你生日快乐
        1, 1, 2, 2, 2, 4,  # 祝你生日快乐
        1, 1, 2, 2, 2, 2, 4,  # 祝你生日快乐，亲爱的朋友
        1, 1, 2, 2, 2, 4  # 祝你生日快乐
    ]
    print("正在播放：生日快乐")  # 打印正在播放的歌曲名称
    for i in range(len(song_happy_birthday)):
        board.play_tone_continuously(TONE_PIN, song_happy_birthday[i])  # 播放音符
        time.sleep(beat_happy_birthday[i] * 0.25)  # 根据节拍等待
        board.play_tone_continuously(TONE_PIN, CL[0])  # 播放空音符
        time.sleep(0.08)  # 空音符间隔

# 播放小星星
def play_star():
    song_star = [
        CM[1], CM[1], CM[5], CM[5], CM[6], CM[6], CM[5],    # 一闪一闪亮晶晶
        CM[4], CM[4], CM[3], CM[3], CM[2], CM[2], CM[1],     # 满天都是小星星
        CM[5], CM[5], CH[4], CM[4], CM[3], CM[3], CM[2],    # 挂在天上放光明
        CM[5], CM[5], CM[4], CM[4], CM[3], CM[3], CM[2]     # 好像许多小眼睛
    ]
    beat_star = [
        2, 2, 2, 2, 2, 2, 4,     # 一闪一闪亮晶晶
        2, 2, 2, 2, 2, 2, 4,     # 满天都是小星星
        2, 2, 2, 2, 2, 2, 4,    # 挂在天上放光明
        2, 2, 2, 2, 2, 2, 4      # 好像许多小眼睛
    ]
    print("正在播放：小星星")  # 打印正在播放的歌曲名称
    for i in range(len(song_star)):
        board.play_tone_continuously(TONE_PIN, song_star[i])  # 播放音符
        time.sleep(beat_star[i] * 0.25)  # 根据节拍等待
        board.play_tone_continuously(TONE_PIN, CL[0])  # 播放空音符
        time.sleep(0.08)  # 空音符间隔

# 主函数：播放两首歌曲
def main():
    try:
        while True:
            # 播放生日快乐
            play_happy_birthday()
            time.sleep(1)  # 两首歌之间间隔1秒

            # 播放小星星
            play_star()
            time.sleep(1)  # 两首歌之间间隔1秒
    except (KeyboardInterrupt, RuntimeError):
        print("程序终止，关闭声音")  # 捕捉键盘中断或运行时错误
        board.play_tone_off(TONE_PIN)  # 关闭声音
        time.sleep(0.1)  # 短暂等待
    finally:
        print("程序已退出，连接已中断")  # 程序结束时打印信息
        board.shutdown()  # 关闭与硬件的连接

# 启动主函数
if __name__ == "__main__":
    main()  # 调用主函数
