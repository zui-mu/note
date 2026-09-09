import time

from MyClass import pymata4EX


DHT_PIN = 2
FAN_PIN = 3

TEMP_HIGH = 29
TEMP_LOW = 28

board = pymata4EX.Pymata4EX()
board.set_pin_mode_dht(DHT_PIN, sensor_type=11)
board.set_pin_mode_digital_output(FAN_PIN)

fan_is_on = False

try:
    while True:
        value = board.dht_read(DHT_PIN)

        if value is None:
            print("暂时没有读取到 DHT11 数据")
            time.sleep(0.5)
            continue

        humidity = value[0]
        temperature = value[1]
        print(f"湿度: {humidity} %，温度: {temperature} ℃")

        # Hysteresis: turn on at 29 C, but do not turn off until 28 C.
        if temperature >= TEMP_HIGH and not fan_is_on:
            board.digital_write(FAN_PIN, 1)
            fan_is_on = True
            print("温度过高，风扇开启")
        elif temperature <= TEMP_LOW and fan_is_on:
            board.digital_write(FAN_PIN, 0)
            fan_is_on = False
            print("温度正常，风扇关闭")

        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n程序终止，释放资源")
finally:
    board.digital_write(FAN_PIN, 0)
    board.shutdown()
