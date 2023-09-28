import os

def print_all_files_content(directory):
    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry)
        if os.path.isdir(entry_path):
            # Recursively explore subdirectories
            print_all_files_content(entry_path)
        else:
            # Check if the entry has a dot (.) in its filename
            if "." in entry:
                print(f"Contents of {entry_path}:")
                try:
                    with open(entry_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(content)
                    print("=" * 40)  # Separator between files
                except UnicodeDecodeError:
                    print(f"Cannot read {entry_path} as text file (UnicodeDecodeError)")

# Start the search from the "letsgo" directory
print_all_files_content("letsgo")
