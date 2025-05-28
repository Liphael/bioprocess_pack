# GuideBook For **Logger Module**

## Descriptions

    日志模块
    
    功能特性：
    - 自动创建CSV文件并添加表头
    - 支持自定义字段结构
    - 自动处理特殊字符
    - 时间戳自动生成
    - 严格的字段验证

### Usage

    示例用法：
    >>> logger = MessageLogger("logs.csv", ["timestamp", "level", "message"])
    >>> logger.log("系统启动")  # 快速记录消息
    >>> logger.logger_record({"level": "ERROR", "message": "文件未找到"})  # 完整记录

## Source Code With notes

    ```python

    import csv
    import os
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

            """
            Logger初始化参数：

            filename: CSV文件路径；
            fieldnames: 字段名称列表；默认为timestamp时间戳，type类型，message原始信息。
            encoding: 编码格式；默认为BOM的UTF-8（以兼容Excel）
            """
            self.filename = filename
            self.fieldnames = fieldnames
            self.encoding = encoding
            self._ensure_header()

        def _ensure_header(self) -> None:
            """确保文件存在并包含表头"""
            if not os.path.exists(self.filename):
                with open(self.filename, "w", newline="", encoding=self.encoding) as f:
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                    writer.writeheader()

        def log(self, message: str, level: str = "INFO") -> None:
            """
            快速记录消息（自动生成时间戳）
            
            参数：
            message: 消息内容
            level: 日志级别（默认INFO）
            """
            internal_record = {
                "timestamp": datetime.now().isoformat(),
                "level": level,
                "message": message
            }
            self.logger_record(internal_record)

        def logger_record(self, record: Dict[str, Union[str, int, float]]) -> None:
            """
            记录完整数据记录
            
            参数：
            record: 字典格式的数据记录，必须包含所有声明的字段
            """
            # 验证字段有效性
            if not all(key in self.fieldnames for key in record.keys()):
                missing = set(self.fieldnames) - set(record.keys())
                raise ValueError(f"缺少必需字段: {missing}")

            # 写入CSV文件
            try:
                with open(self.filename, "a", newline="", encoding=self.encoding) as f:
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                    writer.writerow(internal_record)
            except PermissionError:
                raise RuntimeError("文件被占用，请关闭Excel等程序后重试")
            except Exception as e:
                raise RuntimeError(f"写入文件失败: {str(e)}")

        def export_csv(self, new_filename: str = None) -> str:
            """
            导出CSV文件（主要用于格式转换）
            
            参数：
            new_filename: 新文件名（默认覆盖原文件）
            返回：最终文件路径
            """
            target = new_filename or self.filename
            os.replace(self.filename, target)
            return target

    # --------------------------
    # 使用示例
    # --------------------------

    if __name__ == "__main__":
        # 初始化日志记录器（自定义字段）
        logger = Logger(
            filename="system_logs.csv",
            fieldnames=["timestamp", "message", "level"]
        )

        # 记录系统启动信息
        logger.logger_record({
            "timestamp": datetime.now().isoformat(),
            "level": "SUCCESS",
            "message": "服务初始化完成"
        })

        # 快速记录消息（自动生成时间戳）
        try:
            # 模拟业务操作
            logger.log("收到用户请求", level="DEBUG")
            logger.logger_record({
                "level": "WARNING",
                "message": "连接池使用率超过80%"
            })
        except Exception as e:
            logger.log(f"发生错误: {str(e)}", level="ERROR")

        print(f"日志已保存至: {logger.export_csv()}")

    ```
