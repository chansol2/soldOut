import pandas as pd


def trimBed(rawDF):

    ##침대를 포함하지 않는 rows 다 drop
    index0 = df[~df["prd_nm"].str.contains("침대")].index

    df.drop(index0, inplace=True)

    ##메트 또는 매트를 포함하는 rows 다 drop
    index1 = df[df["prd_nm"].str.contains("메트") | df["prd_nm"].str.contains("매트")].index

    df.drop(index1, inplace=True)

    ## 돌침대 관련 rows 다 drop
    index2 = df[
        df["prd_nm"].str.contains("흙")
        | df["prd_nm"].str.contains("숯")
        | df["prd_nm"].str.contains("돌")
        | df["prd_nm"].str.contains("황토")
        | df["prd_nm"].str.contains("맥반석")
        | df["prd_nm"].str.contains("옥")
        | df["prd_nm"].str.contains("현대의료기")
    ].index

    df.drop(index2, inplace=True)

    ## 쿠션이란 단어는 있는데 헤드라는 단어는 포함하지 않는 rows 다 drop

    index3 = df[
        df["prd_nm"].str.contains("쿠션") & ~df["prd_nm"].str.contains("헤드")
    ].index

    df.drop(index3, inplace=True)

    ## 기타 필요없는 것들 모두 제거

    index4 = df[
        df["prd_nm"].str.contains("토퍼")
        | df["prd_nm"].str.contains("테이블")
        | df["prd_nm"].str.contains("커버")
        | df["prd_nm"].str.contains("메모리")
        | df["prd_nm"].str.contains("안전가드")
        | df["prd_nm"].str.contains("안전바")
        | df["prd_nm"].str.contains("의료")
        | df["prd_nm"].str.contains("이불")
        | df["prd_nm"].str.contains("갈비살")
        | df["prd_nm"].str.contains("옷장")
        | df["prd_nm"].str.contains("등받이")
        | df["prd_nm"].str.contains("등 받이")
        | df["prd_nm"].str.contains("자동차")
        | df["prd_nm"].str.contains("차량")
        | df["prd_nm"].str.contains("거치대")
        | df["prd_nm"].str.contains("침대등")
        | df["prd_nm"].str.contains("스커트")
        | df["prd_nm"].str.contains("패드")
        | df["prd_nm"].str.contains("협탁")
        | df["prd_nm"].str.contains("악세사리")
        | df["prd_nm"].str.contains("전용")
        | df["prd_nm"].str.contains("틈새")
    ].index

    df.drop(index4, inplace=True)

    df.drop_duplicates

    df.to_csv("bed.csv")

    return df
