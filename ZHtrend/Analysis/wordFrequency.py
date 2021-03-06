# -*- encoding:utf-8 -*-
import jieba.analyse
from ZHtrend.model.User import User

if __name__ == "__main__":
    users = User.all()
    l = []
    for u in users:
        l.append(u.get('description'))
        l.append(u.get('profession'))
    seg_list = jieba.cut_for_search(" ".join(l))
    tags = jieba.analyse.extract_tags(" ".join(l), withWeight=True, topK=30000)
    db.WFUPloadWF(tags)
    print("已经成功生成词频。")
