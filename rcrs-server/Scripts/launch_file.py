#!/usr/bin/env python

import subprocess
import time, os 
import signal, sys
import socket
import argparse

	

def launch_everything(building_port, reward_port, agent_port):
	# path_for_start_file = os.path.join(sys.path[0], "start-comprun.sh -bp {} -rp {}".format(building_port,reward_port))
	print('Trial...')
	print(os.getcwd())
	path_for_start_file = f"./rcrs-server/Scripts/start-comprun.sh -m ../../test/map -c ../../test/config -bp {building_port} -rp {reward_port}"
	
	#path_for_launch_file = "./rcrs-adf-sample/launch.sh '-all -p {}'".format(agent_port)
	subprocess.Popen(path_for_start_file, shell=True)
	print(os.getcwd())
	#print(path_for_launch_file)
	#subprocess.Popen(path_for_launch_file, shell=True)
	time.sleep(5000000)	 


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("building_port", help = 'What is the building_port', type= int)
	parser.add_argument("reward_port", help = "What is the reward_port?", type=int)
	parser.add_argument("agent_port", help = "What is the agent_port?", type=int)
	args = parser.parse_args()
	launch_everything(args.building_port, args.reward_port, args.agent_port)

if __name__ == '__main__':
	main()
