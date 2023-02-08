from PySide6.QtWidgets import QLabel
from PySide6 import QtGui
import PySide6
from PySide6.QtGui import QMouseEvent, QPainter, QCursor


class DrawWidget(QLabel):
    def __init__(self, parent):
        super(DrawWidget, self).__init__(parent)

    def mousePressEvent(self, ev: PySide6.QtGui.QMouseEvent) -> None:
        self.pos = ev.pos()
        self.painter = QPainter(self.pixmap())
        #self.paintEvent(pos)

    def paintEvent(self, ev: PySide6.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPoint(self.pos)
        painter.drawEllipse(50, 25, 20, 20)
        painter.end()

# Set Colour mit Farbmenü
#