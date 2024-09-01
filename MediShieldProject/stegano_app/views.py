from django.shortcuts import render
import stepic
from PIL import Image
import io

def index(request):
    return render(request, 'index.html')

def hide_text_in_image(image, text):
    data = text.encode('utf-8')
    return stepic.encode(image, data)

def encryption_view(request):
    message = ''
    if request.method == 'POST':
      
        patient_name = request.POST['patient_name']
        age = request.POST['age']
        gender = request.POST['gender']
        contact_info = request.POST['contact_info']
        medical_history = request.POST['medical_history']
        medication_management = request.POST['medication_management']
        lab_results = request.POST['lab_results']
        clinical_notes = request.POST['clinical_notes']
        immunization_records = request.POST['immunization_records']
        allergies_reactions = request.POST['allergies_reactions']
        treatment_plans = request.POST['treatment_plans']
        billing_info = request.POST['billing_info']

       
        text_to_hide = f"{patient_name},{age},{gender},{contact_info},{medical_history},{medication_management},{lab_results},{clinical_notes},{immunization_records},{allergies_reactions},{treatment_plans},{billing_info}"

        image_file = request.FILES['image']
        image = Image.open(image_file)

       
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

       
        if image.format == 'JPEG':
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

        new_image = hide_text_in_image(image, text_to_hide)

       
        image_path = 'project_folder/encrypted_images/' + 'new_' + image_file.name.split('.')[0] + '.png'
        new_image.save(image_path, format="PNG")

        message = 'Text has been encrypted in the image.'

    return render(request, 'encryption.html', {'message': message})


def extract_text_from_image(image):
    data = stepic.decode(image)
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data

def decryption_view(request):
    text = ''
    if request.method == 'POST':
        image_file = request.FILES['image']
        image = Image.open(image_file)

        
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        
        if image.format == 'JPEG':
            buffer = io.BytesIO()
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

        
        text = extract_text_from_image(image)

    
    if text:
        decrypted_data = text.split(',')
        patient_name = decrypted_data[0]
        age = decrypted_data[1]
        gender = decrypted_data[2]
        contact_info = decrypted_data[3]
        medical_history = decrypted_data[4]
        medication_management = decrypted_data[5]
        lab_results = decrypted_data[6]
        clinical_notes = decrypted_data[7]
        immunization_records = decrypted_data[8]
        allergies_reactions = decrypted_data[9]
        treatment_plans = decrypted_data[10]
        billing_info = decrypted_data[11]

        return render(request, 'decryption.html', {
            'text': text,
            'patient_name': patient_name,
            'age': age,
            'gender': gender,
            'contact_info': contact_info,
            'medical_history': medical_history,
            'medication_management': medication_management,
            'lab_results': lab_results,
            'clinical_notes': clinical_notes,
            'immunization_records': immunization_records,
            'allergies_reactions': allergies_reactions,
            'treatment_plans': treatment_plans,
            'billing_info': billing_info
        })

    return render(request, 'decryption.html', {'text': text})