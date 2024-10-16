# BorderCraft PDF Generator

**BorderCraft PDF Generator** is a Python-based tool that allows users to create customized PDF documents with adjustable borders, margins, page sizes, and colors. It provides an intuitive interface to specify the number of pages and modify document aesthetics, ensuring tailored outputs for various needs.

## Features

- Create PDF documents with customizable borders and margins.
- Choose from various paper sizes (A4, LETTER, Landscape A4, Portrait LETTER).
- Adjust border thickness and color.
- Change page background color.
- Generate multiple pages easily.
- User-friendly prompts for configuration.

## Requirements

- Python 3.x
- `reportlab` library

You can install the `reportlab` library using pip:

```bash
pip install reportlab
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/triadwoozie/BorderCraft.git
   ```

2. Navigate to the project directory:

   ```bash
   cd BorderCraft
   ```

3. Install the required dependencies:

   ```bash
   pip install reportlab
   ```

## Usage

1. Run the script:

   ```bash
   python bordercraft.py
   ```

2. Follow the prompts to configure your document:
   - Select paper size.
   - Input margin and border thickness.
   - Specify the number of pages.
   - Choose colors for the page background and border (or use defaults).

3. The generated PDF file will be saved as `generated_document.pdf` in the same directory.

4. If you're not satisfied with the result, you can rerun the script to make adjustments.

## Example

```bash
python bordercraft.py
```

- Choose paper size: 1 (A4)
- Enter margin distance from the page edge (in inches): 1
- Enter border thickness (in points): 2
- Enter the number of pages: 5
- Do you want to change the default colors? (y/n): n

This will create a 5-page A4 PDF with a 1-inch margin and a 2-point black border on a white background.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Author

[Your Name](https://github.com/yourusername)

## Acknowledgments

- Thanks to the [ReportLab](https://www.reportlab.com/) team for their excellent library.
