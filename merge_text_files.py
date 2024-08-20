import os

# Directory containing the text files
directory = 'texts'

# Output file path
output_file = 'URL_ID.txt'


# Function to merge text files
def merge_text_files(directory, output_file, encoding='utf-8'):
    file_contents = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.txt') and os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    file_contents.append(file.read())
            except UnicodeDecodeError:
                print(f"Warning: Unable to read file '{filename}' with encoding '{encoding}'. Skipping.")

    # Write all contents to the output file
    with open(output_file, 'w', encoding=encoding) as output:
        for content in file_contents:
            output.write(content + '\n')

    print(f'Merged {len(file_contents)} files into {output_file}')

# Call the function to merge text files
merge_text_files(directory, output_file)