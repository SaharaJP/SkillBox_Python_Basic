nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [s_el for b_el in nice_list
             for m_el in b_el
             for s_el in m_el]

print('Ответ:', nice_list)
