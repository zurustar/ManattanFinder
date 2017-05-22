import os
import sys
import glob
import shutil

def main(srcdir = "./imgs/"):
  for label in range(2):
    for subdir in ["test", "train"]:
      if not os.path.exists(srcdir + subdir):
        os.mkdir(srcdir + subdir)
      if not os.path.exists(srcdir + subdir + "/" + str(label)):
        os.mkdir(srcdir + subdir + "/" + str(label))
    counter = 0
    for filename in glob.glob(srcdir + str(label) + "/*.jpg"):
      counter += 1
      if counter == 5:
        counter = 0
        shutil.move(filename, srcdir + "/test/" + str(label) + "/")
      else:
        shutil.move(filename, srcdir + "/train/" + str(label) + "/")

if __name__ == '__main__':
  main(sys.argv[1])
  
