# -*- coding: utf-8 -*-
"""
Created on Fri May 26 01:27:33 2023

@author: Sanket
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
