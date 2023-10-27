#!/usr/bin/python3

import hashlib
import argparse
import base64

parser = argparse.ArgumentParser(
  prog='PassCracker - by Xvng0d',
  description='Password decrypter',
  usage='python3 xvndecrypt.py -w wordlist.txt -H hashfile.txt -t md5'
)

parser.add_argument('--wordlist', '-w', metavar='wordlist.txt', required=True, help='Wordlist file')
parser.add_argument('--hash', '-H', metavar='hashfile.txt', required=True, help='Hash file')
parser.add_argument('--stop', '-S', metavar='100', default=100, type=int, help='Stop after X passwords cracked')

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--type', '-t', metavar='md5', choices=['md5', 'sha1', 'sha256', 'sha512', 'base64'], help='Hash type')
group.add_argument('--combine', '-c', metavar='md5,base64,sha1', help='Combine hash type')


args = parser.parse_args()

wordlist = args.wordlist
hashfile = args.hash
hashtype = args.type
combine = args.combine
stop = args.stop

passlibs = {}

def decryptor():
  with open(hashfile, 'r') as hsh:
    for hashtxt in hsh:
      cleanHash = hashtxt.strip('\r\n')
      with open(wordlist, 'r', encoding='utf-8', errors='ignore') as word:
        for wrd in word:
          cleanWord = wrd.strip('\r\n')
          if (len(passlibs) == stop):
            break
          if (combine):
            encoded = handleCombine(cleanWord)
          else:
            encoded = encodeFn(hashtype, cleanWord)
          if (encoded == cleanHash):
            passlibs[cleanWord] = encoded
            break


def handleCombine(word):
  combineSplitted = combine.split(',')
  wordEncrypted = word
  for index, tp in enumerate(combineSplitted):
    encrypted = encodeFn(tp, wordEncrypted)
    wordEncrypted = encrypted
    if (len(combineSplitted) - 1 == index):
      return wordEncrypted



def encodeFn(tp, word):
  switch={
    'md5':hashlib.md5,
    'sha1':hashlib.sha1,
    'sha256':hashlib.sha256,
    'sha512':hashlib.sha512,
    'base64': base64.b64encode
  }
  methodType = switch.get(tp, 'Invalid hash type')
  if (tp == 'base64'):
    encoded = methodType(word.encode('utf-8', errors='ignore')).decode('utf-8')
  else:
    encoded = methodType(word.encode('utf-8', errors='ignore')).hexdigest()
  return encoded

def showPass():
  if (len(passlibs) == 0):
    print('No password cracked')
    exit(0)
  for key, value in passlibs.items():
    print(f'Password: {key} - Hash: {value}\n')

def imgTitle():
  print(r'''
 ____                        ____                         __
/\  _`\                     /\  _`\                      /\ \
\ \ \L\ \ __      ____   ___\ \ \/\_\  _ __   __      ___\ \ \/'\      __  _ __
 \ \ ,__/'__`\   /',__\ /',__\ \ \/_/_/\`'__/'__`\   /'___\ \ , <    /'__`/\`'__\
  \ \ \/\ \L\.\_/\__, `/\__, `\ \ \L\ \ \ \/\ \L\.\_/\ \__/\ \ \\`\ /\  __\ \ \/
   \ \_\ \__/.\_\/\____\/\____/\ \____/\ \_\ \__/.\_\ \____\\ \_\ \_\ \____\ \_\
    \/_/\/__/\/_/\/___/ \/___/  \/___/  \/_/\/__/\/_/\/____/ \/_/\/_/\/____/\/_/


  ''')

def main():
  imgTitle()
  decryptor()
  showPass()

if __name__ == '__main__':
  main()

