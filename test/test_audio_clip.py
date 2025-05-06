import os
import random
from IPython.display import Audio, display

def display_random_audio(directory):
    """Display one random WAV file from the given directory."""
    try:
        # Get list of WAV files
        files = [f for f in os.listdir(directory) if f.endswith('.wav')]
        if not files:
            print(f"No WAV files found in {directory}")
            return
        
        # Select random file
        random_file = random.choice(files)
        file_path = os.path.join(directory, random_file)
        
        # Display audio
        print(f"Playing: {file_path}")
        display(Audio(file_path))
        
    except Exception as e:
        print(f"Error playing audio from {directory}: {str(e)}")

if __name__ == "__main__":
    directories = [
        "/teamspace/studios/this_studio/audio_detect/dataset/split_data/train/real",
        # "/teamspace/studios/this_studio/audio_detect/dataset/split_data/train/fake",
        # "/teamspace/studios/this_studio/audio_detect/dataset/split_data/val/real",
        # "/teamspace/studios/this_studio/audio_detect/dataset/split_data/val/fake",
        # "/teamspace/studios/this_studio/audio_detect/dataset/split_data/test/real",
        # "/teamspace/studios/this_studio/audio_detect/dataset/split_data/test/fake"
    ]
    
    # Display one random audio file from each directory
    for directory in directories:
        display_random_audio(directory)