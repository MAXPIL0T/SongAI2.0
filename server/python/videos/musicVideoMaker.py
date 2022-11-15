from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import sys
from get_genre import classify_from_web
import random
import os


genre_to_file = {
    'country': 2,
    'metal': 3,
    'folk': 5,
    'funk': 3,
    'indie': 5,
    'jazz': 5,
    'k-pop': 2,
    'pop': 18,
    'r&b': 1,
    'rap': 4,
    'rock': 11,
}


def genre_to_song(genre):
    return '{}_{number}.mp3'.format(genre.lower(), number=random.randrange(1, genre_to_file[genre.lower()] + 1))


vocal_path = sys.argv[1]
text = sys.argv[2]
classified_genre = classify_from_web(text)
print(classified_genre)

video_name = {
    "Folk": "reggae.m4v",
    "Rap": "trap.m4v",
    "Metal": "headbanger.m4v",
    "K-Pop": "kpop.m4v",
    "Disco": "gme.m4v",
    "Pop": "lo-fi.m4v",
    "Funk": "rickroll.m4v",
    "Rock": "rock.m4v",
    "R&B": "trap.m4v",
    "Country": "idk.m4v",
    "Jazz": "jazz.m4v",
    "Indie": "high_school.m4v"
}


def genre_to_video(special_genre):
    print(special_genre)
    return video_name.get(special_genre, "marius.mp4")


video_clip = VideoFileClip("{}/server/python/videos/{}".format(os.getcwd(), genre_to_video(classified_genre)))
genre_audio = AudioFileClip("{}/server/python/songs/{}".format(os.getcwd(), genre_to_song(classified_genre)))
vocal_audio = AudioFileClip(vocal_path)

genre_clip = genre_audio.volumex(0.5)
vocal_clip = vocal_audio.volumex(2.0)

final_audio = CompositeAudioClip([genre_clip, vocal_clip])
final_clip = video_clip.set_audio(final_audio)

final_clip.write_videofile("./server/python/output/{}".format(sys.argv[3]))

print(sys.argv[3])
sys.stdout.flush()
