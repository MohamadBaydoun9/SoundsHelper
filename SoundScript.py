from pydub import AudioSegment
import os
import noisereduce as nr

def adjust_volume(sound, dB_change):
    return sound + dB_change

def process_audio(input_path, output_path, increase_db, noise_reduce=False):
    sound = AudioSegment.from_file(input_path)
    
    # Adjust volume
    adjusted_sound = adjust_volume(sound, increase_db)
    
    # Apply noise reduction if requested
    if noise_reduce:
        audio_data = adjusted_sound.get_array_of_samples()
        reduced_audio = nr.reduce_noise(y=audio_data, sr=adjusted_sound.frame_rate)
        adjusted_sound = adjusted_sound._spawn(reduced_audio)
    
    adjusted_sound.export(output_path, format="mp3")

def process_folder(input_folder, output_folder, increase_db, noise_reduce=False, target_format="mp3"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    valid_input_formats = (".mp3", ".m4a", ".ogg")  # Supported input formats

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_input_formats):
            input_path = os.path.join(input_folder, filename)
            for i in target_format.split(","):
                print(i)
                output_filename = os.path.splitext(filename)[0] + "." + i
                output_path = os.path.join(output_folder, output_filename)
                process_audio(input_path, output_path, increase_db, noise_reduce)
            
    print("Processing completed and files saved to", output_folder)

if __name__ == "__main__":
    print("Select an action:")
    print("1. Adjust Volume and Noise Reduction")
    print("2. Convert to Different Formats")
    
    action = input("Enter your choice (1/2): ")
    
    if action == "1":
        input_folder = input("Enter the input folder path: ")
        output_folder = input("Enter the output folder path: ")
        increase_db = int(input("Enter the number of decibels to increase the volume by: "))
        suppress_noise = input("Do you want to suppress noise? (yes/no): ").lower() == "yes"
        process_folder(input_folder, output_folder, increase_db, suppress_noise)
    
    elif action == "2":
        input_folder = input("Enter the input folder path: ")
        output_folder = input("Enter the output folder path: ")
        target_format = input("Enter the target format (mp3/ogg/m4a): ").lower()

        process_folder(input_folder, output_folder, 0, False, target_format)
    
    else:
        print("Invalid choice")
