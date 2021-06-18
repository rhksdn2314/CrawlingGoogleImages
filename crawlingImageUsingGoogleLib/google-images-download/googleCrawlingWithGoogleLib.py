#-*- coding: utf-8 -*-

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"이영자 채널 LYJ CH.,노마드 코더 Nomad Coders,김준표,뻑가 PPKKa,코미꼬", "limit":100, "print_urls":True, "format": "jpg"}

paths = response.download(arguments)

print(paths)