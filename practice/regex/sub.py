import re
text = "Python  && for && beginner || is a very cool website"

pattern = re.sub(r'[&&]+',"and",text).sub(r'[||]+', "or",text)

print(pattern)