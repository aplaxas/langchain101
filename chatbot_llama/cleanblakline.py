import os

# Specify the directory containing text files
directory_path = './data/calltext/'

# Iterate through each text file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        input_filepath = os.path.join(directory_path, filename)

        # Read the file
        with open(input_filepath, 'r', encoding='utf-8') as f:
            input_text = f.read()

        # Remove blank lines
        filtered_lines = [
            line for line in input_text.splitlines() if line.strip()]
        output_text = '\n'.join(filtered_lines)

        # Create output filename
        output_filename = f'filtered_{filename}'
        output_filepath = os.path.join(directory_path, output_filename)

        # Write the output back to a new file
        with open(output_filepath, 'w', encoding='utf=8') as f:
            f.write(output_text)
