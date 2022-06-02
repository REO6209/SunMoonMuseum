import requests

headers = {
    # requests won't add a boundary if this header is set when you pass files=
    'Content-Type': 'multipart/form-data',
    'Authorization': 'KakaoAK 6eb73b92aef84c8cac31921c30c1b5fb',
}

files = {
    'image': open('skew_corrected.png', 'rb'),
}

response = requests.post('https://dapi.kakao.com/v2/vision/text/ocr', headers=headers, files=files)
token = response.json()

print(response)
print(token)