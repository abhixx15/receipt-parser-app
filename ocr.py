import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image_path):
    results = reader.readtext(image_path)
    return "\n".join([res[1] for res in results if res[2] > 0.4])
