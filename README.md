# 410_Moving_Target_Def.
Project for Applied Cyber Defense - implements a moving target defense

The following are the instructions for using the supplied python files to create a docker container to run the flask server.


First, ensure that all files are in the same directory level

Build the docker image from the provided docker file:

        $ docker build -t flask_server:v1

Then run that image to start the container:

	$ docker run -p 9001-9099:9001-9099 flask_server:v1

Because this uses a range of ports, if any are already in use you can separate the range like so:
	-p 9001-9042:9001-90042 -p 9043-9098:9043-9098

This is a fairly straightforward implementation, the docker container runs the controller application on startup, which continually resets the flask server to a random port- in this case every 30 seconds.

To see your service running just visit the services IP specified and the randomly chosen port, for example:

        172.17.0.2:9001

The following NPM commands were then ran by a group member in the host vm while the docker container was active using the given IP address:


	$ nmap -p- 172.17.0.2

This command will display the open port to the "attacker" in this example it's 9001

The group member would then attempt an additional scan with commands such as:

	$ nmap -sV -p 9001 172.17.0.2

	$ nmap -A -p 9001 172.17.0.2

However, the flask server will most likely have restarted before both or any additional scans can be completed - scanning the old port again will show it as closed

To shut down the server simply use ctrl+c and it will end gracefully - if desired you can also remove the docker containers using:
	
	$ docker rm <pid> 
