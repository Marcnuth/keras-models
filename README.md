# Keras Models Hub

![PyPI - Downloads](https://img.shields.io/pypi/dm/keras-models?label=PyPI)
![PyPI](https://img.shields.io/pypi/v/keras-models?color=%2300a8ff&label=Latest)

This repo aims at providing both **reusable** Keras Models and **pre-trained** models, which could easily integrated into your projects.

## Install

```shell
pip install keras-models
```

If you will using the NLP models, you need run one more command:
```shell
python -m spacy download xx_ent_wiki_sm
```

## Usage Guide

### Import

```
import kearas_models
```


### Examples

__LinearModel__

__DNN__

__CNN__

```python
from keras_models.models import CNN

# fake data
X = np.random.normal(0, 1.0, size=500 * 100 * 100 * 3).reshape(500, 100, 100, 3)
w1 = np.random.normal(0, 1.0, size=100)
w2 = np.random.normal(0, 1.0, size=3)
Y = np.dot(np.dot(np.dot(X, w2), w1), w1) + np.random.randint(1)

# initialize & train model
model = CNN(input_shape=X.shape[1:], filters=[32, 64], kernel_size=(2, 2), pool_size=(3, 3), padding='same', r_dropout=0.25, num_classes=1)
model.compile(optimizer='adam', loss=mean_squared_error, metrics=['mae', 'mse'])
model.summary()

model.fit(X, Y, batch_size=16, epochs=100, validation_split=0.1)
```

__SkipGram__

__WideDeep__

__VGG16_Places365 [pre-trained]__
> This model is forked from [GKalliatakis/Keras-VGG16-places365](https://github.com/GKalliatakis/Keras-VGG16-places365) and [CSAILVision/places365](https://github.com/CSAILVision/places365)

```python
from keras_models.models.pretrained import vgg16_places365
labels = vgg16_places365.predict(['your_image_file_pathname.jpg', 'another.jpg'], n_top=3)

# Example Result: labels = [['cafeteria', 'food_court', 'restaurant_patio'], ['beach', 'sand']]
```


## Models

- LinearModel
- DNN
- WideDeep
- TextCNN
- TextDNN
- SkipGram
- ResNet
- VGG16_Places365 [pre-trained]
- working on more models

## Citation

__WideDeep__

```
Cheng H T, Koc L, Harmsen J, et al. 
Wide & deep learning for recommender systems[C]
Proceedings of the 1st workshop on deep learning for recommender systems. ACM, 2016: 7-10.
```

__TextCNN__

```
Kim Y. 
Convolutional neural networks for sentence classification[J]. 
arXiv preprint arXiv:1408.5882, 2014.
```

__SkipGram__

```
Mikolov T, Chen K, Corrado G, et al. 
Efficient estimation of word representations in vector space[J]. 
arXiv preprint arXiv:1301.3781, 2013.
```


__VGG16_Places365__
```
Zhou, B., Lapedriza, A., Khosla, A., Oliva, A., & Torralba, A.
Places: A 10 million Image Database for Scene Recognition
IEEE Transactions on Pattern Analysis and Machine Intelligence
```

__ResNet__
```
He K, Zhang X, Ren S, et al. 
Deep residual learning for image recognition[C]
Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 770-778.

```

## Contribution

Please submit PR if you want to contribute, or submit issues for new model requirements.

