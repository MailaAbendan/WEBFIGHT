import time
import webbrowser

def spawn_webfight():
    # Prompt user for website name
    website = input("WEBFIGHT: WHAT DO YOU WANT THE WEBSITE TO UPLOAD IT? (e.g., AHH.com): ")
    
    if website:
        print(f"WEBFIGHT: Ok, I will upload {website}")

        # Simulate upload progress
        for i in range(1, 101):
            time.sleep(0.05)  # Simulate time delay for upload
            print(f"WEBFIGHT: Uploading... ({i}/100)")

        # Upload complete
        print("WEBFIGHT: Upload complete!")
        
        # Spawn Google URL pop-up
        webbrowser.open(f"https://{website}")
    else:
        print("WEBFIGHT: No website provided. Exiting program.")

# Run the program
spawn_webfight()
