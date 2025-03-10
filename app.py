import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFileDialog, QMessageBox, QSlider
)
from PyQt5.QtCore import Qt
from PIL import Image
import pillow_heif  # Enables Pillow to open HEIF files

# Supported image extensions
SUPPORTED_EXTENSIONS = {'.heif', '.jpeg', '.jpg', '.png'}

class ImageConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter to WebP")
        self.setGeometry(300, 300, 500, 250)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Source folder selection
        src_layout = QHBoxLayout()
        src_label = QLabel("Source Folder:")
        self.src_path = QLineEdit()
        self.src_path.setReadOnly(True)
        src_button = QPushButton("Select Source")
        src_button.clicked.connect(self.select_source_folder)
        src_layout.addWidget(src_label)
        src_layout.addWidget(self.src_path)
        src_layout.addWidget(src_button)
        layout.addLayout(src_layout)

        # Destination folder selection
        dest_layout = QHBoxLayout()
        dest_label = QLabel("Destination Folder:")
        self.dest_path = QLineEdit()
        self.dest_path.setReadOnly(True)
        dest_button = QPushButton("Select Destination")
        dest_button.clicked.connect(self.select_destination_folder)
        dest_layout.addWidget(dest_label)
        dest_layout.addWidget(self.dest_path)
        dest_layout.addWidget(dest_button)
        layout.addLayout(dest_layout)

        # Quality slider layout
        quality_layout = QHBoxLayout()
        quality_label = QLabel("Quality (High compression = low quality):")
        self.quality_slider = QSlider(Qt.Horizontal)
        self.quality_slider.setMinimum(10)
        self.quality_slider.setMaximum(100)
        self.quality_slider.setValue(80)
        self.quality_slider.setTickPosition(QSlider.TicksBelow)
        self.quality_slider.setTickInterval(10)
        self.quality_value_label = QLabel(str(self.quality_slider.value()))
        self.quality_slider.valueChanged.connect(lambda value: self.quality_value_label.setText(str(value)))
        quality_layout.addWidget(quality_label)
        quality_layout.addWidget(self.quality_slider)
        quality_layout.addWidget(self.quality_value_label)
        layout.addLayout(quality_layout)

        # Convert Button
        self.convert_button = QPushButton("Convert Images")
        self.convert_button.clicked.connect(self.convert_images)
        layout.addWidget(self.convert_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def apply_styles(self):
        # Updated stylesheet with black text for labels and QLineEdit
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QLineEdit, QLabel {
                padding: 4px;
                color: black;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #003f6b;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #ccc;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #0078d7;
                border: none;
                width: 16px;
                margin: -4px 0;
                border-radius: 8px;
            }
        """)

    def select_source_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if folder:
            self.src_path.setText(folder)

    def select_destination_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if folder:
            self.dest_path.setText(folder)

    def convert_images(self):
        src = self.src_path.text()
        dest_base = self.dest_path.text()
        if not src or not dest_base:
            QMessageBox.warning(self, "Missing Path", "Please select both source and destination folders.")
            return

        # Create a new folder inside destination for converted images
        dest_folder = os.path.join(dest_base, "Converted_Images")
        os.makedirs(dest_folder, exist_ok=True)

        quality = self.quality_slider.value()
        converted_count = 0
        for root, _, files in os.walk(src):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in SUPPORTED_EXTENSIONS:
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_folder, os.path.splitext(file)[0] + '.webp')
                    try:
                        with Image.open(src_file) as img:
                            img.save(dest_file, 'WEBP', quality=quality)
                        converted_count += 1
                    except Exception as e:
                        print(f"Error converting {src_file}: {e}")

        QMessageBox.information(
            self,
            "Conversion Complete",
            f"Successfully converted {converted_count} images to WebP.\nSaved in: {dest_folder}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ImageConverterUI()
    converter.show()
    sys.exit(app.exec_())
