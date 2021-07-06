n_squares = 4
small_board_list = [1]
for _ in range(n_squares - 1):
	small_board_list.append(2 * small_board_list[-1])
print('4マスの板に小麦を並べる(リスト) : {}'.format(small_board_list))

import numpy as np
small_board_ndarray = np.array(small_board_list)
print('4マスの板に小麦を並べる(ndarray) : {}'.format(small_board_ndarray))

chess_board_22 = small_board_ndarray.reshape(2, 2)
print('2*2マスのチェス盤に小麦を並べる : \n{}'.format(chess_board_22))
