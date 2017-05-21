import glob
import cv2
import os
import sys
import imghdr
from datetime import datetime

def move(src, targetdir, filename):
  print("move " + src + " to " + targetdir + filename)
  if not os.path.isdir(targetdir):
    os.mkdir(targetdir)
  os.rename(src, targetdir + filename)

def main(srcdir):
  name = "main"
  cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)
  counter = 0
  prefix = datetime.now().strftime('%Y%m%d-%H%M%S_')
  for filename in glob.glob(srcdir + '/*'):
    if os.path.isdir(filename):
      continue
    if imghdr.what(filename) == None:
      continue
    print(filename)
    img = cv2.imread(filename)
    cv2.imshow(name, img)
    key = cv2.waitKey(0)
    if key == ord('q'):
      break
    if key == ord('0'):
      move(filename, srcdir + "/0/", prefix + str(counter) + ".jpg")
      counter += 1
    elif key == ord('1'):
      move(filename, srcdir + "/1/", prefix + str(counter) + ".jpg")
      counter += 1
    else:
      print("skip " + filename)
  cv2.destroyWindow(name)

if __name__ == '__main__':
  main(sys.argv[1])
