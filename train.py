import glob
import numpy as np
import tensorflow.contrib.keras as keras
from keras.models import Sequential
from keras.utils import to_categorical, plot_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img, img_to_array
from keras.layers import Input, Flatten, Dense, Conv2D, Dropout
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint

def draw_graph(res):
  import matplotlib
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  plt.figure()
  for k in ['loss', 'val_loss', 'acc', 'val_acc']:
    plt.plot(np.arange(len(res.history[k])), res.history[k], label=k)
  plt.ylim(0.0, 1.0)
  plt.legend()
  plt.grid()
  plt.savefig('./graph.png')
  plt.close('all')

def main():
  width = 32
  height = 32
  input_shape=(width, height, 1)

  model = Sequential()
  model.add(Conv2D(32, (3, 3), input_shape=input_shape, activation='relu'))
  model.add(MaxPooling2D(2, strides=2))
  model.add(Dropout(0.5))

  model.add(Conv2D(64, (3, 3), activation='relu'))
  model.add(MaxPooling2D(2, strides=2))
  model.add(Dropout(0.5))

  model.add(Conv2D(128, (3, 3), activation='relu'))
  model.add(MaxPooling2D(2, strides=2))
  model.add(Dropout(0.5))

  model.add(Flatten())
  model.add(Dense(512, activation="relu"))
  model.add(Dense(2, activation="softmax"))

  adm = Adam()
  model.compile(loss="categorical_crossentropy",
                optimizer=adm,  metrics=['accuracy'])
  model.summary()
  plot_model(
    model, to_file="model.png", show_shapes=True, show_layer_names=True)

  idg = ImageDataGenerator(rotation_range=30., zoom_range=0.1, rescale=1./255)
  train_gen = idg.flow_from_directory(
    'imgs/train', color_mode='grayscale', target_size=(width, height))
  test_gen = idg.flow_from_directory(
    'imgs/test', color_mode='grayscale', target_size=(width, height))
  mc = ModelCheckpoint(
    "./weights.{epoch:02d}-{val_loss:.2f}.hdf5", save_best_only=True)

  res = model.fit_generator(
    train_gen, steps_per_epoch=200, epochs=2000,
    validation_data=test_gen, validation_steps=20, callbacks=[mc])

  fp = open('./model.json', 'w')
  fp.write(model.to_json())
  fp.close()
  draw_graph(res)

if __name__ == '__main__':
  main()
