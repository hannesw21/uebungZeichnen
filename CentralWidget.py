import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zeichenprogramm')
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        #painter.setRenderHint(QPainter.Antialiasing)

        # Zeichenfarbe auf Schwarz setzen und den Kreis ausfüllen
        painter.setBrush(QColor(0, 0, 0))
        painter.drawEllipse(50, 50, 100, 100)

        # Zeichenfarbe auf Grün ändern und die Ellipse zeichnen
        painter.setBrush(QColor(0, 255, 0))
        painter.drawEllipse(200, 50, 100, 100)

        # Zeichenfarbe auf Rot ändern und das Quadrat zeichnen
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(50, 200, 100, 100)

        # Zeichenfarbe auf Blau ändern und die Linie zeichnen
        painter.setPen(QPen(QColor(0, 0, 255), 2))
        painter.drawLine(200, 300, 300, 300)

        # Text "Zeichenprogramm" zeichnen
        painter.setFont(QFont('Arial', 12))
        painter.drawText(50, 350, "Zeichenprogramm")


class DrawingWidget:
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CentralWidget()
    window.show()
    sys.exit(app.exec())
        

