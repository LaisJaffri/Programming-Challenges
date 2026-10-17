import urllib.request
fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
new = 0
for i in range(1,101):
    start = mystr.find("chart-item-content relative",new)
    song_first = mystr.find("<span>",start)
    song_second = mystr.find("</span>",song_first)
    artist_first = mystr.find("<span>",song_first+1)
    artist_second = mystr.find("</span>",artist_first)
    artist = (mystr[artist_first+6:artist_second]).replace("/<wbr>",", ")
    #artist = artist.replace("/<wbr>",",")
    #print(start,song_first,song_second)
    #print(mystr[song_first+6:song_second])
    #print(mystr[artist_first+6:artist_second])
    print(f"Number {i} {mystr[song_first+6:song_second]} by {artist}")
    new = start + 1






"""
for i in range(1,11):
    start = mystr.find("chart-item-content relative",new)
    first = mystr.find("/songs/",start)
    second = mystr.find("/",first+7)
    print(f"Number {i} {mystr[first+7:second]}")
    new = start + 1
"""   
""""
for i in range(10):
    start = mystr.find("chart-item-content relative",new+10000)
    start_song = mystr.find("data-title=")
    second_song  = mystr.find("data-artist",start_song)
    start_artist = mystr.find("data-artist=")
    second_artist= mystr.find("type",start_artist)
    song = mystr[start_song+12:second_song-2]
    artist = mystr[start_artist+13:second_artist-2]
    new = mystr.find("<!--[-->",start)
    print(song,artist)
    print(new)
"""