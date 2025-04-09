import serial
import time
from serial.tools import list_ports

# 配置串口参数（根据实际设备调整）
PORT = 'COM1'           # 串口号（Windows）或/dev/ttyUSB0（Linux）
BAUDRATE = 9600         # 波特率
BYTESIZE = serial.EIGHTBITS  # 数据位
PARITY = serial.PARITY_NONE  # 校验位
STOPBITS = serial.STOPBITS_ONE  # 停止位
TIMEOUT = 1             # 读取超时时间（秒）
INTERVAL = 0.5          # 读取间隔（秒）

def find_serial_device():
    """自动检测可用串口设备"""
    ports = list_ports.comports()
    if not ports:
        return None
    return ports[0].device

def parse_weight_data(raw_data):
    """
    解析原始重量数据（需根据实际协议实现）
    示例处理：
    假设设备发送ASCII字符串："W,+0001.23kg\\r\\n"
    """
    try:
        # 去除空白字符和换行符
        cleaned = raw_data.decode().strip()
        # 提取数字部分
        weight_str = cleaned.split(',')[1].replace('kg', '')
        return float(weight_str)
    except Exception as e:
        print(f"数据解析失败: {e}")
        return None

def main():
    # 自动检测串口设备
    auto_port = find_serial_device()
    port = auto_port or PORT

    try:
        # 初始化串口连接
        with serial.Serial(
            port=port,
            baudrate=BAUDRATE,
            bytesize=BYTESIZE,
            parity=PARITY,
            stopbits=STOPBITS,
            timeout=TIMEOUT
        ) as ser:
            print(f"已连接串口: {ser.name}")
            print("按Ctrl+C停止程序...")

            while True:
                # 发送查询命令（如果需要，根据设备协议）
                # ser.write(b"GET_WEIGHT\r\n")
                
                # 读取数据
                raw_data = ser.readline()
                
                if raw_data:
                    weight = parse_weight_data(raw_data)
                    if weight is not None:
                        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 当前重量: {weight:.2f} kg")
                
                time.sleep(INTERVAL)

    except serial.SerialException as e:
        print(f"串口连接失败: {e}")
    except KeyboardInterrupt:
        print("\n程序已手动终止")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()