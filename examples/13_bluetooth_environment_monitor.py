import sys
import time
from collections import deque

import pyqtgraph as pg
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class SerialThread(QThread):
    data_received = pyqtSignal(float, float, float, int)
    connected = pyqtSignal()
    connection_error = pyqtSignal(str)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.running = False
        self.ser = None

    def run(self):
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=9600,
                timeout=1,
            )

            self.running = True
            self.connected.emit()

            while self.running:
                line = self.ser.readline().decode(
                    "utf-8",
                    errors="ignore",
                ).strip()

                if not line:
                    continue

                values = {}

                for item in line.strip(";").split(";"):
                    if ":" in item:
                        key, value = item.split(":", 1)
                        values[key] = value

                if all(key in values for key in ["T", "H", "D", "L"]):
                    temperature = float(values["T"])
                    humidity = float(values["H"])
                    distance = float(values["D"])
                    light = int(values["L"])

                    self.data_received.emit(
                        temperature,
                        humidity,
                        distance,
                        light,
                    )

        except Exception as e:
            self.connection_error.emit(str(e))

        finally:
            if self.ser is not None and self.ser.is_open:
                self.ser.close()

    def stop(self):
        self.running = False

        if self.ser is not None and self.ser.is_open:
            self.ser.close()

        self.wait()


