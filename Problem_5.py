# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt


# 関数の定義
def chess_board_wheal(vertical, side):
	"""
	function : 縦[vertical] * 横[side]のマスを持つチェス盤に1,2,4と倍々に小麦を置いた配列[chess_board_and_wheal]を返す関数
	:param vertical : int
		チェス盤の縦のマス数
	:param side : int
		チェス盤の横のマス数
	number_of_square : int
		マスの総数
	board_list : list
		マスを右上から一列に並べたと仮定して小麦を置いたリスト
	:return : chess_board_chess_wheal
		小麦を置いた後の配列
	"""

	# マスの合計の計算
	number_of_square = vertical * side
	# リストの作成及び初期値の代入
	board_list = [1]
	# リストの計算及び追加
	for _ in range(number_of_square - 1):
		board_list.append(2 * board_list[-1])
	# ndarrayへの変換
	board_ndarray = np.array(board_list)
	# 指定された形への変換
	chess_board_and_wheal = board_ndarray.reshape(vertical, side)

	# 返り値の設定
	return chess_board_and_wheal


# 8*8のマスのチェス盤での小麦の数の計算
chess_board_88 = chess_board_wheal(8, 8)

# 前後半の小麦の数を求める計算式
first_half = 0
latter_half = 0
count1 = 0
count2 = 0

# 計算
for column in range(chess_board_88.shape[0]):
	for row in range(chess_board_88.shape[1]):
		if column <= 3:
			first_half += chess_board_88[column][row]
			count1 += 1
		else:
			latter_half += chess_board_88[column][row]
			count2 += 1

# 結果の表示
print(count1 == count2)
print('チェス盤の後半にある小麦の数は前半にある小麦の数の{:e}倍です。'.format(latter_half // first_half))
