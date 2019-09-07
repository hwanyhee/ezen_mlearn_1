import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


rng = np.random
#parameter
learning_rate = 0.01
training_epochs = 1000
display_step =50
#Training Data
train_X = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                        7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                        2.827,3.465,1.65,2.904,2.42,2.94,1.3])

print( train_X.shape)
n_samples = train_X.shape[0]
#tf graph input

X = tf.placeholder("float")
Y = tf.placeholder("float")
# Set model weight
W = tf.Variable(rng.randn() ,name='weight')
b = tf.Variable(rng.randn(),name='bias')
#construct a linear model
pred = tf.add(tf.multiply(X,W),b) # Y = WX +b
#mean squared error

cost = tf.reduce_mean(tf.pow(pred-Y,2)) /(2*n_samples)

#gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)
init = tf.global_variables_initializer()
#start training
with tf.Session() as sess:
    sess.run(init)
    # fit all traing data
    for epoch in range(training_epochs):
        for (x,y) in zip(train_X,train_Y):
            sess.run((optimizer,{X:x,Y:y}))

        #display logs per epoch step
        if (epoch+1) % display_step:
            c = sess.run(cost,{X:train_X,Y:train_Y})
            print("epoch:",'%0.4d' % (epoch+1),"cost=","{:.9f}".format(c),"W=",sess.run(W),"b=",sess.run(b))

    print("optimization finished")
    training_cost = sess.run(cost,{X:train_X,Y:train_Y})
    print("training cost=","{:.9f}".format(c),"W=",sess.run(W),"b=",sess.run(b))

    #graphic display
    plt.plot(train_X,train_Y,'ro',label='original data')
    plt.plot(train_X,sess.run(W) * train_Y+sess.run(b),label='fitted line')
