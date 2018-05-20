#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: Jeay 
 * @Date: 2018-05-20 10:24:52 
 * @Last Modified by: Jeay
 * @Last Modified time: 2018-05-20 15:34:03
 * /
'''

import os, io, paramiko, stat

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
      key = self.gen_keys()
      self.__pubkey = key["public_key"]
      self.__privkey = key["private_key"]
      # 保存密钥
      if os.path.exists(self.__sshpath) == False:
        os.makedirs(self.__sshpath)
      with open(self.pubkey_path, 'w+') as f:
        f.write(self.__pubkey)
        os.chmod(self.pubkey_path, 0o0644)
      with open(self.privkey_path,'w+') as f:
        f.write(self.__privkey)
        os.chmod(self.privkey_path, 0o0644)
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

  def gen_keys(self,key=""):
    output = io.StringIO()
    sbuffer = io.StringIO()
    key_content = {}
    if not key:
      try:
        key = paramiko.RSAKey.generate(2048)
        key.write_private_key(output)
        private_key = output.getvalue()
      except IOError:
        raise IOError('gen_keys: there was an error writing to the file')
      except Exception as e:
        print(e)
    else:
      private_key = key
      output.write(key)
      try:
        key = paramiko.RSAKey.from_private_key(output)
      except Exception as e:
        print(e)
  
    for data in [key.get_name(),
                 " ",
                 key.get_base64(),
                 " %s@%s" % ("magicstack", os.uname()[1])]:
      sbuffer.write(data)
    public_key = sbuffer.getvalue()
    key_content['public_key'] = public_key
    key_content['private_key'] = private_key
    return key_content

# pubk = cert().get_loginkey()
# privkey = cert().get_privkey()

# print(pubk)
#pubkey = paramiko.RSAKey.generate(2048)
#key = paramiko.RSAKey.generate(2048)
#print(key.write_private_key())
