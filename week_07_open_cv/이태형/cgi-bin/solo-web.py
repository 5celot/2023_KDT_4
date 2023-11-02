"""
# URL : http://localhost:8080/cgi-bin/solo-web.py
"""
# python -m http.server --cgi 8080
# 모듈 로딩 ---------------------------------------------------
import cgi, sys, codecs, os
from pydoc import html
import cv2
from rembg import remove
import numpy as np
import joblib
import pandas as pd

# WEB 인코딩 설정 ---------------------------------------------
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

# 함수 선언 --------------------------------------------------
# WEB 페이지 출력 --------------------------------------------
def display_main(tv=''):
    print("Content-Type: text/html; charset=utf-8")
    print(f'''
<!DOCTYPE html>
<html lang="en">
<head>

    <title>Document</title>
    <link type="text/css" rel="stylesheet" href="/main.css?12">
    

</head>
<body>
    <div id="back">
        <!--메인 페이지-->
        <div class="main">
            
            <!--헤더-->
            <header id="team">
                 
                    <a class="teammates" href="main.html#sec0" class="header-text">출연진</a><br/>
                <div id="jocja">   
                    <p></p>
                    <br>
                    <br>
                    <br>
                    <br>
                    
                    <a href="#container1" class="header-text"><em>영수</em></a><br/>
                    <p></p>
                    <a href="#container2" class="header-text"><em>영호</em></a><br/>
                    <p></p>
                    <a href="#container3" class="header-text"><em>영식</em></a><br/>
                    <p></p>
                    <a href="#container4" class="header-text"><em>영철</em></a><br/>
                    <p></p>
                    <a href="#container5" class="header-text"><em>광수</em></a><br/>
                    <p></p>
                    <a href="#container6" class="header-text"><em>상철</em></a><br/>
                    <p></p>
                    <a href="#container7" class="header-text"><em>영숙</em></a><br/>
                    <p></p>
                    <a href="#container8" class="header-text"><em>정숙</em></a><br/>
                    <p></p>
                    <a href="#container9" class="header-text"><em>순자</em></a><br/>
                    <p></p>
                    <a href="#container10" class="header-text"><em>영자</em></a><br/>
                    <p></p>
                    <a href="#container11" class="header-text"><em>옥순</em></a><br/>
                    <p></p>
                    <a href="#container12" class="header-text"><em>현숙</em></a><br/>
                    <p></p>
                    <a href="#container12" class="header-text"><em></em></a><br/>
                    <p></p>
                    <a href="#container12" class="header-text"><em></em></a><br/>
                    <br/>
                    
                </div>
            </header>


            <footer>
                <div id="mainImg">
                
                </div>
            </footer>
        </div>
        



        <!--1 페이지-->
        <div class="main">
            <div id="container1">
                <figure align="center">
                    <a href="youngsoo_web.html" target="_blank" id="hvr1"></a>
                    <figcaption align="center">
                        <br/>
                        재력과 여유의 집합체
                    </figcaption>
                </figure>
            </div>
        </div>


        <!--2 페이지-->
        <div class="main">
            <div id="container2">
                <figure align="center">
                    <a href="#" target="_blank" id="hvr2"></a>
                    <figcaption align="center">
                        <br/>
                        요즘 대세는 초식남
                    </figcaption>
                </figure>
            </div>
        </div>


        <!--3 페이지-->
        <div class="main">
            <div id="container3">
                <figure align="center">
                    <a href="#" target="_blank" id="hvr3"></a>
                    <figcaption align="center">
                        <br/>
                        남자의 외모는 능력
                    </figcaption>
                </figure>
            </div>
        </div>


        <!--4 페이지-->
        <div class="main">
            <div id="container4">
                <figure align="center">
                    <a href="#" target="_blank" id="hvr4"></a>
                    <figcaption align="center">
                        <br/>
                        남자중의 남자 직진남
                    </figcaption>
                </figure>
            </div>
        </div>

        
        <!--5 페이지-->
        <div class="main">
            <div id="container5">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr5"></a>
                    <figcaption align="center">
                        <br/>
                        프로페셔널한 섹시미
                    </figcaption>
                </figure>
            </div>
        </div>

        <!--6 페이지-->
        <div class="main">
            <div id="container6">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr6"></a>
                    <figcaption align="center">
                        <br/>
                        기대고싶은 듬직한 남자
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--7 페이지-->
        <div class="main">
            <div id="container7">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr7"></a>
                    <figcaption align="center">
                        <br/>
                        커리어우먼의 열정
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--8 페이지-->
        <div class="main">
            <div id="container8">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr8"></a>
                    <figcaption align="center">
                        <br/>
                        세심한 배려와 안정감
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--9 페이지-->
        <div class="main">
            <div id="container9">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr9"></a>
                    <figcaption align="center">
                        <br/>
                        솔직하고 도도한 그녀
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--10 페이지-->
        <div class="main">
            <div id="container10">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr10"></a>
                    <figcaption align="center">
                        <br/>
                        귀여움으로 무장해제
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--11 페이지-->
        <div class="main">
            <div id="container11">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr11"></a>
                    <figcaption align="center">
                        <br/>
                        나는 솔로의 대표 미인
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--12 페이지-->
        <div class="main">
            <div id="container12">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr12"></a>
                    <figcaption align="center">
                        <br/>
                        편안하고 밝은 매력
                    </figcaption>
                </figure>
            </div>
        </div>
        <!--13 페이지-->
        <div class="main">
            <div id="container13">
                <figure align="center">
                    <a href="taehyoungProfile.html" target="_blank" id="hvr13"></a>
                    <figcaption align="center">
                        <br/>
    
                        <form action="/cgi-bin/solo-web.py" method="post" enctype="multipart/form-data">
                            <div style='text-align:center; background-color:#a28888;border-radius:10px;width:60%; margin: auto;padding:50px;'>
                                <input id="gender" type="text" placeholder="성별입력 : 남 / 여" name="gender">
                                <input id="image" type="file" id="myFile" name="image">
                                <input type="submit" value="결과싹볼TV"></br>
                                <p><font color='blue'>{tv}</font></p>
                                <p><font color='blue'></font></p>
                                
                            </div>
                        </form>
                    </figcaption>
                </figure>
            </div>
        </div>


    
    </div>


</body>

</html>
''')




