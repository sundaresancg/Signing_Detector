# Signing_Detector
A Deep Learning model to detect whether an individual is signing with his hands or not (being idle), created with the motive to aid speech impaired people. 
A model that can interpret sign language would be an invaluable asset for people with speech impairment. This detector is the first step in that process. 

Dataset:
- Videos of 30 individuals signing and not signing
- The videos were separated into frames
- Absdiff images (Difference between N th frame and (N+1)th frame) of the corresponding frames were generated
- All the absdiff images are combined to create the dataset for the model (30000 absdiff images for signing and 30000 absdiff images for not signing)

Model:
- Dimensions of input images = 256 x 256
- Convolutional Neural Network : Alexnet Architecture
- Highest validation accuracy obtained = 81 %
- Accuracy obtained for the testing data = 95 %

SignClf_preprocessing: 
- Consists of frame generation from a video.
- Augmentation, Resizing of images, Conversion of images to Black and White.
- Generation od Absdiff images.

SignClf_modelling: 
- CNN Model Architecture, Building, Compilation, Testing.
- A snippet to classify based on the number of white(light) pixels present in the absdiff images.

SignClf_app:
- Launching the model as an application that runs on a web browser.
- Accesses the camera and detects if the user is signing or not.


