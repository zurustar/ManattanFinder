FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y

RUN apt-get install build-essential cmake git libgtk2.0-dev pkg-config python-dev -y

RUN apt-get install firefox -y

RUN apt-get install libopencv-dev -y

RUN apt-get install ffmpeg libopencv-dev libgtk-3-dev python-numpy python3-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libv4l-dev libtbb-dev qtbase5-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils unzip -y

RUN apt-get install wget -y

RUN wget https://github.com/Itseez/opencv/archive/3.1.0.zip && unzip 3.1.0.zip
RUN cd opencv* && mkdir build && cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON .. && make && make install

RUN /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
RUN ldconfig

RUN pip3 install --upgrade pip
RUN pip3 install selenium
RUN pip3 install pillow

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && tar zxvf geckodriver*.tar.gz && mv geckodriver /usr/local/bin/

#
#  docker run -v $PWD:/mnt -i -t IMAGE /bin/bash
#  cd /mnt
#  python3 ./dl.py
#

