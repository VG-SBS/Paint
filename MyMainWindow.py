from PySide6.QtWidgets import QMainWindow, QMenuBar, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from DrawWidget import DrawWidget


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.draw_widget = DrawWidget(self)

        # See https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMenuBar.html?highlight=qmenubar
        # for None parent
        self.menu_bar = QMenuBar(None)

        self.fileMenu = self.menu_bar.addMenu("Bilder")
        self.action_load_file = self.fileMenu.addAction("Bild öffnen", self.load_file)
        self.action_save_file = self.fileMenu.addAction("Bild speichern")

        self.setMenuBar(self.menu_bar)
        self.setWindowTitle("M$ P41nt")
        self.setCentralWidget(self.draw_widget)

    def load_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Bild auswählen", "Bilder (*.png, *.jpg)")

        if fileName == "":
            return

        self.image = QImage(fileName)
        self.pixmap = QPixmap(self.image)
        #self.pixmap.fromImage(self.image)
        self.draw_widget.setPixmap(self.pixmap)
        self.setBaseSize(self.pixmap.size())

        print("done.")
