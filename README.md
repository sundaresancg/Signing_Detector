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
- Accuracy obtained for the testing data + 95 %


