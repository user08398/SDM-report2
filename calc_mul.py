#!/usr/bin/python3

import re
                
def calc(A, B):
    """
    仕様:
    - A, B は整数型 (int) で 1..999 の範囲
    - 条件に合致する場合 C = A * B を返す
    - 条件に合致しない、または整数以外の入力は -1 を返す
    """
    try:
        # 厳密に int 型のみ許可（文字列や float は不可）
        if not isinstance(A, int) or not isinstance(B, int):
            return -1

        # 範囲チェック
        if 1 <= A <= 999 and 1 <= B <= 999:
            return A * B
        else:
            return -1
    except Exception:
        return -1

        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()