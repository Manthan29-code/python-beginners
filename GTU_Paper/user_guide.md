# GTU Paper Downloader 

A sleek and user-friendly GUI application to download GTU (Gujarat Technological University) previous year question papers. This tool automatically fetches both Summer and Winter examination papers from 2017 to 2023.

![GTU Paper Downloader](https://img.shields.io/badge/GTU-Paper%20Downloader-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Quick Start

### Prerequisites

- Python 3.x installed on your system
- Internet connection

### Installation

1. **Clone or download** this repository to your local machine
2. **Install required dependencies** by running:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Navigate to the application directory and run:
```bash
python GTU_PYQ.py
```

## Features

- **User-friendly GUI** interface
- **Automatic downloading** of papers from 2017 to 2023
- **Both Summer and Winter** examination papers
- **Progress tracking** with visual feedback
- **Error handling** for network issues
- **Organized file naming** convention

## How to Use

### Step 1: Launch the Application
- Double-click the `GTU_PYQ.py` file or run it from the terminal
- A window titled "PDF Downloader" will appear

### Step 2: Enter Subject Details
1. In the **Subject Code** field:
   - Enter the GTU subject code (e.g., `3110003`)
   - This is the official code assigned by GTU

2. In the **Subject Name** field:
   - Enter a name for the subject (e.g., `Programming_in_C`)
   - This will be used in the filename of downloaded PDFs
   - Avoid using special characters

### Step 3: Download
1. Click the **Download PDFs** button
2. The application will:
   - Attempt to download papers from 2017 to 2023
   - Show progress in the text area below
   - Save PDFs in the same folder as the application

### Step 4: Monitor Progress
- Green checkmarks indicate successful downloads
- Red crosses indicate unavailable papers
- Progress is shown in real-time in the scrollable text area

## File Naming Convention

Downloaded files follow this pattern:
- Summer papers: `SubjectName_S[YY].pdf`
- Winter papers: `SubjectName_W[YY].pdf`

Example:
- `Programming_in_C_S19.pdf` (Summer 2019)
- `Programming_in_C_W19.pdf` (Winter 2019)

## Troubleshooting

### Common Issues and Solutions

1. **"No such file or directory" error**
   - Ensure you're running the script from its directory
   - Check if you have write permissions

2. **Download failures**
   - Verify your internet connection
   - Check if the subject code is correct
   - Some papers might not be available on GTU's website

3. **"Module not found" error**
   - Run `pip install -r requirements.txt` again
   - Ensure Python is properly installed

## Note

- Papers are downloaded directly from GTU's official website
- Some papers might not be available for all years
- Download speed depends on your internet connection
- Files are saved in PDF format

## Contributing

Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
*Made with  for GTU students*
