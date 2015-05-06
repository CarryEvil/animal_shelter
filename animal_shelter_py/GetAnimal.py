#!/usr/bin/env python2
# coding: utf-8
import StringIO
import pycurl
import urllib2
import re
import sys
import json
import WebFetcher
import os
import time
from AnimalDAHelper import AnimalDAHelper


def HandleAnimal(json_data):
    data = json.loads(json_data)
    temp = {}
    for animal in data:
        try:
            if ANIMAL_DA_HELPER.CheckAnimalIsExisted(animal['animal_id']) == False:
                for key in animal.keys():
                    temp[key] = animal[key].replace('\'', '')
                animal_id = ANIMAL_DA_HELPER.InsertAnimal(temp)
                print 'Insert animal: ', animal['animal_id']
            else:
                print 'Animal is existed: ', animal['animal_id']
        except:
            print("HandleAnimal: Unexpected error:"
                , sys.exc_info()[0], sys.exc_traceback.tb_lineno)

ANIMAL_DA_HELPER = AnimalDAHelper()

