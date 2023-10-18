import serial
import time

rx_chr = 'x'  # 串口接收字符暂存

try:
    # 打开串口
    ser1 = serial.Serial("COM7", 115200, timeout=5)

    if ser1.isOpen():  # 判断串口是否成功打开
        print("打开串口成功")
        print(ser1.name)  # 输出串口号
    else:
        print("打开串口失败")

    # 串口轮询等待接收数据
    while True:
        if ser1.in_waiting > 0:
            rx_chr = ser1.read().decode('ascii')
            if rx_chr == 'a':
                print("111")
        else:
            print("222")
        time.sleep(1)

    # 关闭串口
    ser1.close()

except Exception as e:
    print("出现异常：", e)
