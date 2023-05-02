from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app=Flask(__name__)
@app.get('/summary')

def summary_api():
    url=request.args.get('url',' ')
    video_id=url.split('=')[1]
    summary=get_summary(get_transcript(video_id))
    return summary, 200

def get_transcript(video_id):
    transcript_list=YouTubeTranscriptApi.get_transcript(video_id)
    transcript=' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    summarizer=pipeline('summarization')
    summary=''
    for i in range(0,(len(transcript)//1000)+1):
        summary_text= summarizer(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary= summary+ summary_text+ ' '
    return summary

if __name__=='__main__':
    app.run()  
# from youtube_transcript_api import YouTubeTranscriptApi
# from transformers import pipeline
# print("hello")
# # Enter the URL of the YouTube video you want to summarize
# url = 'https://www.youtube.com/watch?v=lcmadPVaHVA'

# # Get the video ID from the URL
# video_id = url.split('=')[1]

# # Get the transcript of the video using the YouTubeTranscriptApi
# transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
# transcript = ' '.join([d['text'] for d in transcript_list])

# # Summarize the transcript using the transformers pipeline
# summarizer = pipeline('summarization')
# summary = summarizer(transcript, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

# # Print the summary
# print(summary)
