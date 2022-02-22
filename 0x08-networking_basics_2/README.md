# Networking basics #1

- ###### 0-change_your_home_IP
Bash script that configures an Ubuntu server with the below requirements.<br>
Requirements: <br>
	      - localhost resolves to `127.0.0.2`
	      - facebook.com resolves to `8.8.8.8.`

- ###### 1-show_attached_IPs
Bash script that displays all active IPv4 IPs on the machine s executed on.it

- ###### 100-port_listening_on_localhost
Bash script that listens on port 98 on localhost.</br>
- ###### Terminal 0
Starting my script.</br>
- ###### Terminal 1
Connecting to localhost on port 98 using telnet and typing some text.
- ###### Terminal 0
Receiving the text on the other side.

Note: For the sake of the exercise, this connection is made entirely within localhost. This t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe re debugging socket connection issues, or re trying to connect to a software and you are unsure if the issue is the software or the network, or re working on firewall...Another tool to add to your debugging toolbox!
