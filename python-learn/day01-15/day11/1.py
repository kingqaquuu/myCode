'''
Author: kingqaquuu
Date: 2024-03-16 19:05:40
FilePath: \myCode\python-learn\day01-15\day11\1.py
'''
def main():
    f = None
    try:
        f=open('致橡树.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()