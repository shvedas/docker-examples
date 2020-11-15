import getpass
import hashlib
import random

salt_len = 12
algorithm='sha1'

def encode(u, encoding=None):
  return u.encode(encoding, "replace")

passphrase = getpass.getpass('Enter password: ')
h = hashlib.new(algorithm)
salt = ('%0' + str(salt_len) + 'x') % random.getrandbits(4 * salt_len)
h.update(encode(passphrase, 'utf-8') + encode(salt, 'ascii'))

print(':'.join((algorithm, salt, h.hexdigest())))