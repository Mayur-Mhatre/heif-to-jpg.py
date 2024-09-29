
# HEIF/HEIC to JPG Converter 🖼️

A simple Python tool to batch convert `.heif` or `.heic` images (used by Apple devices) into `.jpg` format, making them easier to edit, share, or use across different platforms.

This tool is ideal for anyone who works with HEIF/HEIC images and needs a fast, reliable way to convert them for compatibility with common image editors or viewers.

## 🚀 Features

- **Batch Conversion**: Automatically converts all `.heif/.heic` images in a specified directory to `.jpg`.
- **Progress Bar**: Displays real-time progress using a `tqdm` progress bar for a clear view of the conversion status.
- **Platform Support**: Fully functional on Windows and other operating systems, with Windows-friendly dependencies.
- **Easy Setup**: Minimal setup required. Just place your images in a folder, and the tool handles the rest.

## 📁 How It Works

1. **Input Directory**: Place your `.heif/.heic` images in the `./IMPORT` directory.
2. **Output Directory**: The script will convert the images and save the `.jpg` files in the `./EXPORT` directory.
3. **Conversion Status**: Watch the progress bar for real-time feedback on conversion progress.

## 📜 Prerequisites

To run this script, you'll need to have Python 3.x installed along with the following dependencies:

```bash
pip install pillow-heif Pillow tqdm
```

## 🛠️ Usage Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-repo/heif-to-jpg.py.git
   cd heif-to-jpg-converter
   ```

2. **Place your images in the `IMPORT` folder**:
   - Create a folder named `IMPORT` in the same directory as the script.
   - Copy your `.heif` or `.heic` files into this folder.

3. **Run the script**:
   ```bash
   python convert_heif_to_jpg.py
   ```

4. **Find your converted images**:
   - All the converted `.jpg` files will be saved in the `EXPORT` folder, automatically created by the script.

## 🔄 Example Workflow

1. Add your HEIF/HEIC images to the `IMPORT` folder.
2. Run the script from your terminal.
3. The `.jpg` files will be created in the `EXPORT` folder with a smooth progress bar showing conversion status.

## 🖥️ Sample Command-Line Output

```
Converting files: 100%|█████████████████████████████████████████████| 10/10 [00:03<00:00,  3.21file/s]
Conversion complete! 10 files converted.
```

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Feel free to contribute! Submit a pull request or open an issue for any suggestions or bug reports.

---

### Enjoy seamless image conversion from HEIC to JPG! 🎉
