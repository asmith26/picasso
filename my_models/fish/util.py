from operator import itemgetter
from PIL import Image

from keras.applications.imagenet_utils import preprocess_input
import numpy as np

VGG16_DIM = (224, 224, 3)


def preprocess(targets):
    """Turn images into computation inputs

    Converts an iterable of PIL Images into a suitably-sized numpy array which
    can be used as an input to the evaluation portion of the Keras/tensorflow
    graph.

    Args:
        targets (list of Images): a list of PIL Image objects

    Returns:
        array (float32)

    """
    image_arrays = []
    for target in targets:
        im = target.resize(VGG16_DIM[:2], Image.ANTIALIAS)
        im = im.convert('RGB')
        arr = np.array(im).astype('float32')
        image_arrays.append(arr)

    all_targets = np.array(image_arrays)
    return preprocess_input(all_targets)


def postprocess(output_arr):
    """Reshape arrays to original image dimensions

    Typically used for outputs or computations on intermediate layers which
    make sense to represent as an image in the original dimension of the input
    images (see ``SaliencyMaps``).

    Args:
        output_arr (array of float32): Array of leading dimension n containing
            n arrays to be reshaped

    Returns:
        reshaped array

    """
    images = []
    for row in output_arr:
        im_array = row.reshape(VGG16_DIM[:2])
        images.append(im_array)

    return images


def prob_decode(probability_array, top=5):
    """Provide class information from output probabilities

    Gives the visualization additional context for the computed class
    probabilities.

    Args:
        probability_array (array): class probabilities
        top (int): number of class entries to return. Useful for limiting
            output in models with many classes. Defaults to 5.

    Returns:
        result list of  dict in the format [{'index': class_index, 'name':
            class_name, 'prob': class_probability}, ...]

    """
    class_names = ['ALB',
                  'BET',
                  'DOL',
                  'LAG',
                  'NoF',
                  'OTHER',
                  'SHARK',
                  'YFT']
    results = []
    for row in probability_array:
        entries = []
        for i, prob in enumerate(row):
            entries.append({'index': i,
                            'name': class_names[i],
                            'prob': prob})

        entries = sorted(entries,
                         key=itemgetter('prob'),
                         reverse=True)[:top]

        for entry in entries:
            entry['prob'] = '{:.3f}'.format(entry['prob'])
        results.append(entries)

    return results
