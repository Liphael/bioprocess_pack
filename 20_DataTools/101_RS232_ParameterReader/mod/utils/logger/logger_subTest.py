import csv
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Union

class Logger:

    def __init__(
        self,
        filename: str,
        fieldnames: List[str] = [
            "timestamp",
            "message"
            ],
        encoding: str = "utf-8-sig"
    ):

        self.filename = filename
        self.fieldnames = fieldnames
        self.encoding = encoding
        self.pre_ensure_header()

    def pre_ensure_header(self) -> None:
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="", encoding=self.encoding) as f:
                csv_writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                csv_writer.writeheader()

# 自带日志记录方法
    def log(self, message: str, log_type: str = "log", level: str = "INFO") -> None:
        internal_record = {
            "timestamp": datetime.now().isoformat(),
            "type": log_type,
            "level": level,
            "message": message
        }
        self.logger_record(internal_record)

# 记录方法
    def logger_record(self, record: Dict[str, Union[str, int, float]]) -> None:
        # 验证字段有效性
        if not all(key in self.fieldnames for key in record.keys()):
            missing = set(self.fieldnames) - set(record.keys())
            raise ValueError(f"缺少必需字段: {missing}")

        # 写入CSV文件
        try:
            with open(self.filename, "a", newline="", encoding=self.encoding) as f:
                csv_writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                csv_writer.writerow(record)
        except PermissionError:
            raise RuntimeError("文件被占用，请关闭Excel或相关程序后重试")
        except Exception as e:
            raise RuntimeError(f"写入文件失败，错误: {str(e)}")

    def close(self) -> None:
        """关闭文件句柄，释放资源"""
        pass

    def replace_csv(self, new_filename: str = None) -> str:
        current_dir = Path(self.filename)
        target = new_filename or self.filename
        try:
            Path(target).parent.mkdir(parents=True, exist_ok=True)
            os.replace(self.filename, target)
            self.filename = target
            return target
        except Exception as e:
            raise RuntimeError(f"导出CSV文件失败，错误: {str(e)}")

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "output.csv")
data_log = Logger(
    filename=data_path,
    fieldnames=["timestamp", "message"],
)

import sys

if __name__ == "__main__":
    decoded_data = str("this is a test message")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    try:
        data_log.logger_record({
            "timestamp": timestamp,
            "message": decoded_data
        })
    except Exception as e:
        raise RuntimeError(f"FATAL: {str(e)}")

    
    print(f"New filename path: {new_filename_path}")
    data_log.replace_csv(new_filename=new_filename_path)
    input("Press Enter to exit...")
    
