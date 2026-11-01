import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, confusion_matrix

digits = load_digits()

print("Dataset Loaded Successfully")
print()
print("Number of Images:", len(digits.images))
print("Feature Shape:", digits.data.shape)
print("Target shape:", digits.target.shape)
print("\nClasses:")

plt.figure(figsize=(10, 5))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(digits.images[i], cmap='gray')
    plt.title(f'True Label: {digits.target[i]}')
    plt.axis('off')

plt.suptitle("The Digit Sample Images")
plt.show()

x = digits.data
y = digits.target

print("\nFeature Shape:", x.shape)
print("Target Shape:", y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=41)
print("\nTraining Set Shape:", len(x_train))
print("Testing Set Shape:", len(x_test))

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)
print("\nModel Training Completed!")
predictions = model.predict(x_test)

print("\nFirst 20 predictions:", predictions[:20])

for i in range(20):
    print(
        f"actual: {y_test[i]}",
        f"predicted: {predictions[i]}"
    )
    
accuracy = accuracy_score(y_test, predictions) 
print()
print("=" * 10)
print("MODEL ACCURACY")
print("=" * 10)
print(f"Accuracy: {accuracy*100:.2f}%")

cm = confusion_matrix(y_test, predictions)
print()
print("=" * 20)
print("CONFUSION MATRIX")
print("=" * 20)
print(cm)

report = classification_report(y_test, predictions)
print()
print("=" * 30)
print("CLASSIFICATION REPORT")
print("=" * 30)
print(report)

plt.figure(figsize=(6, 12))

for i in range(10):
    plt.subplot(4, 3, i + 1)
    plt.imshow(x_test[i].reshape(8, 8), cmap='gray')
    plt.title(f"p: {predictions[i]}")
    plt.axis('off')
    
plt.suptitle("Model Predictions")
plt.show()

print()
print("=" * 50)
print("INCORRECT PREDICTIONS")
print("=" * 50)

count = 0

for i in range(len(y_test)):
    if y_test[i] != predictions[i]:
        print(
            f"Actual: {y_test[i]}",
            f"Predicted: {predictions[i]}"
        )
        count += 1

print(
    "\nTotal Errors:",
    count
)

sample_index = 20
sample = x_test[sample_index].reshape(1, -1)
prediction = model.predict(sample)



print()
print("=" * 50)
print("CUSTOM SAMPLE PREDICTION")
print("=" * 50)

print(
    "Actual Digit:",
    y_test[sample_index]
)

print(
    "Predicted Digit:",
    prediction[0]
)

plt.imshow(
    sample.reshape(8, 8),
    cmap="gray"
)

plt.title(
    f"Prediction = {prediction[0]}"
)

plt.axis("off")

plt.show()

probabilities = model.predict_proba(sample)

print()
print("=" * 50)
print("PREDICTION PROBABILITIES")
print("=" * 50)
for digit, prob in enumerate(probabilities[0]):
    print(f"Digit {digit}: {prob:.6f}")