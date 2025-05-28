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
                csv_writer.writerow(internal_record)
        except PermissionError:
            raise RuntimeError("文件被占用，请关闭Excel或相关程序后重试")
        except Exception as e:
            raise RuntimeError(f"写入文件失败，错误: {str(e)}")

    def replace_csv(self, new_filename: str = None) -> str:
        """
        导出CSV文件（主要用于格式转换）
        
        参数：
        new_filename: 新文件名（默认覆盖原文件）
        返回：最终文件路径
        """
        current_dir = Path(self.filename)
        target = new_filename or self.filename
        try:
            Path(target).parent.mkdir(parents=True, exist_ok=True)
            os.replace(self.filename, target)
            self.filename = target
            return target
        except Exception as e:
            raise RuntimeError(f"导出CSV文件失败，错误: {str(e)}")
