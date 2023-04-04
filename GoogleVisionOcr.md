```
import io
import os

#!pip install google-api-python-client google-cloud google-auth google-auth-oauthlib google-auth-httplib2
#!pip install --upgrade google-cloud-vision

#from google.oauth2 import service_account

#credentials = service_account.Credentials.from_service_account_file('E:\\projects\\apt-mark-382708-22af1afdddb6.json')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="E:\\projects\\apt-mark-382708-22af1afdddb6.json"

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

detect_text(r"C:\Users\Acer\Downloads\fyp\download.jpg")
```
