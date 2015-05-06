#!/usr/bin/env python2
# coding: utf-8
import StringIO
import pycurl
import urllib2
import re
import sys
import json
from DataAccess import DataAccess


def FetchWebPage(url, Proxy=None):
    crl = pycurl.Curl()
    crl.setopt(pycurl.VERBOSE, 0)
    crl.setopt(pycurl.FOLLOWLOCATION, 1)
    crl.setopt(pycurl.MAXREDIRS, 5)
    crl.setopt(pycurl.CONNECTTIMEOUT, 30)
    crl.setopt(pycurl.TIMEOUT, 30)

    crl.setopt(pycurl.REFERER, 'http://www.google.com/search')
    if Proxy != None:
        crl.setopt(pycurl.PROXY, Proxy)
    crl.fp = StringIO.StringIO()
    crl.setopt(pycurl.URL, url)
    crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
    try:
        i = str(crl.perform())
        data = crl.fp.getvalue()
    except Exception, e:
        try:
            #print Proxy, '\t', str(e), '\t', url
            i = str(crl.perform())
            data = crl.fp.getvalue()
        except:
            data = ''
    return data
