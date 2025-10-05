from datetime import datetime
import os

def create_file():
    # Create the files directory if it doesn't exist
    os.makedirs('files', exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create file with timestamp as name
    file_path = f'files/{timestamp}.txt'
    
    # Write Lorem ipsum to the file
    with open(file_path, 'w') as f:
        f.write('Lorem ipsum')

if __name__ == '__main__':
    create_file()
