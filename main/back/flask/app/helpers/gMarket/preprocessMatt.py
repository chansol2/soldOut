import pandas as pd


def preprocessMatt(rawDF):
    df = rawDF

    ##하이브리드매트리스: '하이브리드매트리스'라는 컬럼을 만들고 '스프링', '독립', '본넬'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["하이브리드매트리스"] = (
        (df["prd_nm"].str.contains("라텍스") | df["prd_nm"].str.contains("메모리"))
        & (
            df["prd_nm"].str.contains("스프링")
            | df["prd_nm"].str.contains("독립")
            | df["prd_nm"].str.contains("본넬")
        )
    ) | (df["prd_nm"].str.contains("하이브리드") | df["prd_nm"].str.contains("혼합"))

    ##스프링매트리스: '스프링매트리스'라는 컬럼을 만들고 '스프링', '독립', '본넬'이 들어가고 '하이브리드매트리스' 컬럼에 속하지 않는 로우에는 True 안들어가는 로우에는 False 넣기
    df["스프링매트리스"] = (
        df["prd_nm"].str.contains("스프링")
        | df["prd_nm"].str.contains("독립")
        | df["prd_nm"].str.contains("본넬")
    ) & ~df["하이브리드매트리스"]

    ##라텍스매트리스: '라텍스매트리스'라는 컬럼을 만들고 '라텍스'가 들어가고 '하이브리드매트리스' 컬럼에 속하지 않는 로우에는 True 안들어가는 로우에는 False 넣기
    df["라텍스매트리스"] = df["prd_nm"].str.contains("라텍스") & ~df["하이브리드매트리스"]

    ##메모리폼매트리스: '메모리폼매트리스'라는 컬럼을 만들고 '메모리'가 들어가고 '하이브리드매트리스' 컬럼에 속하지 않는 로우에는 True 안들어가는 로우에는 False 넣기
    df["메모리폼매트리스"] = df["prd_nm"].str.contains("메모리") & ~df["하이브리드매트리스"]

    ##접이식매트리스: '접이식매트리스'라는 컬럼을 만들고 '스프링', '독립', '본넬'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["접이식매트리스"] = df["prd_nm"].str.contains("접이식")

    ##에어매트리스: '에어매트리스'라는 컬럼을 만들고 '스프링', '독립', '본넬'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["에어매트리스"] = df["prd_nm"].str.contains("에어")

    ##물매트리스: '물매트리스'라는 컬럼을 만들고 '스프링', '독립', '본넬'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["물매트리스"] = df["prd_nm"].str.contains("아쿠아 매트리스") | df["prd_nm"].str.contains(
        "물매트리스"
    )

    ##토퍼: '토퍼'라는 컬럼을 만들고 '토퍼' 도는 '타퍼'가 들어가고 '하이브리드매트리스' 컬럼에 속하지 않는 로우에는 True 안들어가는 로우에는 False 넣기
    df["토퍼"] = (
        df["prd_nm"].str.contains("토퍼") | df["prd_nm"].str.contains("타퍼")
    ) & ~df["하이브리드매트리스"]

    ##멀티싱글: '멀티싱글'라는 컬럼을 만들고 '멀티싱글' 또는 'MS'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["멀티싱글"] = df["prd_nm"].str.contains("멀티싱글") | df["prd_nm"].str.contains(
        "MS침대| MS"
    )

    ##슈퍼싱글: '슈퍼싱글'라는 컬럼을 만들고 슈퍼싱글' 또는 'SS' 또는 'ss'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["슈퍼싱글"] = (
        df["prd_nm"].str.contains("슈퍼싱글")
        | df["prd_nm"].str.contains("수퍼싱글")
        | df["prd_nm"].str.contains("SS")
        | df["prd_nm"].str.contains("ss")
    )

    ##싱글: '싱글'이라는 컬럼을 만들고 '멀티싱글', '슈퍼싱글' 칼럼 값이 False이고 상품명에 싱글' 또는 'S' 또는 's'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["싱글"] = (
        ~df["멀티싱글"]
        & ~df["슈퍼싱글"]
        & (
            df["prd_nm"].str.contains("싱글")
            | df["prd_nm"].str.contains("S")
            | df["prd_nm"].str.contains("s")
        )
    )

    ##더블: '더블'이라는 컬럼을 만들고 '더블'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["더블"] = df["prd_nm"].str.contains("더블")

    ##퀸: '퀸'이라는 컬럼을 만들고 '퀸' 또는 'Q'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["퀸"] = df["prd_nm"].str.contains("퀸") | df["prd_nm"].str.contains("Q")

    ##라지킹: '라지킹'이라는 컬럼을 만들고 '라지킹' 또는 'LK'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["라지킹"] = df["prd_nm"].str.contains("라지킹") | df["prd_nm"].str.contains("LK")

    ##칼킹: '칼킹'이라는 컬럼을 만들고 'CK'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["칼킹"] = (
        df["prd_nm"].str.contains("CK")
        | df["prd_nm"].str.contains("칼킹")
        | df["prd_nm"].str.contains("로얄킹")
    )

    ##킹: '킹'이라는 컬럼을 만들고 '라지킹', '칼킹' 칼럼 값이 False이고 상품명에 'CBK'가 안들어가고 '킹','k' 또는 'K' 가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["킹"] = (
        ~df["라지킹"]
        & ~df["칼킹"]
        & ~df["prd_nm"].str.contains("CBK")
        & (
            df["prd_nm"].str.contains("킹")
            | df["prd_nm"].str.contains("k")
            | df["prd_nm"].str.contains("K")
        )
    )

    ##타이트탑: '타이트탑'이라는 컬럼을 만들고 '타이트탑'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["타이트탑"] = df["prd_nm"].str.contains("타이트탑")

    ##필로우탑: '필로우탑'이라는 컬럼을 만들고 '필로우탑'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["필로우탑"] = df["prd_nm"].str.contains("필로우탑")

    ##유로탑: '유로탑'이라는 컬럼을 만들고 '유로탑'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["유로탑"] = df["prd_nm"].str.contains("유로탑")

    ##독립스프링: '독립스프링'이라는 컬럼을 만들고 '독립스프링'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["독립스프링"] = df["prd_nm"].str.contains("독립")

    ##본넬스프링: '본넬스프링'이라는 컬럼을 만들고 '본넬스프링'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["본넬스프링"] = df["prd_nm"].str.contains("본넬")

    ##라텍스: '라텍스'이라는 컬럼을 만들고 '라텍스매트리스' 컬럼이 트루인 로우에는 True 안들어가는 로우에는 False 넣기
    df["라텍스소재"] = df["prd_nm"].str.contains("라텍스")

    ##메모리폼소재: '메모리폼소재'이라는 컬럼을 만들고 '메모리폼매트리스' 컬럼이 트루인 로우에는 True 안들어가는 로우에는 False 넣기
    df["메모리폼소재"] = df["prd_nm"].str.contains("메모리")

    ##솜소재: '솜소재'이라는 컬럼을 만들고 '솜'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["솜소재"] = df["prd_nm"].str.contains("솜")

    ##깃털소재: '깃털소재'이라는 컬럼을 만들고 '깃털'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["깃털소재"] = df["prd_nm"].str.contains("깃털")

    ##양모소재: '양모소재'이라는 컬럼을 만들고 '양모'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["양모소재"] = df["prd_nm"].str.contains("양모")

    ##극세사소재: '극세사소재'이라는 컬럼을 만들고 '극세사'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["극세사소재"] = df["prd_nm"].str.contains("극세사")

    ##커버분리형: '커버분리형'이라는 컬럼을 만들고 '커버'가 들어가고 '분리'도 들어가는 로우에는 True 안들어가는 로우(커버 일체형)에는 False 넣기
    df["커버분리형"] = df["prd_nm"].str.contains("커버") & df["prd_nm"].str.contains("분리")

    ##두께10cm미만: '두께10cm미만'이라는 컬럼을 만들고 '0~9cm'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["두께10cm미만"] = (
        df["prd_nm"].str.contains(" 1cm")
        | df["prd_nm"].str.contains(" 2cm")
        | df["prd_nm"].str.contains(" 3cm")
        | df["prd_nm"].str.contains(" 4cm")
        | df["prd_nm"].str.contains(" 5cm")
        | df["prd_nm"].str.contains(" 6cm")
        | df["prd_nm"].str.contains(" 7cm")
        | df["prd_nm"].str.contains(" 8cm")
        | df["prd_nm"].str.contains(" 9cm")
    )

    ##두께10~19cm: '두께10~19cm'이라는 컬럼을 만들고 '10~19cm'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["두께10~19cm"] = (
        df["prd_nm"].str.contains(" 10cm")
        | df["prd_nm"].str.contains(" 11cm")
        | df["prd_nm"].str.contains(" 12cm")
        | df["prd_nm"].str.contains(" 13cm")
        | df["prd_nm"].str.contains(" 14cm")
        | df["prd_nm"].str.contains(" 15cm")
        | df["prd_nm"].str.contains(" 16cm")
        | df["prd_nm"].str.contains(" 17cm")
        | df["prd_nm"].str.contains(" 18cm")
        | df["prd_nm"].str.contains(" 19cm")
    )

    ##두께20~29cm: '두께20~29cm'이라는 컬럼을 만들고 '20~29cm'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["두께20~29cm"] = (
        df["prd_nm"].str.contains(" 20cm")
        | df["prd_nm"].str.contains(" 21cm")
        | df["prd_nm"].str.contains(" 22cm")
        | df["prd_nm"].str.contains(" 23cm")
        | df["prd_nm"].str.contains(" 24cm")
        | df["prd_nm"].str.contains(" 25cm")
        | df["prd_nm"].str.contains(" 26cm")
        | df["prd_nm"].str.contains(" 27cm")
        | df["prd_nm"].str.contains(" 28cm")
        | df["prd_nm"].str.contains(" 29cm")
    )

    ##두께30이상: '두께30이상'이라는 컬럼을 만들고 '30~39cm'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["두께30이상"] = (
        df["prd_nm"].str.contains(" 30cm")
        | df["prd_nm"].str.contains(" 31cm")
        | df["prd_nm"].str.contains(" 32cm")
        | df["prd_nm"].str.contains(" 33cm")
        | df["prd_nm"].str.contains(" 34cm")
        | df["prd_nm"].str.contains(" 35cm")
        | df["prd_nm"].str.contains(" 36cm")
        | df["prd_nm"].str.contains(" 37cm")
        | df["prd_nm"].str.contains(" 38cm")
        | df["prd_nm"].str.contains(" 39cm")
    )

    ##양면사용: '양면사용'이라는 컬럼을 만들고 '양면'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["양면사용"] = df["prd_nm"].str.contains("양면")

    ##쿨링: '쿨링'이라는 컬럼을 만들고 '쿨'이 들어가고 '쿨론','쿨쿨','잠스쿨'은 안들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["쿨링"] = (
        df["prd_nm"].str.contains("쿨")
        & ~df["prd_nm"].str.contains("쿨론")
        & ~df["prd_nm"].str.contains("쿨쿨")
        & ~df["prd_nm"].str.contains("잠스쿨")
    )

    ##알러지/진드기방지: '알러지/진드기방지'이라는 컬럼을 만들고 '알러지' 또는 '진드기'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["알러지/진드기방지"] = df["prd_nm"].str.contains("알러지") | df["prd_nm"].str.contains(
        "진드기"
    )

    ##향균: '향균'이라는 컬럼을 만들고 '향균'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["향균"] = df["prd_nm"].str.contains("향균")
