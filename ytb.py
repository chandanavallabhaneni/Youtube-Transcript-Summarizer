from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

# youtube_video = "https://www.youtube.com/watch?v=HMJO_wYrXNQ"

def sumriz(youtube_video):
  video_id = youtube_video.split("=")[1]
  YouTubeTranscriptApi.get_transcript(video_id)
  transcript = YouTubeTranscriptApi.get_transcript(video_id)
  transcript[0:5]
  result = ""
  for i in transcript:
      result += ' ' + i['text']
  # print(result)
  # print(len(result))

  summarizer = pipeline('summarization')

  num_iters = int(len(result)/1000)
  summarized_text = []
  for i in range(0, num_iters + 1):
    start = 0
    start = i * 1000
    end = (i + 1) * 1000
    print("input text \n" + result[start:end])
    out = summarizer(result[start:end])
    out = out[0]
    out = out['summary_text']
    print("Summarized text\n"+out)
    summarized_text.append(out)

  return(str(summarized_text))