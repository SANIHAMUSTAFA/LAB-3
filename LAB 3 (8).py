from rasterio.plot import show
import rasterio
from numpy import expand_dims
from keras.preprocessing.image import ImageDataGenerator

# Open the raster file using rasterio
DATA1 = rasterio.open(r"E:\Saniha\DIP\Alaska\HH-ALPSRP268500490-H2.2_UA.tif")

# Read the image data and convert it to a NumPy array
data = DATA1.read()
data = data.transpose(1, 2, 0)  # Transpose to (height, width, channels)

# Data augmentation
samples = expand_dims(data, 0)
data_generator = ImageDataGenerator(width_shift_range=0.5)
it = data_generator.flow(samples, batch_size=1)

# Display augmented images
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(330 + 1 + i)
    batch = it.next()
    result = batch[0].astype('uint16')
    plt.imshow(result)

plt.show()
plt.title("Vertical shiff of HHQ")