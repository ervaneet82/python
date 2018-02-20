imelda="More Mayhem","Imelda May","2011",(
  (1,"Pulling the Rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Watlz")
)

print(imelda)

title,artist,year,tracks=imelda

for song in tracks:
  track,title=song
  print('\tTrack number: {}, Title: {}'.format(track,title))