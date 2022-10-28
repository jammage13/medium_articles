# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:22:17 2022

@author: Jam
"""

import keyring

keyring.set_password('system', 'username', 'password')

password = keyring.get_password('system', 'username')

print(password)