# 이미지 처리 --------------------------------------------------

def userImg(img_va):
    filename=img_va
    # [2] 이미지 배경제거 후 사이즈 조절
    dsize_=(340,160)
    arr = np.frombuffer(filename, np.uint8)
    org = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(org, dsize_)
    output=remove(img)
    gray = cv2.cvtColor(output, cv2.COLOR_RGBA2GRAY)
    gray=gray.reshape(-1)
    img_df=pd.DataFrame([gray])

    return img_df




# 판정 --------------------------------------------------------



def detect_solo(gender_value,img_v):
    img=userImg(img_v)  # 위 이미지처리 함수
    if gender_value=='남':
        solo_man=man_clf.predict(img)[0]
        return solo_man # 숫자 1~6
    elif gender_value=='여':
        solo_woman=woman_clf.predict(img)[0]
        return solo_woman # 숫자 1~6

   
    



# 기능 구현 -----------------------------------------------------
# (1) 학습 데이터 읽기


man_pklfile = os.path.dirname(__file__) + "/man.pkl"
man_clf = joblib.load(man_pklfile)

woman_pklfile = os.path.dirname(__file__) + "/woman.pkl"
woman_clf = joblib.load(woman_pklfile)

# (2) WEB 페이지 <Form> -> <INPUT> 리스트 가져오기
form = cgi.FieldStorage()


gender_value = form.getvalue('gender')
if 'image' in form:
    img_field = form['image']
    img_value = img_field.file.read()

# (3) 판정 하기
if gender_value is not None and img_value is not None:
    if gender_value=="남" and detect_solo(gender_value,img_value)==1:     #영수
        tv='영수'
    elif gender_value=="남" and detect_solo(gender_value,img_value)==2:     #영호
        tv='영호'
    elif gender_value=="남" and detect_solo(gender_value,img_value)==3:     #영식
        tv='영식'
    elif gender_value=="남" and detect_solo(gender_value,img_value)==4:     #영철
        tv='영철'
    elif gender_value=="남" and detect_solo(gender_value,img_value)==5:     #광수
        tv='광수'
    elif gender_value=="남" and detect_solo(gender_value,img_value)==6:     #상철
        tv='상철'
    elif gender_value=="여" and detect_solo(gender_value,img_value)==1:     #영숙
        tv='영숙'
    elif gender_value=="여" and detect_solo(gender_value,img_value)==2:     #정숙
        tv='정숙'
    elif gender_value=="여" and detect_solo(gender_value,img_value)==3:     #순자
        tv='순자'
    elif gender_value=="여" and detect_solo(gender_value,img_value)==4:     #영자
        tv='영자'
    elif gender_value=="여" and detect_solo(gender_value,img_value)==5:     #옥순
        tv='옥순'
    elif gender_value=="여" and detect_solo(gender_value,img_value)==6:     #현숙
        tv='현숙'
else:
    tv=''


  

# (4) WEB 출력하기
# displayWEB(result)
display_main(tv)


# if gender_value=="남" and detect_solo(gender_value,img_value)==1:     #영수
#     print("<script> location.href='/cgi-bin/solo_youngsoo.py'; </script>")
# elif gender_value=="남" and detect_solo(gender_value,img_value)==2:     #영호
#     print("<script> location.href='/cgi-bin/solo_youngho.py'; </script>")
# elif gender_value=="남" and detect_solo(gender_value,img_value)==3:     #영식
#     print("<script> location.href='/cgi-bin/solo_youngsik.py'; </script>")
# elif gender_value=="남" and detect_solo(gender_value,img_value)==4:     #영철
#     print("<script> location.href='/cgi-bin/solo_youngchul.py'; </script>")
# elif gender_value=="남" and detect_solo(gender_value,img_value)==5:     #광수
#     print("<script> location.href='/cgi-bin/solo_kwangsoo.py'; </script>")
# elif gender_value=="남" and detect_solo(gender_value,img_value)==6:     #상철
#     print("<script> location.href='/cgi-bin/solo_sangchul.py'; </script>")
# elif gender_value=="여" and detect_solo(gender_value,img_value)==1:     #영숙
#     print("<script> location.href='/cgi-bin/solo_youngsook.py'; </script>")
# elif gender_value=="여" and detect_solo(gender_value,img_value)==2:     #정숙
#     print("<script> location.href='/cgi-bin/solo_jungsook.py'; </script>")
# elif gender_value=="여" and detect_solo(gender_value,img_value)==3:     #순자
#     print("<script> location.href='/cgi-bin/solo_soonja.py'; </script>")
# elif gender_value=="여" and detect_solo(gender_value,img_value)==4:     #영자
#     print("<script> location.href='/cgi-bin/solo_youngja.py'; </script>")
# elif gender_value=="여" and detect_solo(gender_value,img_value)==5:     #옥순
#     print("<script> location.href='/cgi-bin/solo_oksoon.py'; </script>")
# elif gender_value=="여" and detect_solo(gender_value,img_value)==6:     #현숙
#     print("<script> location.href='/cgi-bin/solo_hyunsook.py'; </script>")

# else:
#     display_main(tv)
