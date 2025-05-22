import serial



# 写入初始化串口参数，以防止串口未正确配置
PORT = None                     # 串口号（Windows）或/dev/ttyUSB0（Linux）
BAUDRATE = 9600                 # 波特率
BYTESIZE = serial.EIGHTBITS     # 数据位
PARITY = serial.PARITY_NONE     # 校验位
STOPBITS = serial.STOPBITS_ONE  # 停止位
TIMEOUT = 1                     # 读取超时时间（秒）
INTERVAL = 0.5                  # 读取间隔（秒）

class DefaultCfg():
    def __init__(self):
        self.port = PORT
        self.baudrate = BAUDRATE
        self.bytesize = BYTESIZE
        self.parity = PARITY
        self.stopbits = STOPBITS
        self.timeout = TIMEOUT
        self.interval = INTERVAL
        self.load_default_cfg()

    def load_default_cfg(self):
        try:
            with open('default.cfg', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    key, value = line.strip().split('=')
                    if hasattr(self, key):
                        setattr(self, key, value)
        except FileNotFoundError:
            print("未找到默认配置文件，使用默认参数。")
        except Exception as e:
            print(f"加载配置文件失败: {e}")
        finally:
            print(f"当前配置: {self.__dict__}")


class CfgEditor():
    def __init__(self):
        self.cfg = DefaultCfg()
        self.signals = ConfigSignal()
        self.current_path = None
        self.file_type = None
        self.config_data = None

    def detect_file_type(self, file_path):
        f_sfx = file_suffix = Path(file_path).suffix.lower()[1:]
        if f_sfx in {'yaml', 'yml'}:
            return 'yaml'
        return f_sfx if f_sfx in {'json', 'ini'} else None

    def load_cfg(self, file_path):
        try:
            self.file_type = self.detect_file_type(file_path)
            if not self.file_type:
                raise ValueError("不支持的配置文件格式")

            with open(file_path, 'r', encoding='utf-8') as f:
                if self.file_type == 'json':
                    self.config_data = json.load(f)
                elif self.file_type == 'ini':
                    config = configparser.ConfigParser()
                    config.read_file(f)
                    self.config_data = {s: dict(config.items(s)) 
                                       for s in config.sections()}
                elif self.file_type in ('yaml', 'yml'):
                    self.config_data = yaml.safe_load(f)

            self.current_path = file_path
            self.signals.config_loaded.emit(file_path)
            return True

        except Exception as e:
            self.signals.error_occurred.emit(f"加载失败: {str(e)}")
            return False


class SignalSeeker():
    def __init__(self):
        self.config_loaded = Signal()
        
    def find_serial_device(self):
        """自动检测可用串口设备"""
        ports = list_ports.comports()
        if not ports:
            return None
        return ports[0].device

class BioComApp():
    def __init__(self):
        DefaultCfg.__init__(self)
    
    def parse_weight_data(self, raw_data):
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
