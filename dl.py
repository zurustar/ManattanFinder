# encoding: utf-8

from selenium import webdriver
from time import sleep
from PIL import Image
import os
import sys
import cv2

def download(workdir, browser, filename, query):
  # googleで与えられた文字列で検索しスクロールしながら画面キャプチャ
  browser.get('https://www.google.co.jp/search?q=%s&tbm=isch' % query)
  h = browser.execute_script('return document.documentElement.clientHeight')
  pos = 0
  counter = 0
  while True:
    browser.execute_script('window.scrollTo(0, %d);' % pos)
    browser.get_screenshot_as_file('%s/tmp%d.png' % (workdir, counter))
    counter += 1
    pos += h
    if pos > browser.execute_script('return document.body.scrollHeight'):
      break
    sleep(1)
  # キャプチャした画像を一枚に合体
  imgs = []
  total_height, total_width = 0, 0
  for i in range(counter):
    img = Image.open('%s/tmp%d.png' % (workdir, i), 'r')
    if total_width < img.width:
      total_width = img.width
    total_height += img.height
    imgs.append(img)
  result = Image.new('RGB', (total_width, total_height), (255, 255, 255))
  margin = 0
  for img in imgs:
    result.paste(img, (0, margin))
    margin += img.height
  result.save(filename)
  # 一時ファイルを削除
  for i in range(counter):
    os.remove('%s/tmp%d.png' % (workdir, i))

def face(dir, filename):
  os.mkdir('./' + dir)
  path = '/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_alt.xml'
  cascade = cv2.CascadeClassifier(path)
  print(filename)
  img = cv2.imread(filename)
  frect = cascade.detectMultiScale(img, minSize=(32, 32))
  for i, r in enumerate(frect):
    face = img[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
    faceimg = './' + dir + '/' + str(i) + '.png'
    cv2.imwrite(faceimg, face)

def main():
  workdir = './work/'
  if os.path.exists(workdir):
    print("remove " + workdir)
    sys.exit()
  os.mkdir(workdir) 
  dirpath = os.path.dirname(workdir)
  os.environ['MOZ_HEADLESS'] = '1'
  browser = webdriver.Firefox()
  members = ['高山一実', '秋元真夏', '大園桃子', '中田花奈']
  for i, member in enumerate(members):
    print("start #", i)
    filename = './' + str(i) + '.png'
    download(workdir, browser, filename, member)
    face(str(i), filename)
  browser.close()
  os.rmdir(workdir)

if __name__ == '__main__':
  main()

