"""
# URL : http://localhost:8080/cgi-bin/solo_kwangsoo.py
"""
# python -m http.server --cgi 8080
# 모듈 로딩 ---------------------------------------------------
import cgi, sys, codecs, os
from pydoc import html


# WEB 인코딩 설정 ---------------------------------------------
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

# 함수 선언 --------------------------------------------------
# WEB 페이지 출력 --------------------------------------------
def display_main():
    print("Content-Type: text/html; charset=utf-8")
    print('''
<!DOCTYPE html>
<html>
    <head>
        <title>광수</title>
        <link type="text/css" rel="stylesheet" href="webpage.css">
        <style>
            @font-face {
                        font-family: 'MAKGEOLLI.ttf';
                        src: url('../solo/MAKGEOLLI.ttf') format('truetype');
                        font-weight: normal;
                        font-style: normal;
                }
            body{margin:0px;
                padding:0px;
                overflow: hidden;
                color:white;
                font-family: 'MAKGEOLLI.ttf'
                
            }
            #back{
                position: relative;;
                overflow: auto;
                background: url('../solo/background.jpg');
                height: 100vh; 
                margin: 0;
                scroll-behavior: smooth;
                scroll-snap-type: y mandatory;
                /* display: flex; */
            }
            .main{
                scroll-snap-align: center;
                height: 100vh;
            }



            /* 1page */
            .img{ 
                position: absolute;
                z-index:2;
                top:100px;
                left:450px;
                box-shadow: 10px 10px 10px #575151;
                background-repeat: no-repeat;
                border-radius: 0.3cm;
            }

            .home{ 
                position: absolute;
                z-index:2;
                top:0px;
                left:0px;
                background-repeat: no-repeat;
                border-radius: 0.3cm;
            }

            .moto2{
                position:absolute;
                color:white;
                font-size:100px;
                left:500px;
                top:100px;    
            }

            .historytitle{
                position:absolute;
                color:black;
                font-size:70px;
                left:1155px;
                top:750px;
            }

            .history{
                color:black;
                top:850px;
                font-size:60px;
                position: absolute;
                left:900px
            }

            .name{
                color:black;
                text-shadow: 10px 10px 10px #575151;
                background-repeat: no-repeat;
                border-radius: 0.3cm;
                font-size:70px;
            }


            /* 2page */
            .qnatitle {
                text-align: center;
                text-decoration-line: underline;
                font-size:100px;
                color: white;
                height: 90px;
                margin-top: 0px;
                text-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
            }

            .contentsImg{
                box-shadow: 10px 10px 10px #575151;
                background-repeat: no-repeat;
                border-radius: 0.3cm;
            }

            .contents{
                color:black;
                top:1450px;
                font-size:60px;
                position: absolute;
                left:300px
            }

            .contents1{
                color:black;
                top:1400px;
                font-size:60px;
                position: absolute;
                left:300px
            }

            .home1{
                top:1070px;
                position: absolute;
                left:5px
            }



            /* 3page */
            .home2{
                top:1070px;
                position: absolute;
                left:5px
            }

            /* 광수 */
            .ksoo1{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo2{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo3{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo4{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo5{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo6{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo7{
                position:relative;
                left:100px;
                top:200px;
            }

            .ksoo8{
                position:relative;
                left:100px;
                top:200px;
            }
        </style>
        
    </head>
    
    <body>
        <div id="back">

            <!-- 1page -->
            <div class="main">

                <div class="home">
                    <a href="홈 페이지의 URL을 여기에 넣으세요">
                        <img class="home" src="../solo/homebutton.png" width="400px" height="300px">
                    </a>
                </div>

                <img class="img" src="../solo/kwangsoo/kwangsoojukja.png" width=260px height=870px>
                <div class="moto2"><img class="img" src="/kwangsoo_main.png" width=500px height=500px></div>
                
                <div class="historytitle">두 둥 !</div>
                <div class="history">당신은 나는솔로 17기 <span class="name">광수</span> 입니다.</div>

            </div>

            <!-- 2page -->
            <div class="main">

                <p style="font-size: 24px;"><br></p>
                <p class="home1">
                    <a href="홈 페이지의 URL을 여기에 넣으세요">
                        <img class="home" src="../solo/homebutton.png" width="400px" height="300px">
                    </a>
                </p>
                <p class="qnatitle">특  징</p>
                <img class="contentsImg" src="../solo/jukja.png" width="1470" height="750" style="position: relative; left: 190px; top: 30px">
                <p class="contents">출연자들의 스펙과 배경이 대체로 좋은 편이긴 하지만<br>
                    이들중에서도 으뜸은 단연 광수라고 말할 수 있습니다.<br>
                    엘리트의 분위기와 포스가자연스럽게 따라오는 광수는 <br>
                    언제나 인기만점!<br><br>
                    여심공략전문가, 재간둥이 광수의 매력을 마음껏 뽐내세요!</p>

            </div>

            <!-- 3page -->
            <div class="main">

                <p class="home2">
                    <a href="홈 페이지의 URL을 여기에 넣으세요">
                        <img class="home2" src="../solo/homebutton.png" width="400px" height="300px">
                    </a>
                </p>

                <div style="position: relative; width:100%; height:100%; pointer-events: none;"> 
                    <img class="ksoo1" src="../solo/kwangsoo/광수 (1).jfif" style="position:absolute; top:200px; left:100px;" width="800">
                    <img class="ksoo2" src="../solo/kwangsoo/광수 (1).PNG" style="z-index: 2; transform: rotate(350deg); position:absolute; left:200px; top:650px" width="700">
                    <img class="ksoo5" src="../solo/kwangsoo/광수 (3).jfif" style="z-index: 1; position:absolute; top:100px; left:900px;" height="500px">
                    <img class="ksoo6" src="../solo/kwangsoo/광수 (3).PNG" style="position:absolute; left:750px; top:400px; z-index: 3;" width="500">
                    <img class="ksoo7" src="../solo/kwangsoo/광수 (4).PNG" style="position:absolute; top:650px; left:1000px; z-index: 4;" width="800">
                </div>
            </div>



        </div>
    </body>
</html>

''')




# 이미지 처리 --------------------------------------------------


  

# (4) WEB 출력하기
# displayWEB(result)
display_main()


# if(gender_value=="남"):
#     print("<script> location.href='/cgi-bin/bmi-web.py'; </script>")
# else:
#     display_main(tv)