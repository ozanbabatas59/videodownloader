!pip install pytube yt-dlp

import os

# Video URL'sini girin
video_url = input("YouTube Video URL'sini girin: ")

# İndirme işlemi
print("Video indiriliyor...")
os.system(f"yt-dlp -o '/content/%(title)s.%(ext)s' {video_url}")
print("İndirme tamamlandı! Dosya /content/ klasöründe saklanıyor.")
