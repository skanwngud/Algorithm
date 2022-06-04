import csv

f = open('result.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)


def que():
    question = "CU"
    question1 = "씨큐프라임"
    question2 = "이스턴웰스_보라매"
    question3 = "심플리파이_글레즈하임호텔"
    question4 = "이마트24"
    question5 = "GS"
    question6 = "비트"

    df = []
    df1 = []
    df2 = []
    df3 = []
    df4 = []
    df5 = []
    df6 = []

    for read in rdr:
        for read2 in read:
            if question in read2:
                df.append(read2)
            if question1 in read2:
                df1.append(read2)
            if question2 in read2:
                df2.append(read2)
            if question3 in read2:
                df3.append(read2)
            if question4 in read2:
                df4.append(read2)
            if question5 in read2:
                df5.append(read2)
            if question6 in read2:
                df6.append(read2)

    cu = len(df)
    cq_prime = len(df1)
    esternwells = len(df2)
    simplypie = len(df3)
    emart24 = len(df4)
    gs = len(df5)
    beat = len(df6)

    all = cu + cq_prime + esternwells + simplypie + emart24 + gs + beat

    