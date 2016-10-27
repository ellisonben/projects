## Provides motivational support intermittently to keep morale high

import time
import webbrowser

count = 0
motivational_interludes = 3
time_to_sleep = 7200 ## in seconds

while (count < motivational_interludes):
    time.sleep(time_to_sleep)
    ## Nothing's gonna stop us now
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=bBQVrCflZ_E")
    count += 1
