import logging
import os

from lightwood.encoders.image.helpers.nn import NnEncoderHelper
import torch

class NnAutoEncoder:

    def __init__(self, images, is_target = False):
        self._model = NnEncoderHelper(images)
        self._pytorch_wrapper = torch.FloatTensor

    def encode(self, images):
        """
          Encode all the images from the list of paths(to images)

        :param images: List of images paths
        :return: a torch.floatTensor
        """
        if not self._model:
            logging.error("No model to encode, please train the model")

        return self._model.encode(images)

    def decode(self, encoded_values_tensor, save_to_path="decoded/"):
        """
         Decoded the encoded list of image tensors and write the decoded images to give path

        :param encoded_values_tensor: List of encoded images tensors
        :param save_to_path: Path to store decoded images
        :return: a list of image paths
        """
        if not self._model:
            logging.error("No model to decode, please train the model")

        if not os.path.exists(save_to_path):
            os.makedirs(save_to_path)
        return self._model.decode(encoded_values_tensor, save_to_path)

    def train(self, images):
        """
        :param images: List of images paths
        """
        self._model = NnEncoderHelper(images)


# only run the test if this file is called from debugger
if __name__ == "__main__":
    images = ['test_data/cat.jpg', 'test_data/cat2.jpg', 'test_data/catdog.jpg']
    encoder = NnAutoEncoder(images)

    images = ['test_data/cat.jpg', 'test_data/cat2.jpg']
    encoded_data = encoder.encode(images)
    print(encoded_data)

    # decoded images will be stored under decoded folder
    decoded_data = encoder.decode(encoded_data, "decoded/images")
    print(decoded_data)
