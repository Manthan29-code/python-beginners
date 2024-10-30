# PDF Downloader GUI Application

This Python application allows users to download PDFs for specific subjects from GTU's website by entering a subject code and subject name. The app uses a Tkinter-based GUI for a user-friendly experience.

## Requirements

To run this application, you'll need:

- **Python 3.x**
- **Requests library**: Install via pip
  ```bash
  pip install requests
  ```

## How to Use

### Launch the Application
Run the Python script in your environment. This will open a window named "PDF Downloader".
  ```bash
  python GTU_PYQ.py
  ```

## Enter Subject Code
In the app's text field labeled **"Subject Code,"** enter the code of the subject you want to download PDFs for.

## Enter Subject Name
In the **"Subject Name"** field, type the name of the subject. This name will be used to save the downloaded PDFs.

## Start the Download
Click the **"Download PDFs"** button. The application will begin fetching PDFs from GTU's website based on the provided subject code.

## Check the Status
The download progress and status for each file will be displayed in the scrollable text area at the bottom of the window. Each PDF file will be saved in the current working directory with names based on the subject name and year (e.g., `SubjectName_S17.pdf`).

## Example Use Case

Suppose you want to download PDFs for a subject with:

- **Subject Code**: `12345`
- **Subject Name**: `Mathematics`

1. Enter `12345` in the **Subject Code** field.
2. Enter `Mathematics` in the **Subject Name** field.
3. Click **Download PDFs**.

If successful, the app will save the files in the current directory and display the success message for each file in the output area.

## Troubleshooting

- **Invalid Subject Code**: If the subject code is incorrect or the file doesn't exist on the server, the output area will display a message stating that the file is not available.
- **Internet Connection**: Ensure that you have an active internet connection, as this app fetches files from an online source.

## Notes

- PDFs are saved in the working directory, so check your terminal’s path or use `os.chdir()` to specify a different directory.
- The app only downloads files from GTU’s website, so files not hosted there will not be accessible.

