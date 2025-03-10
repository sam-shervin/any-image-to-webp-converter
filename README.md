
# Any Image to WebP Converter

A Python application with a modern GUI built using PyQt5 that recursively converts images (HEIF, JPEG, JPG, PNG) to WebP format.

## Features

- **Recursive Conversion:** Scans directories (including subfolders) to convert supported images.
- **Quality Control:** Adjust the quality (compression level) via a slider. (High compression means low quality.)
- **User-Friendly UI:** Select source and destination folders with intuitive file dialogs.
- **Automatic Folder Creation:** Converted images are saved in a new "Converted_Images" folder within the chosen destination.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd any-image-to-webp-converter
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**

   You can install the required packages with:

   ```bash
   pip install .
   ```

   Alternatively, if you prefer, install directly using pip:

   ```bash
   pip install Pillow pillow-heif PyQt5
   ```

## Usage

Run the application with:

```bash
python app.py
```

The GUI will let you:
- Select a **Source Folder** containing images.
- Choose a **Destination Folder** where a `Converted_Images` folder will be automatically created.
- Adjust the **Quality** (slider indicates current quality; note that lower values mean higher compression/lower quality).
- Click **Convert Images** to perform the conversion.

## Requirements

- Python 3.8+
- [Pillow](https://python-pillow.org/)
- [pillow-heif](https://github.com/david-poirier-campion/pillow-heif)
- [PyQt5](https://pypi.org/project/PyQt5/)

## License

This project is licensed under the MIT License.