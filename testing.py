class CheckExcel(QtCore.QThread):
    updated = QtCore.pyqtSignal(int)
    updateLab = QtCore.pyqtSignal(str)
    running = False

    def __init__(self, parent=None):
        super(CheckExcel, self).__init__(parent)
        self.progPercent = 0
        self.running = True

    def run(self):
        pythoncom.CoInitialize()

        try:
            while self.running == True:

                self.updated.emit(int(self.progPercent))
                self.updateLab.emit(str(va_TC))

                print(self.progPercent)

        except :
            print('Excel is not executed')

            CheckExcel().run()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    def startBtnClicked(self):

        self.chk_excel = CheckExcel(self)
        self.chk_excel.start()

        self.chk_excel.updated.connect(self.updateValue)
        self.chk_excel.updateLab.connect(self.updateLabel)

    def updateValue(self, data):
        self.progressBar.setValue(data)

    def updateLabel(self, text):
        self.label.setText(text)

    def stop(self):
        self.event.set()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
python python-3.x pyqt pyqt5 signals-slots