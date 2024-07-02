import requests
import json
import time

from MongoDB_Utilities import CONNECT_MONGODB
from MongoDB_Utilities import IMPORT_DOCS_IN_MONGO

base_url = "https://api.assemblyai.com/v2"

headers = {
    "authorization": "1b4e64cd2c57414baa5a725efcba7d8f"
}

with open("/Users/vittorio/Desktop/TG1_10355.flac" , "rb") as f:
  response = requests.post(base_url + "/upload",
                          headers=headers,
                          data=f)

FILE_URL = response.json()["upload_url"]

# replace with your API token
YOUR_API_TOKEN = "1b4e64cd2c57414baa5a725efcba7d8f"

# URL of the file to transcribe
#FILE_URL = "https://storage.cloud.google.com/fileaudio_oss/TG1_10355.flac"

# AssemblyAI transcript endpoint (where we submit the file)
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

# request parameters where Topic Detection has been enabled
data = {
  "audio_url": FILE_URL,
  "language_code": "it",
  "iab_categories": True,
  "speaker_labels": True
}

# HTTP request headers
headers={
  "Authorization": YOUR_API_TOKEN,
  "Content-Type": "application/json"
}

# submit for transcription via HTTP request
response = requests.post(transcript_endpoint,
                         json=data,
                         headers=headers)

# polling for transcription completion
polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{response.json()['id']}"

while True:
    transcription_result = requests.get(polling_endpoint, headers=headers).json()

    if transcription_result['status'] == 'completed':
        # print the results
        print(json.dumps(transcription_result, indent=2))
        break
    elif transcription_result['status'] == 'error':
        raise RuntimeError(f"Transcription failed: {transcription_result['error']}")
    else:
        time.sleep(3)