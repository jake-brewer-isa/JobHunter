import os
import zipfile
import requests

def download_chromedriver(directory):
    # Direct URL to the ChromeDriver zip file
    download_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip"

    # Make the HTTP request to download the zip file
    response = requests.get(download_url)
    if response.status_code != 200:
        raise Exception(f"Failed to download ChromeDriver: {response.status_code}")

    # Save the zip file
    zip_path = os.path.join(directory, "chromedriver.zip")
    with open(zip_path, "wb") as file:
        file.write(response.content)

    # Extract the executable from the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            filename = os.path.basename(member)
            # skip directories and non .exe files
            if not filename or not filename.endswith('.exe'):
                continue

            # copy file (taken from zipfile's extract)
            source = zip_ref.open(member)
            target = open(os.path.join(directory, filename), "wb")
            with source, target:
                target.write(source.read())

    # Clean up the downloaded zip file
    os.remove(zip_path)

    print("ChromeDriver downloaded and extracted successfully.")

# Example usage
download_directory = os.getcwd()  # Or any other directory where you want to save the driver
download_chromedriver(download_directory)
