
    if hostname is None:
      hostname = os.uname()[1]

    f = StringIO()

    try:
      if type == 'rsa':
          private_key_obj = paramiko.RSAKey.generate(length)
      elif type == 'dsa':
          private_key_obj = paramiko.DSSKey.generate(length)
      else:
          raise IOError('SSH private key must be `rsa` or `dsa`')
      private_key_obj.write_private_key(f, password=password)
      private_key = f.getvalue()
      public_key = ssh_pubkey_gen(private_key_obj, username=username, hostname=hostname)
      return private_key, public_key
    except IOError:
      raise IOError('These is error when generate ssh key.') 