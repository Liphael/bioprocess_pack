import serial
import serial.tools.list_ports
from datetime import datetime
import sys

class RS232Monitor:
    global process_info  # 全局变量，用于存储进程信息
    process_info = None  # 用于存储进程信息

    def __init__(self):
        self.port = 'COM3'    # 串口号
        self.baudrate = 9600  # baudrate:
        self.timeout = 1      # 读取超时时间（秒）
        self.running = False  # 运行状态
        self.ser = None       # 串口对象

    def port_seek(self):
        ports = serial.tools.list_ports.comports()  # 获取所有可用串口
        if not ports:
            process_info = "error#0001: COM device not found"  # 更新进程信息
            print(process_info)  # 打印进程信息，后期替换为日志记录或其他处理
            return []  # 无可用串口时返回空列表
        return [port.device for port in ports] # 返回可用串口列表

    def connect(self, port=None, baudrate=9600):
        """连接串口"""
        try:
            if not port: # 如果未指定端口，则自动查找可用串口
                available_ports = self.port_seek()
                if not available_ports:
                    process_info = "error#0001: COM device not found"  # 更新进程信息
                    print(process_info)  # 打印进程信息，后期替换为日志记录或其他处理
                    return False # 无可用串口时返回False
                process_info = "success#0000: COM device exist"
                print(process_info)
                print(available_ports)
                print("which port should I choose? (serial number start from 0)")
                i = int(input())
                port = available_ports[i] # 连接指定的可用串口

            self.ser = serial.Serial(
                port=port,
                baudrate=baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self.timeout
            )
            self.port = port
            process_info = f"success#0001: connected {port} [baudrate: {baudrate}]"
            print(process_info)
            return True
            
        except serial.SerialException as e:
            process_info = f"error#0002: connect fail {port} [baudrate: {baudrate}]"
            print(process_info)
            return False

    def start_monitoring(self):
        """开始监听数据"""
        if not self.ser or not self.ser.is_open:
            process_info = "error#0003: COM offline or connect fail"
            print(process_info)
            return

        self.running = True
        process_info = f"success#0002: listening (press Ctrl+C to stop)..."
        print(process_info)
        try:
            while self.running:
                if self.ser.in_waiting > 0:
                    # 读取数据（两种方式任选其一）
                    # raw_data = self.ser.readline()  # 方式1：按行读取
                    raw_data = self.ser.read(self.ser.in_waiting)  # 方式2：读取全部缓存数据
                    
                    if raw_data:
                        self.data_process(raw_data) # 调用data_process方法处理数据
        except KeyboardInterrupt:
            self.stop()
        finally:
            self.stop()

    def data_process(self, raw_data):
        """处理接收到的数据"""
        try:
            # 转换为字符串（ASCII解码）
            decoded_data = raw_data.decode('ascii').strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] RX: {decoded_data}")
            
            # 此处可以添加自定义处理逻辑
            # 例如：保存到文件、触发其他操作等
            
        except UnicodeDecodeError:
            # 二进制数据处理
            hex_data = raw_data.hex().upper()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] HEX: {hex_data}")

    def stop(self):
        """停止监听并关闭连接"""
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.running = False
        process_info = "success#0003: connection closed"
        print(process_info)

if __name__ == "__main__":
    monitor = RS232Monitor()
    
    # 自动连接第一个可用端口
    if not monitor.connect():
        sys.exit(3)
    
    # 开始监听
    monitor.start_monitoring()