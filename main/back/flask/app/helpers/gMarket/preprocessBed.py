import pandas as pd


def preprocessBed(rawDF):
    df = rawDF

    ##패밀리침대: '패밀리침대'라는 컬럼을 만들고 '패밀리'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["패밀리침대"] = df["prd_nm"].str.contains("패밀리")

    ##수납침대: '수납침대'라는 컬럼을 만들고 '수납' 또는 '서랍' 또는 '책장'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["수납침대"] = (
        df["prd_nm"].str.contains("수납")
        | df["prd_nm"].str.contains("서랍")
        | df["prd_nm"].str.contains("책장")
    )

    ##이층침대: '이층침대'라는 컬럼을 만들고 '이층' 또는 '2층'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["이층침대"] = df["prd_nm"].str.contains("이층") | df["prd_nm"].str.contains("2층")

    ##벙커침대: '벙커침대'라는 컬럼을 만들고 '벙커'는 들어가고 '벙커형은 안들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["벙커침대"] = df["prd_nm"].str.contains("벙커") & ~df["prd_nm"].str.contains("벙커형")

    ##저상형침대: '저상형침대'라는 컬럼을 만들고 '저상형' 또는 '깔판' 또는 '받침대'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["저상형침대"] = (
        df["prd_nm"].str.contains("저상형")
        | df["prd_nm"].str.contains("깔판")
        | df["prd_nm"].str.contains("받침대")
    )

    ##모션침대: '모션침대'라는 컬럼을 만들고 '모션' 또는 '전동'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["모션침대"] = df["prd_nm"].str.contains("모션") | df["prd_nm"].str.contains("전동")

    ##트윈형모션침대: '트윈형모션침대'라는 컬럼을 만들고 '모션침대' 컬럼값이 True이고 상품명에'트윈'가 들어가는 로우에는 True(트윈) 안들어가는 로우에는 False(일체) 넣기
    df["트윈형모션침대"] = df["모션침대"] & df["prd_nm"].str.contains("트윈")

    ##접이식침대: '접이식침대'라는 컬럼을 만들고 '접이식' 또는 '라꾸라꾸' 또는 '야전' 또는 '캠핑' 또는 '마사지' 또는 '스포츠'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["접이식침대"] = (
        df["prd_nm"].str.contains("접이식")
        | df["prd_nm"].str.contains("라꾸라꾸")
        | df["prd_nm"].str.contains("야전")
        | df["prd_nm"].str.contains("캠핑")
        | df["prd_nm"].str.contains("마사지")
        | df["prd_nm"].str.contains("스포츠")
    )

    ##야전침대: '야전침대'라는 컬럼을 만들고 '접이식침대' 컬럼값이 True이고 상품명에'야전' 또는 '캠핑'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["야전침대"] = df["접이식침대"] & (
        df["prd_nm"].str.contains("야전") | df["prd_nm"].str.contains("캠핑")
    )

    ##마사지침대: '마사지침대'라는 컬럼을 만들고 '접이식침대' 컬럼값이 True이고 상품명에'마사지' 또는 '스포츠'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["마사지침대"] = df["접이식침대"] & (
        df["prd_nm"].str.contains("마사지") | df["prd_nm"].str.contains("스포츠")
    )

    ##데이베드: '데이베드'라는 컬럼을 만들고 '데이베드'또는 '데이배드'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["데이베드"] = df["prd_nm"].str.contains("데이베드") | df["prd_nm"].str.contains("데이배드")

    ##일체형침대: '일체형침대'라는 컬럼을 만들고 '일체'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["일체형침대"] = df["prd_nm"].str.contains("일체")

    ##캐노피침대: '캐노피침대'라는 컬럼을 만들고 '케노피' 또는 '케노피'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["캐노피침대"] = df["prd_nm"].str.contains("케노피") | df["prd_nm"].str.contains("캐노피")

    ##월베드: '월베드'라는 컬럼을 만들고 '월베드'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["월베드"] = df["prd_nm"].str.contains("월베드")

    ##이단침대: '이단침대'라는 컬럼을 만들고 '이단' 또는 '슬라이딩'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["이단침대"] = df["prd_nm"].str.contains("이단") | df["prd_nm"].str.contains("슬라이딩")

    ##3층침대: '3층침대'라는 컬럼을 만들고 '3층'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["3층침대"] = df["prd_nm"].str.contains("3층")

    ##침대헤드보드: '침대헤드보드'라는 컬럼을 만들고 '침대헤드' 또는 '헤드보드' 또는 '헤드쿠션' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["침대헤드보드"] = (
        df["prd_nm"].str.contains("침대헤드")
        | df["prd_nm"].str.contains("헤드보드")
        | df["prd_nm"].str.contains("헤드쿠션")
    )

    ##멀티싱글: '멀티싱글'라는 컬럼을 만들고 '멀티싱글' 또는 'MS'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["멀티싱글"] = df["prd_nm"].str.contains("멀티싱글") | df["prd_nm"].str.contains(
        "MS침대| MS"
    )

    ##슈퍼싱글: '슈퍼싱글'라는 컬럼을 만들고 '패밀리침대', '모션침대' 칼럼 값이 False이고 상품명에 슈퍼싱글' 또는 'SS' 또는 'ss'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["슈퍼싱글"] = (
        ~df["이층침대"]
        & ~df["패밀리침대"]
        & ~df["모션침대"]
        & (
            df["prd_nm"].str.contains("슈퍼싱글")
            | df["prd_nm"].str.contains("수퍼싱글")
            | df["prd_nm"].str.contains("SS")
            | df["prd_nm"].str.contains("ss")
        )
    )

    ##싱글: '싱글'이라는 컬럼을 만들고 '패밀리침대', '모션침대' ,'멀티싱글', '슈퍼싱글' 칼럼 값이 False이고 상품명에 싱글' 또는 'S' 또는 's'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["싱글"] = (
        ~df["이층침대"]
        & ~df["패밀리침대"]
        & ~df["모션침대"]
        & ~df["멀티싱글"]
        & ~df["슈퍼싱글"]
        & (
            df["prd_nm"].str.contains("싱글")
            | df["prd_nm"].str.contains("S")
            | df["prd_nm"].str.contains("s")
        )
    )

    ##더블: '더블'이라는 컬럼을 만들고 '패밀리침대', '모션침대'칼럼 값이 False이고 상품명에 '더블'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["더블"] = (
        ~df["이층침대"] & ~df["패밀리침대"] & ~df["모션침대"] & df["prd_nm"].str.contains("더블")
    )

    ##퀸: '퀸'이라는 컬럼을 만들고 '패밀리침대', '모션침대'칼럼 값이 False이고 상품명에 '퀸' 또는 'Q'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["퀸"] = (
        ~df["이층침대"]
        & ~df["패밀리침대"]
        & ~df["모션침대"]
        & (df["prd_nm"].str.contains("퀸") | df["prd_nm"].str.contains("Q"))
    )

    ##칼킹: '칼킹'이라는 컬럼을 만들고 '패밀리침대', '모션침대'칼럼 값이 False이고 상품명에 'CK'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["칼킹"] = (
        ~df["이층침대"] & ~df["패밀리침대"] & ~df["모션침대"] & df["prd_nm"].str.contains("CK")
    )

    ##라지킹: '라지킹'이라는 컬럼을 만들고 '패밀리침대', '모션침대'칼럼 값이 False이고 상품명에 '라지킹' 또는 'LK'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["라지킹"] = (
        ~df["이층침대"]
        & ~df["패밀리침대"]
        & ~df["멀티싱글"]
        & ~df["슈퍼싱글"]
        & ~df["싱글"]
        & ~df["더블"]
        & ~df["퀸"]
        & (df["prd_nm"].str.contains("라지킹") | df["prd_nm"].str.contains("LK"))
    )

    ##킹: '킹'이라는 컬럼을 만들고 '패밀리침대', '모션침대', '라지킹', '칼킹' 칼럼 값이 False이고 상품명에 'CBK'가 안들어가고 '킹','k' 또는 'K' 가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["킹"] = (
        ~df["패밀리침대"]
        & ~df["모션침대"]
        & ~df["라지킹"]
        & ~df["칼킹"]
        & ~df["prd_nm"].str.contains("CBK")
        & (
            df["prd_nm"].str.contains("킹")
            | df["prd_nm"].str.contains("k")
            | df["prd_nm"].str.contains("K")
        )
    )

    ##SS+SS: 'SS+SS'이라는 컬럼을 만들고 '패밀리침대'칼럼 값이 True이고 상품명에 'SS+SS'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["SS+SS"] = (df["패밀리침대"] | df["모션침대"] | df["이층침대"]) & df["prd_nm"].str.contains(
        "SS\+SS"
    )

    ##SS+S: 'SS+S'이라는 컬럼을 만들고 '패밀리침대'칼럼 값이 True이고 'SS+SS' 컬럼 값이 False인 상품 중에 상품명에 'SS+S' 또는 'S+SS'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["SS+S"] = (
        (df["패밀리침대"] | df["모션침대"] | df["이층침대"])
        & ~df["SS+SS"]
        & (df["prd_nm"].str.contains("SS\+S") | df["prd_nm"].str.contains("S\+SS"))
    )

    ##S+S: 'S+S'이라는 컬럼을 만들고 '패밀리침대'칼럼 값이 True이고 'SS+SS' 또는 'SS+S' 컬럼 값이 False인 상품 중에 상품명에 'SS+S' 또는 'S+SS'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["S+S"] = (
        (df["패밀리침대"] | df["모션침대"] | df["이층침대"])
        & ~df["SS+SS"]
        & ~df["SS+S"]
        & df["prd_nm"].str.contains("S\+S")
    )

    ##Q+SS: 'Q+SS'이라는 컬럼을 만들고 '패밀리침대'칼럼 값이 True인 상품 중에 상품명에 'Q+SS' 또는 'SS+Q'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["Q+SS"] = (df["패밀리침대"] | df["모션침대"] | df["이층침대"]) & (
        df["prd_nm"].str.contains("Q\+SS") | df["prd_nm"].str.contains("SS\+Q")
    )

    ##Q+S: 'Q+S'라는 컬럼을 만들고 '패밀리침대'칼럼 값이 True이고 'Q+SS'칼럼 값이 False인 상품 중에 상품명에 'Q+S' 또는 'S+Q'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["Q+S"] = (
        (df["패밀리침대"] | df["모션침대"] | df["이층침대"])
        & ~df["Q+SS"]
        & (df["prd_nm"].str.contains("S\+Q") | df["prd_nm"].str.contains("Q\+S"))
    )

    ##Q+Q: 'Q+Q'라는 컬럼을 만들고 '패밀리침대'칼럼 값이 True인 상품 중에 상품명에 'Q+Q'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["Q+Q"] = (df["패밀리침대"] | df["모션침대"] | df["이층침대"]) & df["prd_nm"].str.contains(
        "Q\+Q"
    )

    ##원목: '원목' 이라는 컬럼을 만들고 '소나무,오크,나무,메이플,편백,멀바우, 아카시아, 잭파인, 버치, 우드, 참죽, 월넛, 월낫, 티크, 마호가니'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["원목"] = (
        df["prd_nm"].str.contains("원목")
        | df["prd_nm"].str.contains("오크")
        | df["prd_nm"].str.contains("나무")
        | df["prd_nm"].str.contains("메이플")
        | df["prd_nm"].str.contains("편백")
        | df["prd_nm"].str.contains("멀바우")
        | df["prd_nm"].str.contains("아카시아")
        | df["prd_nm"].str.contains("잭파인")
        | df["prd_nm"].str.contains("버치")
        | df["prd_nm"].str.contains("우드")
        | df["prd_nm"].str.contains("참죽")
        | df["prd_nm"].str.contains("월넛")
        | df["prd_nm"].str.contains("월낫")
        | df["prd_nm"].str.contains("티크")
        | df["prd_nm"].str.contains("마호가니")
        | df["prd_nm"].str.contains("소나무")
    )

    ##철제: '철제'라는 컬럼을 만들고 '철제' 또는 '스틸' 또는 '철재'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["철제"] = (
        df["prd_nm"].str.contains("철제")
        | df["prd_nm"].str.contains("스틸")
        | df["prd_nm"].str.contains("철재")
    )

    ##플라스틱: '플라스틱'이라는 컬럼을 만들고 '플라스틱' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["플라스틱"] = df["prd_nm"].str.contains("플라스틱")

    ##라탄: '라탄'이라는 컬럼을 만들고 '라탄' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["라탄"] = df["prd_nm"].str.contains("라탄")

    ##가죽: '가죽'이라는 컬럼을 만들고 '가죽' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["가죽"] = df["prd_nm"].str.contains("가죽")

    ##패브릭: '패브릭'이라는 컬럼을 만들고 '패(페)브릭' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["패브릭"] = df["prd_nm"].str.contains("패브릭") | df["prd_nm"].str.contains("페브릭")

    ##스웨이드: '스웨이드'라는 컬럼을 만들고 '스웨이드' 가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["스웨이드"] = df["prd_nm"].str.contains("스웨이드")

    ##벨벳: '벨벳'이라는 컬럼을 만들고 '벨벳'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["벨벳"] = df["prd_nm"].str.contains("벨벳")

    ##자작나무: '자작나무'이라는 컬럼을 만들고 '자작나무'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["자작나무"] = df["prd_nm"].str.contains("자작나무|버치")

    ##호두나무: '호두나무'이라는 컬럼을 만들고 '호두나무'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["호두나무"] = df["prd_nm"].str.contains("호두나무") | df["prd_nm"].str.contains("월넛|월낫")

    ##소나무: '소나무'이라는 컬럼을 만들고 '소나무'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["소나무"] = df["prd_nm"].str.contains("소나무")

    ##삼나무: '삼나무'이라는 컬럼을 만들고 '삼나무'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["삼나무"] = df["prd_nm"].str.contains("삼나무")

    ##편백나무: '편백나무'이라는 컬럼을 만들고 '편백나무'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["편백나무"] = df["prd_nm"].str.contains("편백나무")

    ##오크: '오크'이라는 컬럼을 만들고 '오크'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["오크"] = df["prd_nm"].str.contains("오크")

    ##멀바우: '멀바우'이라는 컬럼을 만들고 '멀바우'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["멀바우"] = df["prd_nm"].str.contains("멀바우")

    ##아카시아: '아카시아'이라는 컬럼을 만들고 '아카시아'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["아카시아"] = df["prd_nm"].str.contains("아카시아")

    ##참죽나무: '참죽나무'이라는 컬럼을 만들고 '참죽'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["참죽나무"] = df["prd_nm"].str.contains("참죽")

    ##마호가니: '마호가니'이라는 컬럼을 만들고 '마호가니'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["마호가니"] = df["prd_nm"].str.contains("마호가니")

    ##헤드없음: '헤드없음'이라는 컬럼을 만들고 '헤드리스'나 '무헤드'가 안들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["헤드없음"] = df["prd_nm"].str.contains("헤드리스") | df["prd_nm"].str.contains("무헤드")

    ##헤드디자인판넬형: '헤드디자인판넬형'이라는 컬럼을 만들고 '일반헤드'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["헤드디자인판넬형"] = df["prd_nm"].str.contains("일반헤드")

    ##헤드디자인쿠션형: '헤드디자인쿠션형'이라는 컬럼을 만들고 '쿠션헤드'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["헤드디자인쿠션형"] = df["prd_nm"].str.contains("쿠션헤드")

    ##헤드디자인확장형: '헤드디자인확장형'이라는 컬럼을 만들고 '헤드'랑 '확장'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["헤드디자인확장형"] = df["prd_nm"].str.contains("헤드") & df["prd_nm"].str.contains("확장")

    ##헤드디자인수납형: '헤드디자인수납형'이라는 컬럼을 만들고 '헤드'랑 '수납'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["헤드디자인수납형"] = df["prd_nm"].str.contains("헤드") & df["prd_nm"].str.contains("수납")

    ##프레임형태통깔판형: '프레임형태통깔판형'이라는 컬럼을 만들고 '프레임'이 들어가고 '평상', '통판', 또는 '통마루'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["프레임형태통깔판형"] = df["prd_nm"].str.contains("프레임") & (
        df["prd_nm"].str.contains("평상")
        | df["prd_nm"].str.contains("통판")
        | df["prd_nm"].str.contains("통마루")
    )

    ##프레임형태갈빗살형: '프레임형태갈빗살형'이라는 컬럼을 만들고 '프레임'이랑 '갈빗'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["프레임형태갈빗살형"] = df["prd_nm"].str.contains("프레임") & df["prd_nm"].str.contains("갈빗")

    ##프레임형태에어홀깔판형: '프레임형태에어홀깔판형'이라는 컬럼을 만들고 '프레임'이 들어가고 'PVC', 또는 'AIR'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["프레임형태에어홀깔판형"] = df["prd_nm"].str.contains("프레임") & (
        df["prd_nm"].str.contains("PVC") | df["prd_nm"].str.contains("AIR")
    )

    ##프레임형태파운데이션: '프레임형태파운데이션'이라는 컬럼을 만들고 '파운데이션침대' 컬럼이 True인 로우에는 True 안들어가는 로우에는 False 넣기
    df["프레임형태파운데이션"] = df["prd_nm"].str.contains("파운데이션")

    ##밀림방지: '밀림방지'이라는 컬럼을 만들고 '밀림방지'이 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["밀림방지"] = df["prd_nm"].str.contains("밀림방지")

    ##높이조절: '높이조절'이라는 컬럼을 만들고 '높이조절'이 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["높이조절"] = df["prd_nm"].str.contains("높이조절")

    ##USB: 'USB'이라는 컬럼을 만들고 'USB'이 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["USB"] = df["prd_nm"].str.contains("USB")

    ##블루투스스피커: '블루투스스피커'이라는 컬럼을 만들고 '스피커'이 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["블루투스스피커"] = df["prd_nm"].str.contains("스피커|블루투스")

    ##조명포함: '조명포함'이라는 컬럼을 만들고 'LED' 또는 '조명'이 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["조명포함"] = df["prd_nm"].str.contains("LED") | df["prd_nm"].str.contains("조명")

    ##안전가드포함: '안전가드포함'이라는 컬럼을 만들고 '가드', '둥지', 'ㄷ형' 또는 '범퍼'가 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["안전가드포함"] = (
        df["prd_nm"].str.contains("가드")
        | df["prd_nm"].str.contains("둥지")
        | df["prd_nm"].str.contains("ㄷ형")
        | df["prd_nm"].str.contains("범퍼")
    )

    ##바퀴포함: '바퀴포함'이라는 컬럼을 만들고 '바퀴' 또는 '이동'이 들어가는 로우에 True 안들어가는 로우에는 False 넣기
    df["바퀴포함"] = df["prd_nm"].str.contains("바퀴") | df["prd_nm"].str.contains("이동")

    ##수동형: '수동형'라는 컬럼을 만들고'수동'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["수동형"] = df["prd_nm"].str.contains("수동")

    ##전동형: '전동형'라는 컬럼을 만들고'전동'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["전동형"] = df["prd_nm"].str.contains("전동")

    ##무중력자세: '무중력자세'라는 컬럼을 만들고'무중력'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["무중력자세"] = df["prd_nm"].str.contains("무중력")

    ##메트리스포함: '메트리스포함'라는 컬럼을 만들고'세트'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["메트리스포함"] = df["prd_nm"].str.contains("세트|메트리스포함")

    ##메트리스미포함: '메트리스미포함'라는 컬럼을 만들고'프레임만'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["메트리스미포함"] = df["prd_nm"].str.contains("프레임만|메트리스미포함")

    ##독립스프링: '독립스프링'라는 컬럼을 만들고'독립'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["독립스프링"] = df["prd_nm"].str.contains("독립")

    ##본넬스프링: '본넬스프링'이라는 컬럼을 만들고'본넬'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["본넬스프링"] = df["prd_nm"].str.contains("본넬")

    ##라텍스: '라텍스'이라는 컬럼을 만들고'라텍스'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["라텍스"] = df["prd_nm"].str.contains("라텍스")

    ##메모리폼: '메모리폼'이라는 컬럼을 만들고'메모리'이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["메모리폼"] = df["prd_nm"].str.contains("메모리")

    ##벙커침대책상형: '벙커침대책상형'이라는 컬럼을 만들고'벙커침대'컬럼이 True이고 상품명에 '책상' 또는 '데스크'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["벙커침대책상형"] = df["벙커침대"] & (
        df["prd_nm"].str.contains("책상") | df["prd_nm"].str.contains("데스크")
    )

    ##벙커침대수납형: '벙커침대수납형'이라는 컬럼을 만들고'벙커침대'컬럼이 True이고 상품명에 '수납' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["벙커침대수납형"] = df["벙커침대"] & df["prd_nm"].str.contains("수납")

    ##벙커침대계단형: '벙커침대계단형'이라는 컬럼을 만들고'벙커침대'컬럼이 True이고 상품명에 '계단' 이 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["벙커침대계단형"] = df["벙커침대"] & df["prd_nm"].str.contains("계단")

    ##벙커침대옷장형: '벙커침대옷장형'이라는 컬럼을 만들고'벙커침대'컬럼이 True이고 상품명에 '기본행거' 또는 '드레스'가 들어가는 로우에는 True 안들어가는 로우에는 False 넣기
    df["벙커침대옷장형"] = df["벙커침대"] & (
        df["prd_nm"].str.contains("기본행거") | df["prd_nm"].str.contains("드레스")
    )

    return df
