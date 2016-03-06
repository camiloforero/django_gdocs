#encoding:utf-8
"""
Module containing functions related to interactions with google documents
"""
from __future__ import unicode_literals
from oauth2client.service_account import ServiceAccountCredentials

import gspread

class GdocsApi(object):
    def __init__(self, keyfile_path):
        scope = ['https://spreadsheets.google.com/feeds']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scope)
        self.gc = gspread.authorize(self.credentials)
