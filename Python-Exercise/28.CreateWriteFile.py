# WAP TO CREATE A FILE AND WRITE TEXT INTO THE FILE

def create_write_file(file_name, text):
    with open(file_name, "w") as file:
        file.write(text)
    print(f"File {file_name} created and text written successfully.")

# Example usage
create_write_file("example.txt", "This is an example of text written to a file.")
