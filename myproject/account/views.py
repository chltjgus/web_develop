from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to account!</h1>")

def about(request):
    return HttpResponse("<h1>About page</h1>")

def homePage(request):
    return HttpResponse("<h1>Home<h1>")

def testHome(request, first:int, second=None):
    sum = first + second

    #zip 사용해보기
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    zipdata = zip(data1, data2)

    # second의 default값을 정해주는 방법도 있음
    if second is None:
        second = 0

    # 오늘 날짜와 달
    import datetime
    now = datetime.datetime.now().day
    nowMonth = datetime.datetime.now().month

    #삼항 연산자로 해결(boolean으로 넘겨야 나중에 template 관리하기 편함)
    date = True if now % 2 == 0 else False
    month = True if nowMonth % 2 == 0 else False
    #    date = "짝수" if now % 2 == 0 else "홀수"
    #    month = "짝수" if nowMonth % 2 == 0 else "홀수"

    gugudan = []
    for i in range(2, 10, 1):
        for j in range(1, 10, 1):
            if i % 2 == 0:
                gugudan.append((i, j, i*j, True))
            else:
                gugudan.append((i, j, i*j, False))

    string = "django is awesome!!"

    #sum을 또 dict로 만들어서 넣어주는 방법도 좋은 설계
    context = {
        "name": "홍길동",
        "age": 40,
        "date": date,
        "mul_data": 0.5,
        "month": month,
        "first": first,
        "second": second,
        "sum": {
            "first": first,
            "second": second,
            "sum": sum
            },
        "data": {
            "item_list": [(2, 1, 2), (2, 2, 4), (2, 3, 6), (2, 4, 8), (2, 5, 10), (2, 6, 12), (2, 7, 14), (2, 8, 16), (2, 9, 18)],
        },
        "zipdata":zipdata,
        "gugudan": gugudan,
        "string": string,

     }

    return render(request, "index.html", context)




# def testDate(request, year=None, month=None, day=None):
#
#     text = 'OKAY'
#
#     if year is None or month is None or day is None:
#         text = 'INVALID'
#
#     context = {
#         "year": year,
#         "month": month,
#         "day": day,
#         "text": text,
#     }
#
#     return render(request, "index.html", context)


def extend(request):


    context = {
        "string":"Hello",
    }

    return render(request, "base.html", context)


def extend2(request):
    context = {
        "string": "Hello",
    }

    return render(request, "home.html", context)