# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui_window import MainWindow

def main():
    # 创建应用
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    # 创建主窗口
    window = MainWindow()
    window.show()
    
    # 运行应用
    sys.exit(app.exec_())

    # 就这么简单嘻嘻

if __name__ == "__main__":
    main()
