library(treemap)

# Create data
# group = c('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100')
# value = c(1071, 483, 488, 434, 410, 389, 399, 364, 366, 369, 303, 321, 294, 301, 281, 253, 259, 252, 243, 290, 266, 248, 259, 231, 250, 244, 245, 259, 259, 234, 233, 243, 232, 233, 249, 245, 246, 244, 244, 233, 239, 261, 239, 250, 230, 233, 229, 235, 221, 244, 258, 266, 238, 279, 243, 245, 248, 260, 226, 249, 250, 251, 252, 257, 238, 236, 258, 246, 233, 246, 281, 267, 219, 236, 256, 245, 233, 250, 233, 222, 261, 255, 235, 260, 219, 268, 251, 259, 237, 235, 358, 320, 290, 278, 253, 248, 261, 229, 209, 166)
# data = data.frame(group,value)

key = c('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87')
value = c(1744, 1441, 1314, 1322, 1392, 1527, 1538, 1559, 1384, 1242, 1239, 1092, 1050, 1011, 899, 838, 685, 672, 558, 2215, 430, 350, 278, 210, 205, 166, 137, 111, 93, 87, 66, 56, 48, 38, 30, 40, 23, 21, 41, 23, 20, 22, 16, 12, 12, 8, 9, 11, 7, 6, 5, 13, 8, 5, 4, 5, 4, 3, 2, 2, 1, 2, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
data = data.frame(key, value)

# treemap
tree <- treemap(data, index='key', vSize='value', type='index')

print(tree)
