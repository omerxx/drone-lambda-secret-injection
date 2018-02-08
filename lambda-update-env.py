#!/bin/python

import os
import boto3

def pp(name):
    # pp as in plugin parameter 
    param = os.environ.get('{}_{}'.format('PLUGIN', name.upper()))
    if param:
        return param
    else:
        print 'No such variable {}'.format(name) if 'key' not in name else ''
        return None


def env_handler(paramString):
    omap = []
    envSets = paramString.split(',')
    for set in envSets:
        value = os.environ.get(set.split('=')[0]) if not set.split('=')[1] and os.environ.get(set.split('=')[0]) else set.split('=')[1]
            
        omap.append(
            {
                'name': set.split('=')[0],
                'value': value
            }
        )

    return omap  


def update_function_configuration():
    response = client.update_function_configuration(
        FunctionName = pp('functionname'),
        Environment={
            'Variables': env_handler(pp('environment_variables'))
        }
    )

    print response


ACCESS_KEY = pp('access_key')
SECRET_KEY = pp('secret_key')
AWS_REGION = pp('region')


if __name__ == "__main__":
    global client 
    client = boto3.client(
        'lambda',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=AWS_REGION
    )

    update_function_configuration()
    
 
