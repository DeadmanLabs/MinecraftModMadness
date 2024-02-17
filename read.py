import os, time, json
from datetime import datetime


batch_one = "1.7.10-1.12.2\\javadoc\\forge"
batch_two = "1.12.2-1.19.3\\javadoc"
batch_three = "1.19.4-1.20.4"

def buildRepository(basePath):
    return

subdirectories = []
subdirectories += [os.path.join(batch_one, name) for name in os.listdir(batch_one) if os.path.isdir(os.path.join(batch_one, name))]
subdirectories += [os.path.join(batch_one, name) for name in os.listdir(batch_two) if os.path.isdir(os.path.join(batch_two, name))]
subdirectories += [os.path.join(batch_one, name) for name in os.listdir(batch_three) if os.path.isdir(os.path.join(batch_three, name))]
for forgeVersion in subdirectories:
    print("Processing " + forgeVersion.split('\\')[-1] +  " Version...")
    buildRepository(forgeVersion)
    print("Done!")
