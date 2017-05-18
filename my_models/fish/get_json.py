import os
import json
from keras.applications.vgg16 import VGG16

path = 'data-volume'
try:
    os.mkdir(path)
except FileExistsError:
    pass

print('Downloading and setting up custom VGG16 (include_top=True, classes=8, weights=None)...')

vgg16 = VGG16(include_top=True, classes=8, weights=None)

print('Saving json to {}/ ...'.format(path))

if not os.path.exists(os.path.join(os.path.dirname(__file__), path)):
    os.makedirs(os.path.join(os.path.dirname(__file__), path))

with open(os.path.join(os.path.dirname(__file__),
                       path,
                       'vgg16.json'), 'w') as json_file:
    json.dump(vgg16.to_json(), json_file)

print('Done.')
