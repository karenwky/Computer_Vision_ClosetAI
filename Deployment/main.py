from flask import Flask, render_template, request
import os
import sys
import skimage
import numpy as np
from PIL import Image, ImageDraw

# Set the ROOT_DIR variable to the root directory of the Mask_RCNN git repo
ROOT_DIR = '/Users/Home/Mask_RCNN'
assert os.path.exists(ROOT_DIR), 'ROOT_DIR does not exist. Did you forget to read the instructions above? ;)'

# Import mrcnn libraries
sys.path.append(ROOT_DIR) 
from mrcnn.config import Config
import mrcnn.utils as utils
import mrcnn.model as modellib
from visualize import display_instances

app = Flask(__name__)

class InferenceConfig(Config):

    # Give the configuration a recognizable name
    NAME = "deployment"

    # Train on 1 GPU and 1 image per GPU. Batch size is 1 (GPUs * images/GPU).
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    NUM_CLASSES = 1 + 13  # background + no. of classes

    IMAGE_MIN_DIM = 192
    IMAGE_MAX_DIM = 832
    DETECTION_MIN_CONFIDENCE = 0.7

    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128)
    TRAIN_ROIS_PER_IMAGE = 32
    MAX_GT_INSTANCES = 50 
    POST_NMS_ROIS_INFERENCE = 500 
    POST_NMS_ROIS_TRAINING = 1000
    
inference_config = InferenceConfig()

# Root directory of the project
ROOT_DIR = os.getcwd()
# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=inference_config)
model.load_weights('/Users/Home/Mask_RCNN/mask_rcnn_v3_from24_0016.h5', by_name=True)
model.keras_model._make_predict_function()

class_names = ['BG',
 'short_sleeved_shirt',
 'long_sleeved_shirt',
 'short_sleeved_outwear',
 'long_sleeved_outwear',
 'vest',
 'sling',
 'shorts',
 'trousers',
 'skirt',
 'short_sleeved_dress',
 'long_sleeved_dress',
 'vest_dress',
 'sling_dress']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result', methods=['POST'])
def result():
    prediction = ''
    if request.method == 'POST':
        file = request.files['file']
        img = skimage.io.imread(file)
        img_arr = np.array(img)
        results = model.detect([img_arr])
        r = results[0]
        graph1_url = display_instances(img, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
        return render_template("result.html", graph1=graph1_url)

if __name__ == "__main__":
    app.run()