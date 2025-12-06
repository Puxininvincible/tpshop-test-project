import json
def read_json(filename):
    filepath="../data/"+filename
    # 调用 load方法
    with open(filepath,"r",encoding="utf-8")as f:
        return json.load(f)

# if __name__ == '__main__':
#     datas=read_json("login.json")
#
#     arrs=[]
#     for data in read_json("login.json").values():
#         arrs.append((data.get("username"),
#                      data.get("password"),
#                      data.get("verify_code"),
#                      data.get("expect_result"),
#                      data.get("success")))
#     print(arrs)