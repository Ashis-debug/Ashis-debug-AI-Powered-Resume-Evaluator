import pdf2image
import base64
import io


# Helper function to convert PDF bytes into images and encode them in base64
def convert_pdf_to_images(pdf_bytes):
    images = pdf2image.convert_from_bytes(pdf_bytes)
    pdf_parts = []
    for image in images:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts.append({
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64
        })
    return pdf_parts
