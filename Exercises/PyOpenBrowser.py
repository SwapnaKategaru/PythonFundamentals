import time
import webbrowser

count = 0

while count < 1:
    time.sleep(5)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count = count + 1
    print('completed' + str(count))
