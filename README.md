# Pass Cracker - A simple (or not) password cracker

## Description

This is a simple password cracker that needs a wordlist and a file with hashes to work.
Then you can choose the encryption algorithm and the program will try to crack the hashes, or you can combine some algorithms (which the program accepts) and it will try to crack the hashes with all the combinations.

## Usage
To see the usage of the program, you can run the following command:

```bash
$ python3 passcracker.py -h
```
## Examples

#### Example with a single algorithm

```bash
$ python3 passcracker.py -w wordlist.txt -H hashes.txt -t md5
```

#### Example combining algorithms

```bash
$ python3 passcracker.py -w wordlist.txt -H hashlist.txt -c md5,sha1,sha256
```

### Example stopping the program after cracking two hashes

```bash
$ python3 passcracker.py -w wordlist.txt -H hashlist.txt -t sha512 -S 2
```

## Algorithms

- md5
- sha1
- sha256
- sha512
- base64

## To Do

- [ ] Add more algorithms
- [ ] Add salt
- [ ] Add more options

## Printscreens
![image](https://github.com/VictorMonteiro7/passcracker/assets/84861666/5d26d87f-4d32-401f-a174-eaabd0183de8)

_This passwords are not real, they are just examples._

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Social Media
[Linkedin](https://www.linkedin.com/in/ovictormonteiro/)

#### Made by Xvng0d
