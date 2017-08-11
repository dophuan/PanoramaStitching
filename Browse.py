import os
import argparse
from stich import *
from Sticher import *

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True, help ="Path to query")
args = vars(ap.parse_args())


def LoadFileinDialog(path):
    list=[]
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            #print(os.path.join(path, file))
            list.append(os.path.join(path, file))
        if file.endswith(".JPG"):
            #print(os.path.join(path, file))
            list.append(os.path.join(path, file))
    return list

list = []
path = args["query"]
list = LoadFileinDialog(path)

stich(list)