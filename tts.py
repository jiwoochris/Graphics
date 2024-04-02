from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="다 사람이면 주량 알려줘. 맥주 얼마나 마셔?"
)

response.stream_to_file(speech_file_path)