class SensorPanel(QFrame):
    def __init__(self, title, unit, color):
        super().__init__()

        self.color = color
        self.setObjectName("sensorPanel")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(10)

        self.title_label = QLabel(title)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("cardTitle")

        value_layout = QHBoxLayout()

        self.value_label = QLabel("--")
        self.value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.value_label.setObjectName("cardValue")

        self.unit_label = QLabel(unit)
        self.unit_label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.unit_label.setObjectName("cardUnit")

        value_layout.addStretch()
        value_layout.addWidget(self.value_label)
        value_layout.addWidget(self.unit_label)
        value_layout.addStretch()

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground("w")
        self.plot_widget.showGrid(x=True, y=True, alpha=0.2)
        self.plot_widget.setLabel("bottom", "时间", units="s")
        self.plot_widget.setLabel("left", title, units=unit)
        self.plot_widget.setMinimumHeight(210)

        self.curve = self.plot_widget.plot(
            [],
            [],
            pen=pg.mkPen(self.color, width=2.5),
        )

        main_layout.addWidget(self.title_label)
        main_layout.addLayout(value_layout)
        main_layout.addWidget(self.plot_widget, 1)

    def set_value(self, value):
        self.value_label.setText(str(value))

    def set_data(self, times, values):
        self.curve.setData(list(times), list(values))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.serial_thread = None
        self.start_time = None

        self.time_data = deque(maxlen=60)
        self.temperature_data = deque(maxlen=60)
        self.humidity_data = deque(maxlen=60)
        self.distance_data = deque(maxlen=60)
        self.light_data = deque(maxlen=60)

        self.setWindowTitle("环境信息监测系统")
        self.resize(1450, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 25, 30, 20)
        main_layout.setSpacing(18)

        title = QLabel("环境信息监测系统")
        title.setObjectName("mainTitle")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Bluetooth Environmental Monitoring")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        connection_layout = QHBoxLayout()

        port_label = QLabel("蓝牙串口")

        self.port_box = QComboBox()
        self.refresh_button = QPushButton("刷新串口")
        self.connect_button = QPushButton("连接")
        self.status_label = QLabel("● 未连接")
        self.status_label.setObjectName("statusLabel")

        connection_layout.addWidget(port_label)
        connection_layout.addWidget(self.port_box, 1)
        connection_layout.addWidget(self.refresh_button)
        connection_layout.addWidget(self.connect_button)
        connection_layout.addWidget(self.status_label)

        main_layout.addLayout(connection_layout)

        sensors_layout = QGridLayout()
        sensors_layout.setHorizontalSpacing(15)
        sensors_layout.setVerticalSpacing(15)

        self.temperature_panel = SensorPanel("温度", "℃", "#ef4444")
        self.humidity_panel = SensorPanel("湿度", "%", "#3b82f6")
        self.distance_panel = SensorPanel("距离", "cm", "#10b981")
        self.light_panel = SensorPanel("光照", "ADC", "#f59e0b")

        sensors_layout.addWidget(self.temperature_panel, 0, 0)
        sensors_layout.addWidget(self.humidity_panel, 0, 1)
        sensors_layout.addWidget(self.distance_panel, 0, 2)
        sensors_layout.addWidget(self.light_panel, 0, 3)

        sensors_layout.setColumnStretch(0, 1)
        sensors_layout.setColumnStretch(1, 1)
        sensors_layout.setColumnStretch(2, 1)
        sensors_layout.setColumnStretch(3, 1)

        main_layout.addLayout(sensors_layout, 1)

        footer = QLabel(
            "第四小组 · "
            "田承卓 2413042304 · "
            "张榕哲 2423042108 · "
            "张思悦 2423042705 · "
            "刘珺 2423043136"
        )
        footer.setObjectName("footer")
        footer.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(footer)

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f8;
                font-family: "Microsoft YaHei";
                font-size: 14px;
            }

            #mainTitle {
                font-size: 30px;
                font-weight: bold;
                color: #202124;
            }

            #subtitle {
                font-size: 13px;
                color: #7a7f87;
            }

            #sensorPanel {
                background-color: white;
                border: 1px solid #dfe3e8;
                border-radius: 14px;
            }

            #cardTitle {
                font-size: 19px;
                font-weight: bold;
                color: #444444;
            }

            #cardValue {
                font-size: 36px;
                font-weight: bold;
                color: #202124;
            }

            #cardUnit {
                font-size: 14px;
                color: #888888;
                padding-bottom: 6px;
            }

            #statusLabel {
                color: #777777;
                font-weight: bold;
                padding: 0 10px;
            }

            QPushButton {
                background-color: #202124;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 18px;
            }

            QPushButton:hover {
                background-color: #3c4043;
            }

            QComboBox {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 6px;
                padding: 7px;
            }

            #footer {
                color: #999999;
                font-size: 12px;
            }
        """)

        self.refresh_button.clicked.connect(self.refresh_ports)
        self.connect_button.clicked.connect(self.toggle_connection)

        self.refresh_ports()

    def refresh_ports(self):
        self.port_box.clear()

        ports = serial.tools.list_ports.comports()

        for port in ports:
            self.port_box.addItem(
                f"{port.device} - {port.description}",
                port.device,
            )

        if self.port_box.count() == 0:
            self.port_box.addItem("未发现串口", None)

    def toggle_connection(self):
        if self.serial_thread is not None:
            self.disconnect_serial()
            return

        port = self.port_box.currentData()

        if port is None:
            QMessageBox.warning(self, "提示", "没有检测到可用串口")
            return

        self.status_label.setText("● 正在连接...")

        self.serial_thread = SerialThread(port)
        self.serial_thread.data_received.connect(self.update_data)
        self.serial_thread.connected.connect(self.on_connected)
        self.serial_thread.connection_error.connect(self.on_error)
        self.serial_thread.start()

    def on_connected(self):
        self.status_label.setText("● 已连接")
        self.connect_button.setText("断开")

        self.start_time = time.time()

        self.time_data.clear()
        self.temperature_data.clear()
        self.humidity_data.clear()
        self.distance_data.clear()
        self.light_data.clear()

        self.update_charts()

    def on_error(self, message):
        QMessageBox.critical(self, "串口错误", message)

        self.serial_thread = None
        self.status_label.setText("● 连接失败")
        self.connect_button.setText("连接")

    def disconnect_serial(self):
        if self.serial_thread is not None:
            self.serial_thread.stop()
            self.serial_thread = None

        self.status_label.setText("● 未连接")
        self.connect_button.setText("连接")

    def update_data(self, temperature, humidity, distance, light):
        self.temperature_panel.set_value(f"{temperature:.1f}")
        self.humidity_panel.set_value(f"{humidity:.1f}")

        if distance < 0:
            self.distance_panel.set_value("--")
        else:
            self.distance_panel.set_value(f"{distance:.1f}")

        self.light_panel.set_value(light)

        if self.start_time is None:
            self.start_time = time.time()

        elapsed_time = time.time() - self.start_time

        self.time_data.append(elapsed_time)
        self.temperature_data.append(temperature)
        self.humidity_data.append(humidity)

        if distance < 0:
            if len(self.distance_data) == 0:
                self.distance_data.append(0)
            else:
                self.distance_data.append(self.distance_data[-1])
        else:
            self.distance_data.append(distance)

        self.light_data.append(light)
        self.update_charts()

    def update_charts(self):
        self.temperature_panel.set_data(self.time_data, self.temperature_data)
        self.humidity_panel.set_data(self.time_data, self.humidity_data)
        self.distance_panel.set_data(self.time_data, self.distance_data)
        self.light_panel.set_data(self.time_data, self.light_data)

    def closeEvent(self, event):
        if self.serial_thread is not None:
            self.serial_thread.stop()

        event.accept()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
