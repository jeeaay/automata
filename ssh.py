#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: Jeay 
 * @Date: 2018-05-20 10:32:09 
 * @Last Modified by: Jeay
 * @Last Modified time: 2018-05-20 14:01:04
 */
'''

import paramiko

import cert

private_key = cert.cert().get_privkey()
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#第一次登录的认证信息
# 连接服务器
try:
  ssh.connect(hostname='45.32.135.211', port=22, username='root', pkey=private_key)
  print(1)
except Exception as e:
  ssh.connect(hostname='45.32.135.211', port=22, username='root', password='Qj-1.7d?uHKQWahW')
  public_key = cert.cert().get_loginkey()
  # 写入公钥
  ssh.exec_command('echo "' + public_key + '">> ~/.ssh/authorized_keys')
  print(2)

#ssh.connect(hostname='45.32.135.211', port=22, username='root', password='Qj-1.7d?uHKQWahW')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls /')
# 获取命令结果
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())
# 关闭连接
ssh.close()