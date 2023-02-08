from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QMouseEvent, QPainter, QPaintEvent, QPixmap, QColor


class DrawWidget(QLabel):
    def __init__(self, parent):
        super(DrawWidget, self).__init__(parent)
        self.pos = QPoint(5, 5)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.pos = ev.pos()

        # Aufgabe 2:
        # Verbinden Sie das Mouse-Event mit dem Paint-Event,
        # nutzen sie dafür das self.pos.

    def paintEvent(self, ev: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.drawPoint(5, 20)
        painter.drawEllipse(50, 25, 20, 20)

        # Aufgabe 1: https://doc.qt.io/qt-6/qcolordialog.html
        # Über die Menu-Leiste kann der Benutzer die Farbe bestimmen.

        painter.setPen(QColor("yellow"))
        painter.drawRoundedRect(100, 200, 50, 50, 5, 10)

        painter.end()