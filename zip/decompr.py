import zipfile
import optparse
from threading import Thread


# author: huangyuhui
# envir: python 3.7.3
# date: november 20,2019
# tested on the os: windows10
# desc: brute force attack the specified zip file
# repo address: https://github.com/yubuntu0109/penetration-testing-learning
# recommended penetration testing tools are as follows:
# https://github.com/Mebus/cupp
# https://github.com/digininja/CeWL


def extractfile(zfile, password):
    try:
        print('[-] try to decompress the zip file by the password: %s' % password)
        zfile.extractall(pwd=bytes(password, "utf8"))  # https://www.cnblogs.com/Oliva/p/8824040.html
        print('[+] the zip file has decompressed successfully by the password: %s' % password)
        exit(0)
    except:
        pass


def main():
    global zname, dname
    parser = optparse.OptionParser("usage: %prog -f <file> -d <dict>")
    parser.add_option('-f', dest='zname', type='string', help='specified zip file')
    parser.add_option('-d', dest='dname', type='string', help='specified pwd dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print(parser.usage)
        exit(0)

    else:
        zname = options.zname
        dname = options.dname
    zfile = zipfile.ZipFile(zname)
    pwdfile = open(dname)
    for line in pwdfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractfile, args=(zfile, password))
        t.start()


if __name__ == '__main__':
    main()
