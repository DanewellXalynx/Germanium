import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineHistory, QWebEngineSettings

class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('Germanium')

        # Load the start page
        self.load(sys.argv[1] if len(sys.argv) > 1 else 'https://www.search.brave.com')

        # Show the window
        self.show()

    def closeEvent(self, event):
        # Clear cookies, cache, history, and search engine on exit
        from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineHistory, QWebEngineSettings
        QWebEngineProfile.defaultProfile().clearHttpCache()
        QWebEngineProfile.defaultProfile().clearCookies()
        QWebEngineHistory.defaultHistory().clear()
        settings = self.settings()
        settings.setDefaultSearchEngineId('https://search.brave.com/search?q=')

        # Call the base class implementation
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
