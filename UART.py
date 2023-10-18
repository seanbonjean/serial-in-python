import serial
import time

rx_chr = 'x'  # 串口接收字符暂存
rx_str = ''  # 串口接收到的字符串
count = 0  # 发送字节计数

try:
    # 打开串口
    ser1 = serial.Serial("COM7", 115200, timeout=5)

    if ser1.isOpen():  # 判断串口是否成功打开
        print("打开串口成功")
        print(ser1.name)  # 输出串口号
    else:
        print("打开串口失败")

    time.sleep(2)

    # 串口发送
    count += ser1.write("abcde;".encode("ascii"))
    print("发送字节数：", count)
    count = 0

    # 串口接收
    while rx_chr != ';':  # 分号表示一帧结束
        rx_chr = ser1.read().decode('ascii')
        rx_str += rx_chr
    print(rx_str)

    # 关闭串口
    ser1.close()

except Exception as e:
    print("出现异常：", e)
