# Day 3 — Computer Vision Preprocessing with OpenCV

## Learning Objectives

- Understand why images must be standardized before they are provided to a computer-vision model.

- Read and inspect image files using OpenCV.

- Resize images to a fixed input size and convert color channels from BGR to RGB.

- Normalize pixel values when using a general image-processing pipeline.

- Build an image-augmentation pipeline for training data.

- Apply Canny edge detection as an example of classical computer-vision preprocessing.

- Match the preprocessing pipeline to the expectations of a pretrained transfer-learning model such as ResNet50.

- Separate training, validation, and test preprocessing so that random augmentation is applied only to the training data.

## Key Topics

- OpenCV image loading
- Image resizing
- BGR and RGB color ordering
- Pixel normalization
- Data augmentation
- Training, validation, and test separation
- Canny edge detection
- Transfer learning
- ResNet50-specific preprocessing
- ImageDataGenerator
- Preprocessing verification

## Dataset

The notebook uses the **Melanoma Skin Cancer Dataset — Benign vs Malignant**. The dataset contains two image classes: `Benign` and `Malignant`, organized into separate `train/` and `test/` directories.

The notebook detected the following image counts:

| Dataset Split | Number of Images | Classes |
|---|---:|---:|
| Training subset | 9,504 | 2 |
| Validation subset | 2,375 | 2 |
| Test set | 2,000 | 2 |

## Hands-On Lab (Tasks)
- Step 1: Build an OpenCV preprocessing function: read, resize to a fixed size, convert to RGB, normalize.
- Step 2: Create an augmentation pipeline and visualize several augmented versions of one image.
- Step 3: If the project is image-based, apply the correct preprocess_input for the chosen pre-trained model.
- Step 4: Open a pull request with the integrated notebook for the mid-sprint Mentor Code & Notebook
Review and address the feedback.

## Tools Used

- OpenCV
- TensorFlow/Keras
- ImageDataGenerator
- ResNet50 preprocessing
- Matplotlib
- NumPy
- KaggleHub
- Google Colab
- Git / GitHub
## Results

### OpenCV Preprocessing

| Check | Result |
|---|---|
| Sample image shape | `224 × 224 × 3` |
| Resized image shape | `224 × 224 × 3` |
| General normalized data type | `float32` |
| General normalized pixel range | Approximately `0–1` |
| Color conversion | BGR → RGB |

### Augmentation Pipeline

| Augmentation Component | Configuration |
|---|---:|
| Rotation range | `20°` |
| Zoom range | `0.15` |
| Horizontal flip | Enabled |
| Brightness range | `[0.8, 1.2]` |
| Generated examples for visualization | `6` |

### ResNet50 Training Pipeline

| Pipeline | Random Augmentation | ResNet50 Preprocessing | Shuffle |
|---|---|---|---|
| Training | Yes | Yes | Yes |
| Validation | No | Yes | No |
| Test | No | Yes | No |

The ResNet50-preprocessed batch produced tensors with the expected shape and data type:

| Metric | Result |
|---|---|
| Batch image shape | `(32, 224, 224, 3)` |
| Batch label shape | `(32,)` |
| Data type | `float32` |
| Example pixel range | Approximately `-123.68` to `151.06` |
| Number of classes | `2` |

The values are not restricted to `0–1` after ResNet50 preprocessing. This is expected because ResNet50 preprocessing follows the ImageNet convention rather than simple division by `255.0`.

## Learning Outcomes

- At the end of the day, I was able to explain why images require consistent dimensions, channel ordering, and numerical ranges before model training.

- I was able to read images with OpenCV, resize them, convert BGR images to RGB, and create a reusable preprocessing function.

- I was able to distinguish between general `0–1` normalization and model-specific preprocessing for ResNet50.

- I was able to create and visualize an augmentation pipeline while keeping random augmentation limited to the training data.

- I was able to prepare separate training, validation, and test pipelines with consistent ResNet50 preprocessing.

- I was able to apply Canny edge detection and understand its role as a classical computer-vision example rather than a required CNN preprocessing step.

- The final preprocessing choice for the transfer-learning pipeline is **ResNet50-specific preprocessing**, because it matches the expectations of the selected pretrained backbone. General `0–1` normalization remains documented as a fundamental OpenCV preprocessing example.



