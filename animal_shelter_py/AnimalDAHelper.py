#!/usr/bin/env python2
# coding: utf-8
import sys
import os
from DataAccess import DataAccess


class AnimalDAHelper:
    __singleInstance = None
    DA_INSTANCE = None
    debug_level = 1

    def __new__(clz):
        if not AnimalDAHelper.__singleInstance:
            AnimalDAHelper.__singleInstance = object.__new__(clz)
        return AnimalDAHelper.__singleInstance

    def __init__(self):
        self.DA_INSTANCE = DataAccess()

    def InsertAnimal(self, animal):
        self.debug('Insert animal:')
        animal_id = 0
        insert = ''
        try:
            insert = "INSERT INTO `animal`(`animal_id`, `animal_subid`, `animal_area_pkid`, `animal_shelter_pkid`, `animal_place`, `animal_kind`, `animal_sex`, `animal_bodytype`, `animal_colour`, `animal_age`, `animal_sterilization`, `animal_bacterin`, `animal_foundplace`, `animal_title`, `animal_status`, `animal_remark`, `animal_caption`, `animal_opendate`, `animal_closeddate`, `animal_update`, `animal_createtime`, `shelter_name`, `album_update`) VALUES (\'" + animal["animal_id"] + "\', \'" + animal["animal_subid"] + "\', \'" + animal["animal_area_pkid"] + "\', \'" + animal["animal_shelter_pkid"] + "\', \'" + animal["animal_place"] + "\', \'" + animal["animal_kind"] + "\', \'" + animal["animal_sex"] + "\', \'" + animal["animal_bodytype"] + "\', \'" + animal["animal_colour"] + "\', \'" + animal["animal_age"] + "\', \'" + animal["animal_sterilization"] + "\', \'" + animal["animal_bacterin"] + "\', \'" + animal["animal_foundplace"] + "\', \'" + animal["animal_title"] + "\', \'" + animal["animal_status"] + "\', \'" + animal["animal_remark"] + "\', \'" + animal["animal_caption"] + "\', \'" + animal["animal_opendate"] + "\', \'" + animal["animal_closeddate"] + "\', \'" + animal["animal_update"] + "\', \'" + animal["animal_createtime"] + "\', \'" + animal["shelter_name"] + "\', \'" + animal["album_update"] + "\')"
            insert = insert.replace('<','')
            insert = insert.replace('>','')

            animal_id = self.DA_INSTANCE.InsertRow(insert)
        except:
            print("InsertAnimal: Unexpected error:", sys.exc_info(), sys.exc_traceback.tb_lineno)
        self.debug('Select animal_id: ', animal_id)
        return animal_id

    def CheckAnimalIsExisted(self, animal_id):
        select = "SELECT animal_id FROM animal WHERE animal_id = %s LIMIT 1"
        res = self.DA_INSTANCE.SelectRow(select, animal_id)
        if len(res) < 1:
            return False
        else:
            return res[0][0]

    def debug(self, *print_me):
        if self.debug_level > 0:
            print print_me
