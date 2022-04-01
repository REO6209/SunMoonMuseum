import requests

REST_API_KEY = "API KEY 입력"

class KakaoTTS:
	def __init__(self, text, API_KEY=REST_API_KEY):
		self.resp = requests.post(
			url="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
			headers={
				"Content-Type": "application/xml",
				"Authorization": f"KakaoAK {API_KEY}"
			},
			data=f"<speak>{text}</speak>".encode('utf-8')
		)

	def save(self, filename="output.mp3"):
		with open(filename, "wb") as file:
			file.write(self.resp.content)

# 대화체는 여성 차분한 낭독체 or 남성 차분한 낭독체로 결정
#<voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice>
#<voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice>

# text에 듣고싶은 문장 적기.
text = """
            <voice name="WOMAN_READ_CALM">
                <say-as interpret-as="digits">1987</say-as>
            </voice>
"""

if __name__ == '__main__':
	tts = KakaoTTS(text)
    # path 경로
	tts.save(r"SAVE_path.mp3")