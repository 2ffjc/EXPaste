# styles.py
STYLES = {
    "main_window": """
        QMainWindow {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                      stop: 0 #667eea, stop: 1 #764ba2);
            border-radius: 15px;
        }
    """,
    
    "central_widget": """
        QWidget {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            margin: 10px;
        }
    """,
    
    "title_label": """
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: #2d3748;
            padding: 10px;
        }
    """,
    
    "normal_label": """
        QLabel {
            font-size: 14px;
            color: #4a5568;
            padding: 5px;
        }
    """,
    
    "button_primary": """
        QPushButton {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                      stop: 0 #667eea, stop: 1 #764ba2);
            border: none;
            border-radius: 8px;
            color: white;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }
        QPushButton:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                      stop: 0 #5a67d8, stop: 1 #6b46c1);
        }
        QPushButton:pressed {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                      stop: 0 #4c51bf, stop: 1 #553c9a);
        }
        QPushButton:disabled {
            background: #cbd5e0;
            color: #a0aec0;
        }
    """,
    
    "button_secondary": """
        QPushButton {
            background: #e2e8f0;
            border: 2px solid #cbd5e0;
            border-radius: 8px;
            color: #4a5568;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 14px;
        }
        QPushButton:hover {
            background: #cbd5e0;
            border-color: #a0aec0;
        }
    """,
    
    "progress_bar": """
        QProgressBar {
            border: 2px solid #cbd5e0;
            border-radius: 6px;
            text-align: center;
            background: white;
            height: 20px;
        }
        QProgressBar::chunk {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                      stop: 0 #667eea, stop: 1 #764ba2);
            border-radius: 4px;
        }
    """,
    
    "text_edit": """
        QTextEdit {
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            padding: 10px;
            font-size: 12px;
            background: white;
        }
        QTextEdit:focus {
            border-color: #667eea;
        }
    """
}