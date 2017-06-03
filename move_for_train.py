import os, sys, glob, shutil, json

def main(srcdir):
  for label in range(2):
    for subdir in ["/test", "/train"]:
      if not os.path.exists(srcdir + subdir):
        os.mkdir(srcdir + subdir)
      if not os.path.exists(srcdir + subdir + "/" + str(label)):
        os.mkdir(srcdir + subdir + "/" + str(label))
    counter = 0
    target_dir = srcdir + "/" + str(label) + "/*.jpg"
    print("check " + target_dir)
    for filename in glob.glob(target_dir):
      counter += 1
      if counter == 5:
        counter = 0
        shutil.move(filename, srcdir + "/test/" + str(label) + "/")
      else:
        shutil.move(filename, srcdir + "/train/" + str(label) + "/")

if __name__ == '__main__':
  f = open(sys.argv[1])
  conf = json.load(f)
  f.close()
  main(conf['face images directory'])
  
