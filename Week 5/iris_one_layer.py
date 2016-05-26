import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# Translate a list of labels into an array of 0's and one 1.
# i.e.: 4 -> [0,0,0,0,1,0,0,0,0,0]
def one_hot(x, n):
    if type(x) == list:
        x = np.array(x)
    x = x.flatten()
    o_h = np.zeros((len(x), n))
    o_h[np.arange(len(x)), x] = 1
    return o_h


data = np.genfromtxt('iris.data', delimiter=",")
np.random.shuffle(data)
x_data = data[:, 0:4].astype('f4')
y_data = one_hot(data[:, 4].astype(int), 3)

print y_data

print "\nSome samples..."
for i in range(20):
    print x_data[i], " -> ", y_data[i]
print

# Tensor para almacenar en forma de vector con las 4 variables de entrada y None (tamanyo el necesario)
x = tf.placeholder("float", [None, 4])

# Tensor para almacenar en forma de vector con las 3 variables de salida y None (tamanyo el necesario)
y_ = tf.placeholder("float", [None, 3])


W1 = tf.Variable(np.float32(np.random.rand(4, 3)) * 0.1)
b1 = tf.Variable(np.float32(np.random.rand(3)) * 0.1) # B se usa para el sesgo de incertidumbre.

W2 = tf.Variable(np.float32(np.random.rand(3, 3)) * 0.1)
b2 = tf.Variable(np.float32(np.random.rand(3)) * 0.1)

layer = tf.sigmoid(tf.matmul(x, W1) + b1)
y = tf.nn.softmax(tf.matmul(layer, W2)+b2)
# Le pasamos a sigmoid la multiplicacion de x por peso (W) mas el sesgo de incertidumbre.
# La funcion Sigmoid lo convierte o en 0 en 1
# La funcion softmax crea un vector solamente uno de sus valores es 1 y los demas 0.

# cross_entropy = tf.reduce_sum(tf.square(y_ - y))        #Error de entropia cruzada. El minimo se consigue cuando las 2 son parecidas.
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))  # Esta es la formula

# Cambia los valores de W un poco en cada iteracion para reducir la funcion de error,
# minimizando el cross_entropy.

train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

print "----------------------"
print "   Start training...  "
print "----------------------"

batch_size = 20
errores = []

# Se ejecuta el codigo mil veces

for step in xrange(1000):

    # Con lotes de tamanyo xdata partido por veinte
    for jj in xrange(len(x_data) / batch_size):
        batch_xs = x_data[jj * batch_size: jj * batch_size + batch_size]
        batch_ys = y_data[jj * batch_size: jj * batch_size + batch_size]

        # Se ejecuta train, indicando que los datos leidos alimenten a los placeholders
        sess.run(train, feed_dict={x: batch_xs, y_: batch_ys})
        if step % 50 == 0:
            precision = sess.run(cross_entropy, feed_dict={x: batch_xs, y_: batch_ys})
            errores.append(precision)
            print "Iteration #:", step, "Error: ", sess.run(cross_entropy, feed_dict={x: batch_xs, y_: batch_ys})
            result = sess.run(y, feed_dict={x: batch_xs})
            for b, r in zip(batch_ys, result):
                print b, "-->", r
            print "----------------------------------------------------------------------------------"

plt.plot(errores)
plt.show()