#!/usr/bin/env python2
# coding: utf-8
import MySQLdb
import MySQLdb.cursors
import db_set
import sys
import os
from DBUtils.PooledDB import PooledDB


class DataAccess:
    __singleInstance = None
    pool = None
    pool_size = 10
    debug_level = 0

    def __new__(clz):
        if not DataAccess.__singleInstance:
            DataAccess.__singleInstance = object.__new__(clz)
        return DataAccess.__singleInstance

    def __init__(self):
        # mysql
        self.pool = PooledDB(MySQLdb, self.pool_size, db=db_set.db_dbname
            , user=db_set.db_user, passwd=db_set.db_pwd, host=db_set.db_ip, charset="utf8")

    def InsertRow(self, insertStr):
        conn = self.pool.connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SET NAMES utf8')
            cursor.execute(insertStr)
            conn.commit()
            return cursor.lastrowid
        except:
            print("InsertRow: Unexpected error:"
                , sys.exc_info(), sys.exc_traceback.tb_lineno)
            return 0
        finally:
            if conn:
                conn.close()

    def SelectRow(self, selectStr, where = None):
        conn = self.pool.connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SET NAMES utf8')
            if where is not None:
                cursor.execute(selectStr, where)
            else:
                cursor.execute(selectStr)
            res = cursor.fetchall()
            return res
        except:
            print("SelectRow: Unexpected error:"
                , sys.exc_info(), sys.exc_traceback.tb_lineno)
        finally:
            if conn:
                conn.close()

    def debug(self, *print_me):
        if self.debug_level > 0:
            print print_me
