import jieba

print('Full Mode: ')
seg_list = jieba.cut(u'今天上午十点买菜花了10块钱', cut_all=True)
for seg in seg_list:
    print(seg)
print('Default Mode: ')
seg_list = jieba.cut(u'今天上午十点买菜花了10元')
for seg in seg_list:
    print(seg)
print('Cut for search: ')
seg_list = jieba.cut_for_search(u'今天上午十点买菜花了10元')
for seg in seg_list:
    print(seg)
