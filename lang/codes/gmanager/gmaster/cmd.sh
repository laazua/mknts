#!/bin/bash

cd app 
pdm run celery -A tasks worker --pool threads -D 
python main.py
