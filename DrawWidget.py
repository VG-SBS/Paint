from PySide6.QtCore import QPoint, Slot
from PySide6.QtWidgets import QLabel, QColorDialog, QFileDialog
from PySide6.QtGui import QMouseEvent, QPainter, QPaintEvent, QPixmap, QColor, QImage


class DrawWidget(QLabel):
    setColor = Slot()
    loadFile = Slot()
    save_file = Slot()

    def __init__(self, parent):
        super(DrawWidget, self).__init__(parent)

        self.pos = None
        self.color = QColor("green")
        self.pixmap_from_image = None
        self.painter = QPainter()

    def setColor(self):
        selected_color = QColorDialog.getColor(self.color, self, "Farbe wählen")

        if selected_color.isValid():
            self.color = selected_color

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.pos = ev.pos()

        self.update()
        print("mouseevent")

    def paintEvent(self, ev: QPaintEvent) -> None:

        self.painter.begin(self)

        if self.pixmap_from_image:
            self.painter.drawPixmap(QPoint(1, 1), self.pixmap_from_image)
            print("True")

        if self.pos:
            print("in pos")
            self.painter.setPen(self.color)
            self.painter.drawEllipse(self.pos, 20, 20)
            self.painter.drawPoint(self.pos)
            #painter.save()
            #self.update()

        self.painter.end()

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Bild auswählen", "Bilder (*.png, *.jpg)")
        print("loaded")
        if file_name:
            self.image = QImage(file_name)
            self.pixmap_from_image = QPixmap(self.image)

            self.update()

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Bild speichern", "./", "Bilder (*.png, *.jpg)")

        if file_name:

            if self.image.save(file_name):
                print("Success")

