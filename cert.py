#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: Jeay 
 * @Date: 2018-05-20 10:24:52 
 * @Last Modified by: Jeay
 * @Last Modified time: 2018-05-20 13:31:00
 * /
'''

import os
import rsa

#测试是否存在密钥对

# print os.environ['HOME']
# print os.path.expandvars('$HOME')
# print os.path.expanduser('~')

#os.path.exists('～/.ssh')

class cert():
  def __init__(self):
    self.__sshpath = os.path.expanduser('~') + '/.ssh'
    self.__pubkey = ''
    self.__privkey = ''
    self.pubkey_path = self.__sshpath + '/id_rsa.pub'
    self.privkey_path = self.__sshpath + '/id_rsa'
    self.has_rsa = False
    if os.path.exists(self.pubkey_path) and os.path.exists(self.privkey_path):
      self.has_rsa = True
    else:
      self.__gen()
  def __gen(self):
    if self.has_rsa == False:
      # 生成密钥
      (pubkey, privkey) = rsa.newkeys(1024)
      self.__pubkey = pubkey.save_pkcs1().decode()
      self.__privkey = privkey.save_pkcs1().decode()
      print(self.__privkey)
      # 保存密钥
      if os.path.exists(self.__sshpath) == False:
        os.makedirs(self.__sshpath)
      with open(self.pubkey_path,'w+') as f:
        f.write(self.__pubkey)
      with open(self.privkey_path,'w+') as f:
        f.write(self.__privkey)
      f.close()
      
  def get_pubkey(self):
    if self.__pubkey == '':
      f = open(self.pubkey_path)
      self.__pubkey = f.read()
      f.close()
    return self.__pubkey
  def get_privkey(self):
    if self.__privkey == '':
      f = open(self.privkey_path)
      self.__privkey = f.read()
      f.close()
    return self.__privkey
  def get_loginkey(self):
    pubk = self.get_pubkey()
    plist = pubk.split('\n')
    pubk = 'ssh-rsa ' + plist[1] + plist[2] + plist[3] + ' admin@jeay.net'
    return pubk

pubk = cert().get_loginkey()
# privkey = cert().get_privkey()

print(pubk)