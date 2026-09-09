import time

from MyClass import pymata4EX


DHT_PIN = 2

board = pymata4EX.Pymata4EX()
board.set_pin_mode_dht(DHT_PIN, sensor_type=11)

try:
    while True:
        value = board.dht_read(DHT_PIN)

        if value is not None:
            humidity = value[0]
            temperature = value[1]
            print(value)
            print(f"湿度: {humidity} %, 温度: {temperature} ℃")
        else:
            print("暂时没有读取到 DHT11 数据")

        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n程序终止，释放资源")
finally:
    board.shutdown()
