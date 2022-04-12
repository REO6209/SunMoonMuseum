'''
- API 가이드
https://cloud.google.com/text-to-speech/docs/libraries

- 블로그
https://youngq.tistory.com/36?category=764303

- 언어 감지
https://pypi.org/project/langdetect/

- 음성
한글
    남자 MAN_DIALOG_BRIGHT
    여자 WOMAN_READ_CALM

영어
    남자 en-US-Wavenet-D
    여자 en-US-Wavenet-F

일본어
    남자 ja-JP-Wavenet-D
    여자 ja-JP-Wavenet-B

중국어 - 북경어
    남자 cmn-CN-Wavenet-C
    여자 cmn-CN-Wavenet-A
'''

# 환경변수
import os
from google.cloud import storage
# Google TTS API
from google.cloud import texttospeech
# 언어 감지
from langdetect import detect
# Kakao TTS API
import requests

# Kakao
REST_API_KEY = "0c2adb2801124d6dc831a31be5fb9853"

# 환경 변수 설정 - 발급받은 Google API json 파일 경로를 넣는다.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"/Users/gungo/Documents/강의자료/SW심화/SWproject/sunmoon-museum-004f00e6d677.json"

# 인증 확인
# storage_client = storage.Client()
# buckets = list(storage_client.list_buckets())
# print(buckets)


# Google TTS API
client = texttospeech.TextToSpeechClient()

'''음성옵션'''
# 언어 코드랑 음성 옵션 정하기 - English / en-US-Wavenet-F - 여성
voice_en_W = texttospeech.VoiceSelectionParams(
    language_code="en-US", name = "en-US-Wavenet-F", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
# 언어 코드랑 음성 옵션 정하기 - English / en-US-Wavenet-D - 남성
voice_en_M = texttospeech.VoiceSelectionParams(
    language_code="en-US", name = "en-US-Wavenet-D", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# 언어 코드랑 음성 옵션 정하기 - Japenese / ja-JP-Wavenet-B - 여성
voice_ja_W = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", name = "ja-JP-Wavenet-B", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
# 언어 코드랑 음성 옵션 정하기 - Japenese / ja-JP-Wavenet-D - 남성
voice_ja_M = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", name = "ja-JP-Wavenet-D", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# 언어 코드랑 음성 옵션 정하기 - Chinese / cmn-CN-Wavenet-A - 여성
voice_ch_W = texttospeech.VoiceSelectionParams(
    language_code="cmn-CN", name = "cmn-CN-Wavenet-A", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
# 언어 코드랑 음성 옵션 정하기 - Chinese / cmn-CN-Wavenet-C - 남성
voice_ch_M = texttospeech.VoiceSelectionParams(
    language_code="cmn-CN", name = "cmn-CN-Wavenet-C", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# 오디오 파일 형식 정하기
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

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


def exchange_english(input_text, gender):
    # 텍스트 입력
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(
        input=synthesis_input, voice= voice_en_M if gender == 'M' else voice_en_W, audio_config=audio_config
        )
    return response.audio_content

def exchange_chinese(input_text, gender):
    # 텍스트 입력
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(
        input=synthesis_input, voice= voice_ch_M if gender == 'M' else voice_ch_W, audio_config=audio_config
        )
    return response.audio_content

def exchange_japanese(input_text, gender):
    # 텍스트 입력
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(
        input=synthesis_input, voice= voice_ja_M if gender == 'M' else voice_ja_W, audio_config=audio_config
        )
    return response.audio_content

def exchange_korea(input_text, gender):
    # 언어 코드랑 음성 옵션 정하기 - Korea / WOMAN_READ_CALM - 여성 차분한 낭독체 & MAN_DIALOG_BRIGHT - 남성 밝은 대화체
    voice_k = ["""<voice name="WOMAN_READ_CALM">{}</voice>""".format(input_text),
    """<voice name="MAN_DIALOG_BRIGHT">{}</voice>""".format(input_text)]

    if __name__ == '__main__':
        if gender == 'W':
            tts = KakaoTTS(voice_k[0])
        elif gender == 'M':
            tts = KakaoTTS(voice_k[1])
    
    return tts
        
def makeFile(textList, gender):  
    for i, text in enumerate(textList):
        langType = detect(text)

        # 언어가 영어인 경우
        if langType == 'en':
            with open(r"/Users/gungo/Documents/강의자료/SW심화/SWproject/TTS/tts_voice/"+str(i)+"_en"+gender+".mp3", "wb") as out:
                out.write(exchange_english(text, gender))

        # 언어가 중국어인 경우
        elif langType == 'zh-cn':
            with open(r"/Users/gungo/Documents/강의자료/SW심화/SWproject/TTS/tts_voice/"+str(i)+"_zh-cn"+gender+".mp3", "wb") as out:
                out.write(exchange_chinese(text, gender))

        # 언어가 일본어인 경우
        elif langType == 'ja':
            with open(r"/Users/gungo/Documents/강의자료/SW심화/SWproject/TTS/tts_voice/"+str(i)+"_ja"+gender+".mp3", "wb") as out:
                out.write(exchange_japanese(text, gender))

        # 언어가 한글인 경우
        elif langType == 'ko':
            exchange_korea(text, gender).save(r"/Users/gungo/Documents/강의자료/SW심화/SWproject/TTS/tts_voice/"+str(i)+"_ko"+gender+".mp3")

# 텍스트 리스트
textList = ['Hello, World!', "你好，世界！", "こんにちは！", "안녕하세요!"]
# 성별
gender = ['W', 'M']

# 실행
makeFile(textList, gender[0])