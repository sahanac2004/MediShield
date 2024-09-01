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
    \`\`\`bash
    git clone https://github.com/yourusername/medishield.git
    cd medishield
    \`\`\`

2. **Create a Virtual Environment**:
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    \`\`\`

3. **Install Required Packages**:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4. **Run the Django Server**:
    \`\`\`bash
    python manage.py runserver
    \`\`\`

5. **Open in Web Browser**: Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the platform.

## Usage

### Encryption

1. Go to the "Encryption" page.
2. Fill in the patient information form and upload a medical image.
3. Click on "Encrypt" to hide the information within the image.
4. The encrypted image will be saved, and a confirmation message will be displayed.

### Decryption

1. Go to the "Decryption" page.
2. Upload an image containing hidden data.
3. Click on "Decrypt" to extract and view the hidden information.

## Project Structure

- **views.py**: Contains the logic for encryption and decryption of data.
- **templates/**: HTML files for rendering the user interface.
- **project_folder/encrypted_images/**: Directory to store encrypted images.

## File Upload and Handling

- Upload an image on the "Encryption" page.
- The system will process the image and save it with hidden data.
- Use the "Decryption" page to upload and retrieve hidden information.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Acknowledgements

- Built with Django and the Python Imaging Library (PIL).
- Utilizes the Stepic library for steganography.

## Contact

For any questions or feedback, please reach out to [sahanac629@gmail.com ].
