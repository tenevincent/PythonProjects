from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile



import sys

app = QApplication(sys.argv)


# Create a Qt widget, which will be our window.
window = QWidget()
window.show() # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec_()


