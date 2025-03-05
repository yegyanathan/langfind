def get_text_from_file(file_path):
    """
    Reads a text file and returns its contents as a string.

    :param file_path: Path to the text file
    :return: File contents as a string
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
# file_path = "bank_document.txt"  
# text_data = get_text_from_file(file_path)
# print(text_data)
