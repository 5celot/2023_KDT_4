"""
# URL : http://localhost:8080/cgi-bin/solo_soonja.py
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
        <title>순자</title>
        <link type="text/css" rel="stylesheet" href="webpage.css">
        <style>
            @font-face {
                        font-family: 'MAKGEOLLI.ttf';
                        src: url('/solo/MAKGEOLLI.ttf') format('truetype');
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
                background: url('/solo/background.jpg');
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

            /* 순자 */
            .sja1{
                position:relative;
                left:100px;
                top:200px;
            }

            .sja2{
                position:relative;
                left:100px;
                top:200px;
            }

            .sja3{
                position:relative;
                left:100px;
                top:200px;
            }

            .sja4{
                position:relative;
                left:100px;
                top:200px;
            }

            .sja5{
                position:relative;
                left:100px;
                top:200px;
            }

            .sja6{
                position:relative;
                left:100px;
                top:200px;
            }

            .sja7{
                position:relative;
                left:100px;
                top:200px;
            }


        </style>
        
    </head>
    
    <body>
        <!-- 1page -->
        
        <div id="back">
            
            <div class="main">

                <div class="home">
                    <a href="홈 페이지의 URL을 여기에 넣으세요">
                        <img class="home" src="/solo/homebutton.png" width="400px" height="300px">
                    </a>
                </div>

                <img class="img" src="/solo/soonja/soonjajukja.png" width=260px height=870px>
                <div class="moto2"><img class="img" src="/soonja_main.jfif" width=500px height=500px></div>
                
                <div class="historytitle">두 둥 !</div>
                <div class="history">당신은 나는솔로 17기 <span class="name">순자</span> 입니다.</div>

            </div>

            <!-- 2page -->
            <div class="main">

                <p style="font-size: 24px;"><br></p>
                <p class="home1">
                    <a href="홈 페이지의 URL을 여기에 넣으세요">
                        <img class="home" src="/solo/homebutton.png" width="400px" height="300px">
                    </a>
                </p>
                <p class="qnatitle">특  징</p>
                <img class="contentsImg" src="/solo/jukja.png" width="1470" height="750" style="position: relative; left: 190px; top: 30px">
                <p class="contents">순자는 시크하고 도시적인 외모를 가졌습니다.<br>
                    도도하고 세련된 고양이상의 여성이 많습니다.<br>
                    성격 또한 솔직한 매력이 넘치는 여성입니다.<br><br>
                    
                    솔로나라의 앙큼한 냥냥이, 순자의 꾹꾹이를 받아라옹</p>

            </div>


            <!-- 3page -->
            <div class="main">

                <p class="home2">
                    <a href="홈 페이지의 URL을 여기에 넣으세요">
                        <img class="home2" src="/solo/homebutton.png" width="400px" height="300px">
                    </a>
                </p>

                <div style="position: relative; width:100%; height:100%; pointer-events: none;"> 
                    <img class="sja2" src="/solo/soonja/순자 (1).png" style="position:absolute; top:200px; left:100px;" width="800">
                    <img class="sja3" src="/solo/soonja/순자 (1).webp" style="z-index: 2; transform: rotate(350deg); position:absolute; left:200px; top:650px" width="700">
                    <img class="sja4" src="/solo/soonja/순자 (2).jpg" style="z-index: 1; position:absolute; top:100px; left:950px;" height="500px" width="800">
                    <img class="sja6" src="/solo/soonja/순자 (4).jpg" style="position:absolute; left:780px; top:580px; z-index: 3;" height="300">
                    <img class="sja7" src="/solo/soonja/순자 (5).jpg" style="position:absolute; top:600px; left:1000px;" width="800">
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