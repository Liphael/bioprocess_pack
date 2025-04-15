if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = StrategyEditor()
    editor.show()
    sys.exit(app.exec())