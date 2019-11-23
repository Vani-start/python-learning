#threading
#threading used to run multiple functions simultaniously

import threading
import time

def my_function():
	print("starting thread")
	time.sleep(3)
	print("Stop thread")
	
	
threads=[]

for i in range(5):
	th=threading.Thread(target= my_function())
	th.start()
	threads.append(th)
	
for th in threads:
	th.join()

