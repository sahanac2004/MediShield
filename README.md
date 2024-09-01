# MediShield - Secure Medical Image Steganography Platform

MediShield is a web-based platform built using Django for securely hiding sensitive medical information within images. This platform employs steganography techniques to embed encrypted patient data within medical images, ensuring the confidentiality and integrity of patient information without compromising the original image quality.

## Features

- **Data Encryption**: Securely hides patient information within medical images.
- **Data Decryption**: Extracts and displays the hidden information from the images.
- **User-Friendly Interface**: Easy-to-use web interface for uploading images and managing data.
- **Secure Handling**: Ensures confidentiality and integrity of patient data.

## Technologies Used

- **Backend**: Django
- **Image Processing**: Python Imaging Library (PIL)
- **Steganography**: Stepic library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/medishield.git
   cd medishield
2.Create a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3.Install Required Packages:

bash
Copy code
pip install -r requirements.txt

4.Run the Django Server:

bash
Copy code
python manage.py runserver

Open in Web Browser: Visit http://127.0.0.1:8000 to access the platform.

#Usage
Encryption
Go to the "Encryption" page.
Fill in the patient information form and upload a medical image.
Click on "Encrypt" to hide the information within the image.
The encrypted image will be saved, and a confirmation message will be displayed.
Decryption
Go to the "Decryption" page.
Upload an image containing hidden data.
Click on "Decrypt" to extract and view the hidden information.
#Project Structure
views.py: Contains the logic for encryption and decryption of data.
templates/: HTML files for rendering the user interface.
project_folder/encrypted_images/: Directory to store encrypted images.
#File Upload and Handling
Upload an image on the "Encryption" page.
The system will process the image and save it with hidden data.
Use the "Decryption" page to upload and retrieve hidden information.
Contributing
Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request.
#
### Additional Steps:
- Save this content as `README.md` in the root directory of your GitHub repository.
- Make sure to update the placeholders like `sahanac2004`, `sahanac629@gmail.com `, and the GitHub repository link to reflect your information.
