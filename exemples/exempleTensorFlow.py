import tensorflow as tf
from tensorflow import keras

# recuperation et desagregation du jeu de donnees
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# normalisation des donnees
train_images = train_images / 255
test_images = test_images / 255

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28.28)),   # Flatten the 28x28 input images
    keras.layers.Dense(128, activation='relu'),  # Hidden layer with ReLU activation
    keras.layers.Dense(10, activation='softmax')  # Output layer with softmax activation for classification
])

# Compile the model by specifying the loss function, optimizer, and metrics
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Loss function for classification
    metrics=['accuracy'] # monitor accuracy during training
)

model.fit(train_images, train_labels, epochs=10)

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)

predictions = model.predict(test_images)