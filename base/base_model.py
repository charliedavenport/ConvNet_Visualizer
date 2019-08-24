# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:31:04 2019


based on the template provided by https://github.com/Ahmkel/Keras-Project-Template
"""

from json import loads

from keras.models import model_from_json

class BaseModel(object):
    def __init__(self):
        #self.config = config
        self.model = None

    # save function that saves the checkpoint in the path defined in the config file
    def save(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Saving model...")
        self.model.save_weights(checkpoint_path)
        print("Model saved")

    # load latest checkpoint from the experiment path defined in the config file
    def load_weights(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Loading model checkpoint {} ...\n".format(checkpoint_path))
        self.model.load_weights(checkpoint_path)
        print("Model loaded")
        
    def build_from_config(self, config_path):
        print("Building model from config {} ....\n".format(config_path))
        with open(config_path, 'r') as f:
            #json_str = loads(f.read())
            self.model = model_from_json(f.read())
            print('Model Summary:')
            print(self.model.summary())
        
    def export_config(self, file_path):
        json_str = self.model.to_json()
        with open(file_path, 'w+') as file:
            file.write(json_str)
        

    def build_model(self):
        raise NotImplementedError