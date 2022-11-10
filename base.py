import os


def writeLog(text):
    try:
        with open('log.txt', 'a') as f:
            f.writelines(text + '\n')
    except Exception as error:
        print(error)


def readLog():
    with open('log.txt', 'r') as f:
        return f.read()


def clearLog():
    open('log.txt', 'w').close()


def initLog():
    open('log.txt', 'x').close()


def deleteLog():
    os.remove('log.txt')


