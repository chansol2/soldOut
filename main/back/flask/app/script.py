import pandas as pd

coupang = pd.read_csv("app/csvs/changed/coupang.csv")
gmarket = pd.read_csv("app/csvs/changed/gmarket.csv")
ohouse = pd.read_csv("app/csvs/changed/ohouse.csv")
oneroommake = pd.read_csv("app/csvs/changed/oneroommake.csv")
ssg = pd.read_csv("app/csvs/changed/ssg.csv")
tenbyten = pd.read_csv("app/csvs/changed/tenbyten.csv")

# lst = [coupang, gmarket, ohouse, oneroommake, ssg, tenbyten]

# d = {
#     "일반침대": 10101,
#     "수납침대": 10102,
#     "벙커침대": 10103,
#     "깔판": 10104,
#     "매트리스": 10201,
#     "토퍼": 10202,
#     "화장대": 103,
#     "거울": 104,
#     "협탁/사이드테이블": 105,
#     "일반소파": 20101,
#     "리클라이너소파": 20102,
#     "소파베드": 20103,
#     "안락의자/빈백": 20104,
#     "밥상/테이블": 202,
#     "스툴": 203,
#     "서랍장": 301,
#     "선반": 302,
#     "렌지대": 303,
#     "옷장": 30401,
#     "행거": 30402,
#     "책상": 401,
#     "책상의자": 40201,
#     "인테리어의자": 40202,
#     "책장": 403,
#     "카페감성테이블": 8101,
#     "갬성돋는컵/잔": 8102,
#     "포인트그릇/식기": 8103,
#     "식탁보/테이블매트": 8104,
#     "홈카페가전": 8105,
#     "집콕모드가구": 8201,
#     "세상편한쿠션": 8202,
#     "실용성갑거치대": 8203,
#     "집콕가전": 8204,
#     "집콕놀거리": 8205,
#     "파티용필수장식": 8301,
#     "턴업조명": 8302,
#     "술맛달달술잔": 8303,
#     "알콜력상승아이템": 8304,
#     "게이밍의자/발받침": 8401,
#     "게이밍책상": 8402,
#     "게이밍책상꾸미기": 8403,
#     "PC방감성조명": 8404,
# }

# for seller in lst:
#     for i, row in seller.iterrows():
#         row["cate_nm"] = d[row["cate_nm"]]
#     s = ""
#     if seller is coupang:
#         s = "coupang"
#     elif seller is gmarket:
#         s = "gmarket"
#     elif seller is ohouse:
#         s = "ohouse"
#     elif seller is oneroommake:
#         s = "oneroommake"
#     elif seller is ssg:
#         s = "ssg"
#     elif seller is tenbyten:
#         s = "tenbyten"
#     else:
#         print("sth wrong")
#     seller.to_csv(f"app/csvs/changed/{s}.csv")

coupang["has_stock"] = 1
coupang.to_csv("app/csvs/changed/coupang.csv")
gmarket["has_stock"] = 1
gmarket.to_csv("app/csvs/changed/gmarket.csv")
ohouse["has_stock"] = 1
ohouse.to_csv("app/csvs/changed/ohouse.csv")
oneroommake["has_stock"] = 1
oneroommake.to_csv("app/csvs/changed/oneroommake.csv")
ssg["has_stock"] = 1
ssg.to_csv("app/csvs/changed/ssg.csv")
tenbyten["has_stock"] = 1
tenbyten.to_csv("app/csvs/changed/tenbyten.csv")
