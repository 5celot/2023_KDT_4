from flask import Flask, render_template,request
import os
from konlpy.tag import Kkma
import mariadb as mdb
import pandas as pd
import numpy as np
from tqdm import tqdm
import folium
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Okt

app = Flask(__name__)


def generate_result(search):

    emo=pd.read_csv('EXAM_09_SQL\MINI\myproject\static\블로그감성분석.csv')



    cv=CountVectorizer()
    dtm = cv.fit_transform(emo['data'])
    dtm_df = pd.DataFrame(dtm.toarray(), columns=cv.get_feature_names_out())

    # 코사인 유사도 : 두 벡터 사이의 각도의 코사인 값 ( -1 ~ 1 )
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)) # a, b의 내적
    # text='엑티비티하고 재미있는 놀이공원'

    text='너무 힘들다 힐링이 필요해 휴양지 추천해줘'

    kkma = Kkma()
    target=kkma.nouns(search)
    target=' '.join(target)


    target=[search +" " + target]
    nor_target = cv.transform(target)
    nor_target.toarray()[0]

    box=[]
    for i in range(len(dtm_df)):
        sample = dtm_df.iloc[i].to_numpy()
        cosine = make_cosine(nor_target.toarray()[0],sample)
        box.append(cosine)
        
    emo['유사도분석']=box
    final_result=emo.sort_values(by=['유사도분석'],ascending=[False])
    keyword = final_result[final_result.감성분석결과 == 1].검색키워드.iloc[0]
    keyword





    # 테이블 데이터 확인
    conn_params={'host':'localhost',
                'port':3306,
                'user':'root',
                'password':'root',
                'autocommit':True,
                'db':'place'}

    try:
        # mariadb연결
        conn=mdb.connect(**conn_params)

        # db에 접근할 수 있는 cursor객체 가져오기
        cur=conn.cursor()

        # 식당 조회하는 sql실행
        cur.execute("SELECT r.r_name,r.r_star,r.r_latitude, r.r_longitude, e.e_latitude, e.e_longitude, round((6371 * acos(cos(radians(e.e_latitude)) * cos(radians(r.r_latitude)) * cos(radians(r.r_longitude) - radians(e.e_longitude)) + sin(radians(e.e_latitude)) * sin(RADIANS(r.r_latitude)))),0) AS distance FROM restaurant AS r, (SELECT e_latitude, e_longitude from entertain WHERE e_name=?) AS e ORDER BY DISTANCE ASC, r.r_star DESC LIMIT 5;",[keyword])
        # 식당 조회 결과
        tableList=cur.fetchall()

        # 카페 조회하는 sql실행
        cur.execute("SELECT c.c_name,c.c_star,c.c_latitude, c.c_longitude, e.e_latitude, e.e_longitude, round((6371 * acos(cos(radians(e.e_latitude)) * cos(radians(c.c_latitude)) * cos(radians(c.c_longitude) - radians(e.e_longitude)) + sin(radians(e.e_latitude)) * sin(RADIANS(c.c_latitude)))),0) AS distance FROM cafe AS c, (SELECT e_latitude, e_longitude from entertain WHERE e_name=?) AS e ORDER BY DISTANCE ASC, c.c_star DESC LIMIT 5;",[keyword])
        # 카페 조회 결과
        cafeList=cur.fetchall()

        cur.execute("SELECT n.e_name,n.positive,n.e_latitude, n.e_longitude, e.e_latitude, e.e_longitude, round((6371 * acos(cos(radians(e.e_latitude)) * cos(radians(n.e_latitude)) *cos(radians(n.e_longitude) - radians(e.e_longitude))+ sin(radians(e.e_latitude)) * sin(RADIANS(n.e_latitude)))),0) AS distance FROM entertain AS n, (SELECT e_latitude, e_longitude from entertain WHERE e_name=?) AS e ORDER BY n.positive DESC, DISTANCE LIMIT 5;",[keyword])
        # 조회 결과
        entertain=cur.fetchall()




        cur.close()
        conn.close()
    except mdb.Error as e:
        print(f'Error : {e}')
        
        
    # 지도 중심 좌표 설정
    location = [tableList[0][4], tableList[0][5]]
    m = folium.Map(location=location, zoom_start=13)



    # 주변 맛집 파란 마커 추가
    for i in range(len(tableList)):
        popup = folium.Popup(f'<p style="width:200px">{tableList[i][0]}</p>', max_width=200)
        folium.Marker(
        location=[tableList[i][2], tableList[i][3]],
        icon=folium.Icon(color='blue'),
        popup=popup    
    ).add_to(m)
        
    # 주변 카페 초록 마커 추가
    for i in range(len(cafeList)):
        popup = folium.Popup(f'<p style="width:200px">{cafeList[i][0]}</p>', max_width=200)
        folium.Marker(
        location=[cafeList[i][2], cafeList[i][3]],
        icon=folium.Icon(color='green'),
        popup=popup    
    ).add_to(m)
        
    # 주변 놀곳 노랑 마커 추가
    for i in range(len(entertain)):
        popup = folium.Popup(f'<p style="width:200px">{entertain[i][0]}</p>', max_width=200)
        folium.Marker(
        location=[entertain[i][2], entertain[i][3]],
        icon=folium.Icon(color='orange'),
        popup=popup    
    ).add_to(m)



    # 중심 빨간색 마커 추가
    folium.Marker(
        location=location,
        icon=folium.Icon(color='red')
    ).add_to(m)

        
    

    m.save('EXAM_09_SQL\MINI\myproject\static\map\map.html')



    okt = Okt()
    senti = pd.read_csv('EXAM_09_SQL\MINI\myproject\static\knu_sentiment_lexicon.csv')


    def gamsung(text):
        t = okt.normalize(text)
        score = 0
        feel = '긍정'
        for w,p in zip(senti['word'], senti['polarity']):
            score += t.count(w) * p
        if score < 0:
            feel = '부정'
        return score, feel
    
    gams=gamsung(search)
    
    
    return [keyword,tableList,cafeList,entertain,gams]




    

@app.route('/', methods=['GET', 'POST'])
def generate():
    txt0=None
    search=None
    html=None
    jumsu=None


  
    if request.method == 'POST':
        search = request.form['url']
        
        try:
            table=generate_result(search)
            table_List=table[1]
            jumsu=table[4][0]

            txt0=table[0]



            # 만약 이미지 파일들이 존재한다면, 해당 파일들의 경로를 템플릿으로 전달합니다.
            if os.path.exists(r'EXAM_09_SQL\MINI\myproject\static\map\map.html'):
                html = '..\static\map\map.html'




                
        except Exception as e:
            return str(e)
    
    return render_template('index.html', txt0=txt0,html=html,search=search,jumsu=jumsu )



if __name__ == '__main__':
     app.run(debug=True)
