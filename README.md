# pdf-audiobook

pdf-audiobook is a simple Python script that converts PDF documents to speech. This project uses `PyPDF2` to read the PDF files and `pyttsx3` to convert the extracted text to audio.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Black-Scorpio/pdf-audiobook.git
    cd pdf-audiobook
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

### Usage

Replace `resume.pdf` with the path to the PDF file you want to convert to audio. You can modify the script to specify the range of pages you want to read.

1. Run the script:

    ```sh
    python pdf_to_speech.py
    ```

By default, the script reads from the first page to the last page of the PDF. You can specify the start and end pages by modifying the `start_page` and `end_page` variables in the script.

### Example

To convert the text from `resume.pdf` to speech, execute the following command in your terminal:

```sh
python pdf_to_speech.py
