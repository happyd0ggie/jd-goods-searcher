#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import shlex

def get_all_installed_modules():
    all_installed_modules = []
    cmd_str = 'pip3 freeze | grep == > modules.tmp'
    os.system(cmd_str)
    
    with open('modules.tmp', 'r') as f:
        for line in f:
            all_installed_modules.append(line.split('==')[0])

    return all_installed_modules

def check_modules(requirements):
    all_installed_modules = get_all_installed_modules()
    with open(requirements, 'r') as f:
        for line in f:
            module = line.split('>')[0]
            if (module not in all_installed_modules and
                module not in sys.modules and
                module not in sys.builtin_module_names):
                cmd_str = shlex.split('pip3 install {0}'.format(module))
                subprocess.call(cmd_str)
    os.unlink('modules.tmp')

def main():
    pass
    check_modules('requirements.txt')

if __name__ == '__main__':
    main()
