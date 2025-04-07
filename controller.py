#! /usr/bin/env python3

import subprocess
import webbrowser
import random
import time
import signal


def create_port_list(port_list):
	for x in range(100):
		port_list.append(random.randint(9000, 9041))
		port_list.append(random.randint(9043, 9098))
		
		#port_list.append(random.randint(9001, 9012))



def main():

	port_list=[]

	time_delay=[30,30,30]

	create_port_list(port_list)
	#port=port_list[port_iterator]

	while(True):
		port_iterator = random.randint(0, 98)
		#port_iterator = random.randint(1, 12)
		time_index = random.randint(0,2)

		port=port_list[port_iterator]
		print(port)
		print("Flask server running on port:", port)

		flask=subprocess.Popen(["python3", "fServer.py", str(port)])
		
		#url = f"http://localhost:{port}"
		#url = f"http://localhost:{port}/?cache_bust={random.randint(1, 1000000)}"

		#webbrowser.open(url)
		time.sleep(time_delay[time_index])
		print('sleeping')

		flask.terminate()
		flask.wait()



if __name__ == "__main__":
    main()
