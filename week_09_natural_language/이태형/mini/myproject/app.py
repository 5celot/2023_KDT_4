from flask import Flask, render_template,request
from bs4 import BeautifulSoup
from tqdm import tqdm # for문의 진행상황 확인
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests # 페이지 요청
import pandas as pd
import time
import random
from tqdm import tqdm
from konlpy.tag import Okt
import seaborn as sns
import koreanize_matplotlib
import matplotlib.pyplot as plt
from konlpy.tag import Kkma
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageDraw, ImageFont


app = Flask(__name__)

def generate_images(url):
    # 여기에 주어진 URL에 대해 크롤링 및 이미지 생성 과정을 수행하는 코드를 넣으세요.
    # 제공된 코드를 참조하여 필요한 부분을 복사/붙여넣기 하고 적절히 수정하세요.
    # 마지막에는 아래와 같이 이미지를 저장하세요:
    #
    # sns.countplot(data=df,x='리뷰분석')
    # plt.savefig('static/image1.png')
    if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image1.png'):
        os.remove(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image1.png')
    if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image2.png'):
        os.remove(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image2.png')
    if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image3.png'):
        os.remove(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image3.png')
    if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image4.png'):
        os.remove(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image4.png')

    driver=webdriver.Chrome()
    driver.get(url)

    driver.implicitly_wait(10)
    time.sleep(3)


    # 초기 위치 설정 
    position = 0

    while True:
        # 스크롤 다운
        driver.execute_script(f"window.scrollTo(0, {position});")
        
        # 페이지 로딩 대기 및 위치 증가
        position += 600
        time.sleep(0.2)

        # 새로운 높이 가져오고 비교하기 
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if position >= new_height:
            break



    # 포토&동영상 페이지로 이동
    element = driver.find_element(By.CLASS_NAME, 'mQ5b60reFF')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)

    # 평점 낮은순 클릭
    driver.find_element(By.CSS_SELECTOR, ".N\\=a\\:rvs\\.sevaldn").click()
    time.sleep(2)

    # 내용 저장 리스트
    box=[]

    # 내용 만드는 함수
    def make_content():
        for i in driver.find_elements(By.CLASS_NAME,'YEtwtZFLDz'):
            a=i.find_element(By.CLASS_NAME,'_3QDEeS6NLn').text
            box.append(a)


    # 10페이지 리뷰 크롤링 최대 200개
    try:
        for i in range(10):
            make_content()    
            driver.find_element(By.CLASS_NAME, "fAUKm1ewwo._2Ar8-aEUTq").click()
            time.sleep(1)
    except:
        pass
    
    driver.close()

    # 리뷰를 df로 생성
    df=pd.DataFrame(box)
    df[0]=df[0].str.replace('\n',' ')


    # gpt로 감성분석 
    import openai
    openai.api_key='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'
    total=[]
    for i in tqdm(df[0]):

        box1=[{'role':'system','content':'내가 보여준 글이 긍정이면 "긍정", 부정이면 "부정"으로만 대답해줘'},
            {'role':'user','content':i}]

        model=openai.ChatCompletion.create(model='gpt-3.5-turbo-16k-0613',messages=box1)
        gpt=model['choices'][0]['message']['content']
        total.append(gpt)

    df['리뷰분석']=total
    df=df[(df['리뷰분석']=='긍정') | (df['리뷰분석']=='부정')]


    # 첫번째 이미지-------------------------------------
    plt.figure(figsize=(15,10))
    sns.countplot(data=df,x='리뷰분석')
    plt.savefig(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image1.png')
    #--------------------------


    okt=Okt()
    kkma=Kkma()
    # 명사(NN), 동사(VV), 형용사(VA)

    # 단어 토큰화
    total_ = []
    for i in tqdm(df[0]):
        t = okt.normalize(i)
        t = kkma.pos(t)
        box_list = []
        for j in t:
            if j[1][:2] == 'NN':
                box_list.append(j[0])
            elif j[1] in ['VV','VA']:
                box_list.append(j[0]+'다')
        total_.append(" ".join(box_list))
    df['토큰화']=total_

    # 부정 리뷰만 df화
    df_negative=df[df['리뷰분석']=='부정']
    


    cv=CountVectorizer()
    dtm=cv.fit_transform(df_negative['토큰화'])
    dtm_df=pd.DataFrame(dtm.toarray(),columns=cv.get_feature_names_out())
    a = dtm_df.sum().sort_values(ascending=False)
    filtered_a = a[a > 3]
    
    # 쓸모 없는 단어 제거
    words_to_drop = ['하다', '먹다', '오다', '되다', '같다', '나다', '있다', '알다', '가다', '이렇다', '보내다']
    for word in words_to_drop:
        if word in filtered_a.index:
            filtered_a = filtered_a.drop(word)


    # 두번째 이미지 -----------------------------------------------------------------------------------------------
    wc=WordCloud(background_color='white',font_path='EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\BMHANNAPro.ttf')
    cloud=wc.generate_from_frequencies(filtered_a.to_dict())
    plt.figure(figsize=(15, 15))
    plt.axis('off')  # 축 끄기
    plt.imshow(cloud)
    plt.savefig(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image2.png')
    # ------------------------------------------------------------------------------------------------------------


    # 세번째 이미지 ----------------------------------------------------------------------------------------------
    s = filtered_a

    # Select top 5 items
    top_5 = s.head(5)

    # Plot bar plot with first bar in pastel red and others in pastel tone
    plt.figure(figsize=(15,10))

    # First bar in pastel red (salmon)
    plt.bar(top_5.index[0], top_5.values[0], color='salmon')

    # Other bars in pastel tone (light blue)
    for i in range(1, len(top_5)):
        plt.bar(top_5.index[i], top_5.values[i], color='skyblue')

    plt.title('Top 5 words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=0)
    plt.savefig(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image3.png')

    # 네번째 이미지 -----------------------------------------------------------------------
    # 텍스트 데이터 합치기
    indices=df[df['토큰화'].str.contains(filtered_a.index[0])].index



    selected_df = df.loc[indices]
    selected_df=selected_df.head()[0]

    # 폰트 설정 (여기서는 기본 폰트 사용)
    text = '\n\n\n\n'.join(selected_df.values)
    font_path = "EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\BMHANNAPro.ttf"
    font = ImageFont.truetype(font_path,30)


    # 이미지 생성
    image = Image.new('RGB', (1600, 600), color=(73, 109, 137))
    d = ImageDraw.Draw(image)

    # 텍스트 쓰기
    d.text((10,10), text, font=font)

    # 이미지 저장
    image.save(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image4.png')


    

@app.route('/', methods=['GET', 'POST'])
def generate():
    img1 = None
    img2 = None
    img3 = None
    img4 = None
    
    if request.method == 'POST':
        url = request.form['url']
        
        try:
            generate_images(url)
            
            # 만약 이미지 파일들이 존재한다면, 해당 파일들의 경로를 템플릿으로 전달합니다.
            if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image1.png'):
                img1 = 'static/image1.png'
            if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image2.png'):
                img2 = 'static/image2.png'
            if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image3.png'):
                img3 = 'static/image3.png'
            if os.path.exists(r'EXAM_08_NATURAL_LANGUAGE\mini\myproject\static\image4.png'):
                img4 = 'static/image4.png'
                
        except Exception as e:
            return str(e)
    
    return render_template('index.html', img1=img1, img2=img2, img3=img3, img4=img4)



if __name__ == '__main__':
     app.run(debug=True)
