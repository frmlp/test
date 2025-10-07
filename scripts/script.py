from datetime import datetime
import os

def create_file():
    # Get the repository root directory
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Create the files directory if it doesn't exist
    files_dir = os.path.join(repo_root, 'files')
    os.makedirs(files_dir, exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create file with timestamp as name
    file_path = os.path.join(files_dir, f'{timestamp}.txt')
    
    # Write Lorem ipsum to the file
    with open(file_path, 'w') as f:
        f.write('Lorem ipsum')

if __name__ == '__main__':
    create_file()
