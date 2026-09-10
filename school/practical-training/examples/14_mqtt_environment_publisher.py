import json
import time

import paho.mqtt.client as mqtt

from MyClass import pymata4EX


# DHT11 接在数字引脚 D2；A0、A1 在 pymata4EX 中分别使用模拟通道 0、1。
DHT_PIN = 2
LIGHT_PIN = 0
SOUND_PIN = 1

READ_INTERVAL_SECONDS = 2.0

# EMQX 本机 MQTT Broker。1880 是 Node-RED 编辑器端口，不是 MQTT 端口。
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "attributes"


def read_dht11(board):
    """读取 DHT11，并返回 (temperature, humidity) 或 None。"""
    value = board.dht_read(DHT_PIN)

    if not isinstance(value, (list, tuple)) or len(value) < 2:
        return None

    # 课程 pymata4EX 示例约定：value[0] 是湿度，value[1] 是温度。
    humidity = value[0]
    temperature = value[1]

    if not isinstance(temperature, (int, float)):
        return None
    if not isinstance(humidity, (int, float)) or not 0 <= humidity <= 100:
        return None

    return float(temperature), float(humidity)


def read_analog(board, pin):
    """读取模拟通道的 ADC 原始值，读取失败时返回 None。"""
    value = board.analog_read(pin)

    if not isinstance(value, (list, tuple)) or not value:
        return None

    result = value[0]
    if not isinstance(result, (int, float)):
        return None

    return int(result)


board = None
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

try:
    # Arduino 必须烧录 FirmataExpress，才能由 pymata4EX 直接访问引脚。
    board = pymata4EX.Pymata4EX()
    board.set_pin_mode_dht(DHT_PIN, sensor_type=11)
    board.set_pin_mode_analog_input(LIGHT_PIN)
    board.set_pin_mode_analog_input(SOUND_PIN)

    time.sleep(1)

    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    print("Arduino 连接成功")
    print("EMQX 连接成功")
    print(f"开始向 {MQTT_TOPIC} 发布环境数据")

    while True:
        dht_data = read_dht11(board)
        light = read_analog(board, LIGHT_PIN)
        sound = read_analog(board, SOUND_PIN)

        if dht_data is None:
            print("DHT11 数据无效")
            time.sleep(READ_INTERVAL_SECONDS)
            continue

        if light is None or sound is None:
            print("光线或声音数据无效")
            time.sleep(READ_INTERVAL_SECONDS)
            continue

        temperature, humidity = dht_data

        # 四项数据合成一个 JSON，一次 publish 发送到同一个主题。
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "sound": sound,
            "light": light,
        }
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

        result = client.publish(MQTT_TOPIC, payload)
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"已发布: {payload}")
        else:
            print(f"发布失败，错误码: {result.rc}")

        time.sleep(READ_INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\n用户停止程序")
except Exception as error:
    print(f"程序运行错误: {error}")
finally:
    try:
        client.loop_stop()
        client.disconnect()
    except Exception:
        pass

    if board is not None:
        try:
            board.shutdown()
        except Exception:
            pass
