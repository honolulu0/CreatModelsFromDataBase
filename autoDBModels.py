# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Generate models from database
Created date: 2021.1.22
Author: lee
"""

import os


def gen_models():
    db_url = "mysql://root:123456@10.245.29.91:3306/xpit"
    #plants_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    plants_path = os.getcwd()
    print(plants_path)
    model_path = os.path.join(plants_path, 'models','models.py')
    cmd = 'flask-sqlacodegen --flask {}'.format(db_url)
    try:
        output = os.popen(cmd)
        content = str(output.read())
        with open(model_path, 'w+') as f:
            f.write(content)
        print('Generated database models successfully')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    gen_models()