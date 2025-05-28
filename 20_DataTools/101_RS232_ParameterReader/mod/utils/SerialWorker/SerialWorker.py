import sys
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow
import serial.tools.list_ports
import serial

class SerialWorker(QObject):
    data_received = Signal(bytes)          # 原始数据信号
    status_updated = Signal(str)           # 状态信息信号
    error_occurred = Signal(Exception)     # 错误信号

    def __init__(self, port=None, baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.running = False

    def port_seek(self):
        ports = serial.tools.list_ports.comports()  # 获取所有可用串口
        if not ports:
            self.status_updated.emit("无可用串口")
            return []  # 无可用串口时返回空列表
        return [port.device for port in ports] # 返回可用串口列表

    def connect_serial(self, set_port=None, set_baudrate=9600, set_bytesize=serial.EIGHTBITS, set_parity=serial.PARITY_NONE, set_stopbits=serial.STOPBITS_ONE, set_timeout=1):
        """连接串口"""
        try:
            self.ser = serial.Serial(
                port=set_port if set_port else self.port,
                baudrate=set_baudrate if set_baudrate else self.baudrate,
                bytesize=set_bytesize,
                parity=set_parity,
                stopbits=set_stopbits,
                timeout=set_timeout
            )
            self.status_updated.emit(f"成功连接 {self.port}")
            return True
        except Exception as e:
            self.error_occurred.emit(e)
            return False

    def start_monitoring(self):
        """开始监听数据"""
        if not self.connect_serial():
            return

        self.running = True
        self.status_updated.emit("开始监听数据...")
        
        try:
            while self.running and self.ser.is_open:
                if self.ser.in_waiting > 0:
                    raw_data = self.ser.read(self.ser.in_waiting)
                    self.data_received.emit(raw_data)
        except Exception as e:
            self.error_occurred.emit(e)
        finally:
            self.stop()

    def stop(self):
        """停止监听"""
        if self.running:
            self.running = False
            if self.ser and self.ser.is_open:
                self.ser.close()
            self.status_updated.emit("监听已停止")