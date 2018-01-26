#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# from collections import defaultdict
# color_by_images = defaultdict(list)
#
# import glob
# for file_name in glob.glob('data/cell/*.png'):
#     img_cell = cv2.imread(file_name)
#     color = get_main_color_bgr(img_cell)
#     # print(color, file_name)
#
#     color_by_images[color].append(file_name)
#
# # С сохранением файлов по цвету
# for color, images in sorted(color_by_images.items(), key=lambda x: len(x[1]), reverse=True):
#     i = 1
#
#     print('{} ({}):'.format(color, len(images)))
#     for file_name in images:
#         # new_file_name = 'data/cell_color/{}__{}.png'.format('.'.join(map(str, color)), i)
#         new_file_name = 'cell_color/{}__{}.png'.format(color, i)
#         print('    ' + file_name + ' -> ' + new_file_name)
#         import shutil
#         shutil.copy(file_name, new_file_name)
#
#         i += 1
#
#     print()
#
# quit()


# for color, images in sorted(color_by_images.items(), key=lambda x: len(x[1]), reverse=True):
#     print('{} ({}):'.format(color, len(images)))
#     for file_name in images:
#         print('    ' + file_name)
#
#     print()


# board = get_game_board('fojUvGQfBRc.jpg')
# point_by_contour = get_cell_point_by_contour(board)
# show_cell_on_board(board, point_by_contour)

# import glob
# for file_name in glob.glob('data/img/*.jpg'):
#     print(file_name)
#
#     try:
#         board = get_game_board(file_name)
#         point_by_contour = get_cell_point_by_contour(board)
#         # show_cell_on_board(board, point_by_contour)
#
#         for contour in point_by_contour.values():
#             crop_img = crop_by_contour(board, contour)
#
#             import hashlib
#             name_img = 'data/cell/' + hashlib.sha1(crop_img.data.tobytes()).hexdigest() + '.png'
#             # cv2.imshow(name_img, crop_img)
#             # hash_by_img[name_img] = crop_img
#             print(name_img)
#
#             cv2.imwrite(name_img, crop_img)
#
#     except Exception as e:
#         print(e)
#

# #
# # Save cell images:
#
# hash_by_img = dict()
#
# import hashlib
# import glob
# for file_name in glob.glob('data/img/*.jpg'):
#     try:
#         board = get_game_board(file_name)
#         point_by_contour = get_cell_point_by_contour(board)
#
#         cell_contours = list(point_by_contour.values())
#         for contour in cell_contours:
#             crop_img = crop_by_contour(board, contour)
#
#             name_img = hashlib.sha1(crop_img.data.tobytes()).hexdigest() + '.png'
#             # cv2.imshow(name_img, crop_img)
#             hash_by_img[name_img] = crop_img
#
#             cv2.imwrite('cell/' + name_img, crop_img)
#
#     except:
#         pass
#
#
# print(len(hash_by_img))
# # print(hash_by_img.keys())
# quit()


# import glob
# for file_name in glob.glob('test/*.png'):
#     image = cv2.imread(file_name)
#     print(get_main_color_bgr(image), get_main_color_bgr(image, append_gray=False), file_name)
# quit()


# import glob
# for file_name in glob.glob('*.png'):
#     board_img = get_game_board(cv2.imread(file_name))
#     point_by_contour = get_cell_point_by_contour(board_img)
#     show_cell_on_board(board_img, point_by_contour)
#     value_matrix = get_value_matrix_from_board(board_img, point_by_contour)
#     print('value_matrix:', value_matrix)


# pil_image = pyautogui.screenshot()
# opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
# board_img = get_game_board(opencv_image)
# # board_img = get_game_board(cv2.imread('img_bad.png'))
# # board_img = get_game_board(cv2.imread('img.png'))
# point_by_contour = get_cell_point_by_contour(board_img)
# show_cell_on_board(board_img, point_by_contour)
# value_matrix = get_value_matrix_from_board(board_img, point_by_contour)
# print('value_matrix:', value_matrix)
#
# cv2.waitKey()
# cv2.destroyAllWindows()
# quit()

import cv2
import utils

img = cv2.imread('unnecessary/next_game__full_screen.png')
board = img

# img = cv2.imread('unnecessary/next_game.png')
# cv2.imshow(str(img), img)
#
# board = utils.get_game_board(img)
# cv2.imshow(str(board), board)


gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
# cv2.imshow(str(gray), gray)

ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# cv2.imshow(str(thresh), thresh)

img_contours, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours), [cv2.contourArea(i) for i in contours])

contours = [i for i in contours if cv2.contourArea(i) > 6000 and cv2.contourArea(i) < 7000]
print(len(contours), [cv2.contourArea(i) for i in contours])

img_with_contour = board.copy()
cv2.drawContours(img_with_contour, contours, -1, (0, 255, 0), 3)
cv2.imshow(str(img_with_contour), img_with_contour)

# rect_contours = sorted([cv2.boundingRect(i) for i in contours], key=lambda x: x[0])
# print(rect_contours)
sorted_contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])
# print(sorted_contours)

img_with_contour = board.copy()
cv2.drawContours(img_with_contour, sorted_contours, 0, (0, 255, 0), 3)
cv2.imshow(str(img_with_contour), img_with_contour)

cv2.waitKey()
