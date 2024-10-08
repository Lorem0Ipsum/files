import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QStatusBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://cipherbrowse.glitch.me/'))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setPlaceholderText('Enter URL and press Enter')
        self.url_bar.setStyleSheet('font-size: 14px;')

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.browser.back)
        self.back_button.setStyleSheet('font-size: 14px;')

        self.forward_button = QPushButton('Forward')
        self.forward_button.clicked.connect(self.browser.forward)
        self.forward_button.setStyleSheet('font-size: 14px;')

        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.browser.reload)
        self.refresh_button.setStyleSheet('font-size: 14px;')

        self.home_button = QPushButton('Home')
        self.home_button.clicked.connect(self.go_home)
        self.home_button.setStyleSheet('font-size: 14px;')

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        hbox = QHBoxLayout()
        hbox.addWidget(self.back_button)
        hbox.addWidget(self.forward_button)
        hbox.addWidget(self.refresh_button)
        hbox.addWidget(self.home_button)
        hbox.addWidget(self.url_bar)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.browser)

        container = QWidget()
        container.setLayout(vbox)

        self.setCentralWidget(container)
        self.setWindowTitle('CipherBrowse - Your Gateway to a Safer Internet')
        self.setStyleSheet('background-color: #1e1e1e; color: #ffffff;')

        self.browser.urlChanged.connect(self.update_url_bar)
        self.browser.loadFinished.connect(self.update_status_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        url = q.toString()
        self.url_bar.setText(url)
        if url.startswith('https'):
            self.status_bar.showMessage('Secure Connection', 2000)
        else:
            self.status_bar.showMessage('Insecure Connection', 2000)

    def update_status_bar(self):
        pass

    def go_home(self):
        self.browser.setUrl(QUrl('https://cipherbrowse.glitch.me/'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
