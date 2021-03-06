import cv2, glob, sys, os, imghdr, datetime, time, json

def main(srcdir, destdir, cascade_path):

  winname = 'searching..'
  cv2.namedWindow(winname, cv2.WINDOW_AUTOSIZE)

  if not os.path.exists(destdir):
    os.mkdir(destdir)

  lastsaved = datetime.datetime.now()
  prefix = lastsaved.strftime('%Y%m%d-%H%M%S_')
  counter = 0
  cascade = cv2.CascadeClassifier(cascade_path)

  for filename in glob.glob(srcdir + "/*"):

    if os.path.isdir(filename):
      continue
    if imghdr.what(filename) == None:
      continue

    print("load " + filename)
    img = cv2.imread(filename)
    frect = cascade.detectMultiScale(img, minSize=(64, 64))
    pos = []
    for r in frect:
      face = img[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
      filename = destdir + "/" + prefix + str(counter) + ".jpg"
      cv2.imwrite(filename, face)
      print("save " + filename)
      counter += 1
      pos.append(r)
    for p in pos:
      cv2.rectangle(img, (p[0],p[1]),(p[0]+p[2],p[1]+p[3]),(0,0,255), 8)
    if len(pos) > 0:
      cv2.imshow(winname, img)
      cv2.waitKey(1)

  cv2.destroyWindow(winname)

if __name__ == '__main__':
  f = open(sys.argv[1])
  conf = json.load(f)
  f.close()
  main(conf['captured images directory'],
       conf['face images directory'],
       conf['cascade file'])

