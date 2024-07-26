import PyPDF2
import pyttsx3


def pdf_to_speech(pdf_file, start_page=0, end_page=None):
    # Initialize the PDF reader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages in the PDF
    total_pages = len(pdf_reader.pages)

    # If end_page is not specified, read until the last page
    if end_page is None:
        end_page = total_pages

    # Initialize the text-to-speech engine
    tts_engine = pyttsx3.init()

    # Loop through the specified range of pages
    for page_num in range(start_page, end_page):
        # Extract text from the page
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Convert the text to speech
        tts_engine.say(text)

    # Wait until all speech commands are finished
    tts_engine.runAndWait()


if __name__ == "__main__":
    pdf_file_path = "resume.pdf"
    start_page = 0
    end_page = None

    pdf_to_speech(pdf_file_path, start_page, end_page)
