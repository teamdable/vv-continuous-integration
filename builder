#!/usr/bin/env python

import os
import argparse

def build_packages(trusted_host: str, extra_index_url: str):
    if os.path.exists('requirements.txt'):
        command = 'pip install -r requirements.txt'
        command += f' --trusted-host {trusted_host}'
        command += f' --extra-index-url {extra_index_url}'
        os.system(command)
    
    if os.path.exists('package.json'):
        command = 'npm install'
        os.system(command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--trusted-host', type=str, default='')
    parser.add_argument('--extra-index-url', type=str, default='')

    args = parser.parse_args()

    build_packages(args.trusted_host, args.extra_index_url)