import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
class FashionChecker:
    def __init__(self):
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def create_model(self) ->[]:
        #전처리
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        '''
        plt.figure(figsize=(5, 5))
        image = train_images[100]
        plt.imshow(image)
        plt.colorbar()
        plt.grid(False)
        plt.show()
        '''
        #모델링
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28,28)),
            keras.layers.Dense(128,activation='relu'),
            keras.layers.Dense(10,activation='softmax')

        ])

        model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
        #러닝
        model.fit(train_images,train_labels,epochs=5)

        #test
        test_loss,test_acc = model.evaluate(test_images,test_labels)
        print('테스트 정확도:{}'.format(test_acc))
