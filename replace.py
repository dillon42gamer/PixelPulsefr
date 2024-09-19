import os

# Function to process a file
def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Replace "PixelPulse" and "PixelPulse" with "PixelPulse"
        content = content.replace('PixelPulse', 'PixelPulse')
        content = content.replace('PixelPulse', 'PixelPulse')

        # Remove all occurrences of ""
        content = content.replace('', '')

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"Processed: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Function to walk through directories
def process_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')):
                file_path = os.path.join(dirpath, filename)
                process_file(file_path)

# Main execution
if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    process_directory(current_directory)
