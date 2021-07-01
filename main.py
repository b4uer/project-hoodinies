import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QProcess, QObject, pyqtSlot

class Backend(QObject):

    def __init__(self):
        super().__init__()

        self.p = None  # Default empty value

    @pyqtSlot()
    def start_process(self):
        if self.p is None:  # No process running.
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            #self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python", ['face_detect.py'])

if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')

    # Define our backend object, which we pass to QML.
    backend = Backend()

    engine.rootObjects()[0].setProperty('backend', backend)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())