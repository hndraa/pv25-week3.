import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt

class JendelaUtama(QWidget):
    def __init__(self):
        super().__init__()

        # Pengaturan jendela utama
        self.setWindowTitle("Pelacak Gerakan Mouse")
        self.setGeometry(100, 100, 600, 400)
        self.setMouseTracking(True)

        # Label untuk menampilkan koordinat mouse
        self.label_koordinat = QLabel(self)
        self.label_koordinat.setText("Arahkan kursor di sini")
        self.label_koordinat.setStyleSheet("background-color: lightblue; padding: 5px; border-radius: 5px;")
        self.label_koordinat.setGeometry(250, 180, 150, 30)

    def gerakan_mouse(self, event):
        """Menampilkan koordinat mouse saat bergerak di dalam jendela."""
        x, y = event.x(), event.y()
        self.label_koordinat.setText(f"X: {x}, Y: {y}")

    def masuk_label(self, event):
        """Memindahkan label ke posisi acak saat kursor masuk ke area label."""
        posisi_x = random.randint(0, self.width() - self.label_koordinat.width())
        posisi_y = random.randint(0, self.height() - self.label_koordinat.height())
        self.label_koordinat.move(posisi_x, posisi_y)

    # Override event PyQt5
    def mouseMoveEvent(self, event):
        self.gerakan_mouse(event)

    def enterEvent(self, event):
        self.masuk_label(event)

# Menjalankan aplikasi
if __name__ == "__main__":
    aplikasi = QApplication(sys.argv)
    jendela = JendelaUtama()
    jendela.show()
    sys.exit(aplikasi.exec_())
