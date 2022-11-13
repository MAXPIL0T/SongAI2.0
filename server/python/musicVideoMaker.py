from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import sys
from get_genre import classify_from_web
import random
import os

def getRange(genre):
    if genre == 'country': return 2
    if genre == 'metal': return 3
    if genre == 'folk': return 5
    if genre == 'funk': return 3
    if genre == 'indie': return 5
    if genre == 'jazz': return 5
    if genre == 'k-pop': return 2
    if genre == 'pop': return 18
    if genre == 'r&b': return 1
    if genre == 'rap': return 4
    if genre == 'rock': return 11


def genre_to_song(genre):
    return '{}_{number}.mp3'.format(genre.lower(), number=random.randrange(1, getRange(genre.lower()) + 1))

vocal_path = sys.argv[1]
text = sys.argv[2]
genre = classify_from_web(text)
print(genre)

video_name={
    "Folk":"reggae.mp4",
    "Rap":"trap.mp4",
    "Metal":"headbanger.mp4",
    "K-Pop":"kpop.mp4",
    "Disco":"gme.mp4",
    "Pop":"trap.mp4",
    "Funk":"rickroll.mp4",
    "Rock":"rock.mp4",
    "R&B":"trap.mp4",
    "Country":"idk.mp4",
    "Rap":"trap.mp4",
    "Jazz":"jazz.mp4",
    "Indie":"highschool.mp4"
}
def genre_to_video(genre):
    print(genre)
    return video_name.get(genre, "marius.mp4")

video_clip = VideoFileClip("{}\\server\\python\\videos\\{}".format(os.getcwd(), genre_to_video(genre)))
genre_audio = AudioFileClip("{}\\server\\python\\songs\\{}".format(os.getcwd(), genre_to_song(genre)))
# video_clip = VideoFileClip('./server/python/100_0001.mov')
vocal_audio = AudioFileClip(vocal_path)

genre_clip = genre_audio.volumex(0.5)
vocal_clip = vocal_audio.volumex(2.0)

final_audio = CompositeAudioClip([genre_clip, vocal_clip])

final_clip = video_clip.set_audio(final_audio)
final_clip.write_videofile("./server/python/output/{}".format(sys.argv[3]))

print(sys.argv[3])
sys.stdout.flush()