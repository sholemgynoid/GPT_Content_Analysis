import requests
import time
from ai_config import custom_spelling

upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"


# Helper for `upload_file()`
def _read_file(filename, chunk_size=5242880):
    with open(filename, "rb") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


# Uploads a file to AAI servers
def upload_file(audio_file: object, header: object) -> object:
    upload_response = requests.post(
        upload_endpoint,
        headers=header,
        data=_read_file(audio_file)
    )
    return upload_response.json()


# Request transcript for file uploaded to AAI servers
def request_transcript(upload_url, header, lang_code):
    transcript_request = {
        'audio_url': upload_url['upload_url'] ,
        'custom_spelling': custom_spelling ,
        'language_code': lang_code
    }
    transcript_response = requests.post(
        transcript_endpoint,
        json=transcript_request,
        headers=header
    )
    return transcript_response.json()


# Make a polling endpoint
def make_polling_endpoint(transcript_response):
    polling_endpoint = "https://api.assemblyai.com/v2/transcript/"
    polling_endpoint += transcript_response['id']
    return polling_endpoint


# Wait for the transcript to finish
def wait_for_completion(polling_endpoint, header):
    while True:
        polling_response = requests.get(polling_endpoint, headers=header)
        polling_response = polling_response.json()

        if polling_response['status'] == 'completed':
            break

        time.sleep(25)


# Get the paragraphs of the transcript
def get_paragraphs(polling_endpoint: object, header: object) -> object:
    paragraphs_response = requests.get(polling_endpoint + "/paragraphs", headers=header)
    if (
        paragraphs_response.status_code == 200 and
        paragraphs_response.headers["content-type"].strip().startswith("application/json")
    ):

        paragraphs_response = paragraphs_response.json()

        paragraphs = []
        for para in paragraphs_response['paragraphs']:
            paragraphs.append(para)

        return paragraphs
    else:
        print("Error from server: " + str(paragraphs_response.content))
