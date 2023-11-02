from flask import Flask, request, render_template, jsonify
import os
import joblib
import cv2
from keras.saving import load_model
import numpy as np
randomforest = joblib.load('EXAM_07_DL\mini_project\cgi-bin\RandomForestClassifier(15).pkl')
model_age = load_model(r'EXAM_07_DL\mini_project\cgi-bin\cnn_fashion_model_AGE.hdf5')
model_income = load_model(r'EXAM_07_DL\mini_project\cgi-bin\cnn_fashion_model_INCOME.hdf5')
model_job = load_model(r'EXAM_07_DL\mini_project\cgi-bin\cnn_fashion_model_JOB.h5')
model_style = load_model(r'EXAM_07_DL\mini_project\cgi-bin\cnn_fashion_model_STYLE.hdf5')
model_year = load_model(r'EXAM_07_DL\mini_project\cgi-bin\fashion_year.HDF5')




income = {0:'250만 원 미만', 1:'250~350만 원 미만', 2:'350~450만 원 미만', 3:'450~550만 원 미만', 4:'550~650만 원 미만', 5:'650만 원 이상'}
style={0: 'athleisure', 
                1:'bodyconscious',
                2:'cityglam' , 
                3:'classic',
                4:'disco', 
                5:'ecology', 
                6:'feminine', 
                7:'genderless', 
                8:'grunge', 
                9:'hiphop', 
                10:'hippie', 
                11:'kitsch', 
                12:'lingerie', 
                13:'lounge',
                14:'military', 
                15:'minimal', 
                16:'normcore', 
                17:'oriental', 
                18:'popart', 
                19:'powersuit', 
                20:'punk', 
                21:'space', 
                22:'sportivecasual'}

age={0:'40~49세',
        1:'30~39세',
        2:'20~29세',
        3:'50~60세'}
year={0:'1950',1:'1960',2:'1970',3:'1980',4:'1990',5:'2000',6:'2010',7:'2020'}
job =  {0:'전업주부', 1:'기술/전문직', 2:'판매/서비스직', 3:'사무/관리직', 4:'학생', 5:'기타'}



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/')
def index():
    return render_template('index.html', result_message="아직 없음",internal_script="")

@app.route('/upload', methods=['POST','GET'])


def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': '파일이 없습니다.'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'success': False, 'message': '파일을 선택하지 않았습니다.'})

    if file:
        filename = os.path.join(r"EXAM_07_DL\mini_project\cgi-bin\static\upload\uploaded_image.png")
        file.save(filename)





        #여기다가 인공지능 처리하실거 넣으시고
        imgData1 = cv2.imread(r"EXAM_07_DL\mini_project\cgi-bin\static\upload\uploaded_image.png")
        imgData1 = cv2.resize(imgData1,(300,400)).reshape(1,400,300,3)/255.0
        predResult_year = year[np.argmax(model_year.predict(imgData1))]

        imgData2 = cv2.imread(r"EXAM_07_DL\mini_project\cgi-bin\static\upload\uploaded_image.png")
        imgData2 = cv2.resize(imgData2,(75,100)).reshape(1,100,75,3)/255.0
        predResult_style = style[np.argmax(model_style.predict(imgData2))]
        arr1 = np.array([[10**6.9999,10,10**6.9992,10]])
        predResult_age = age[np.argmax(model_age.predict(imgData2)*arr1)]
        predResult_job = job[np.argmax(model_job.predict(imgData2))]
        arr2 = np.array([[1.5,1,2,2.5,3,3]])
        predResult_income = income[np.argmax(model_income.predict(imgData2)* arr2)]




        # 'uploaded_image' 변수를 템플릿에 전달
        return render_template('index.html',  result_message=f"{predResult_year}",
                               result_message1=f"{predResult_style}",
                               result_message2=f"{predResult_age}",
                               result_message3=f"{predResult_job}",
                               result_message4=f"{predResult_income}",
                               internal_script="showResult();")

if __name__ == '__main__':
    app.run(debug=True)