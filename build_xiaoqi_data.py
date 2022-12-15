import hashlib
import json
import os
import random
import string


def build_hashid():
    ss = list(string.ascii_letters)
    random.shuffle(ss)
    ss = "".join(ss)
    sha = hashlib.sha256()
    sha.update(ss.encode())
    return sha.hexdigest()


def build_cpid():
    dgt = string.digits
    res = "1"
    for _ in range(4):
        res += random.choice(dgt)
    return res

def build_cpname():
    cpname_list = ["JdUnion", "AliExpress", "Kelkoo", "OZON", "天猫", "淘宝", "京东"]
    return random.choice(cpname_list)

def build_ptss():
    ptss_list = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
    rnum = random.randint(1, len(ptss_list))
    res = [random.choice(ptss_list) for _ in range(rnum)]
    return res

def build_xiaoqi_data():
    for _ in range(data_num1):
        hashid = build_hashid()
        cpid = build_cpid()
        cpname = build_cpname()
        ptss = build_ptss()
        res = { "hashId": hashid, "cpId": cpid, "cpName": cpname, "productTags": ptss}
        print(json.dumps(res, ensure_ascii=False), file=fou1)
    fou1.close()


def build_entity_data():
    hashid_list = [json.loads(line).get("hashId") for line in open("xiaoqi_data.txt", "r", encoding="utf-8").readlines()]
    for _ in range(data_num2):
        hashid = random.choice(hashid_list)
        entityid = build_hashid()[:16]
        print(f"{hashid}\t{entityid}", file=fou2)
    fou2.close()



if __name__ == '__main__':
    data_num1 = 10000
    data_num2 = 5000
    output_file1 = "xiaoqi_data.txt"
    output_file2 = "entity_data.txt"
    if os.path.exists(output_file1):
        os.remove(output_file1)
    if os.path.exists(output_file2):
        os.remove(output_file2)
    fou1 = open(output_file1, "a", encoding="utf-8")
    fou2 = open(output_file2, "a", encoding="utf-8")

    build_xiaoqi_data()
    build_entity_data()