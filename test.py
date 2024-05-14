import requests
import fastavro
import io

url = 'https://example.com/path/to/avrofile.avro'

# Request the first few kilobytes of the file (adjust size as needed)
headers = {'Range': 'bytes=0-10239'}
response = requests.get(url, headers=headers)
response.raise_for_status()

# Read the Avro file content from the partial content
bytes_io = io.BytesIO(response.content)
reader = fastavro.reader(bytes_io)

# Print the first 100 records
for i, record in enumerate(reader):
    if i >= 100:
        break
    print(record)