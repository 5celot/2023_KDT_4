from flask import Flask, render_template,request
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('colorblind')
from tensorflow.keras import (layers,models,optimizers,utils,callbacks,metrics,losses,activations,)
from static.load_models.cover1.poke_models import get_diffusion
from static.load_models.cover2.stargan_models import get_stargan
from static.load_models.cover3.wgan_models import get_wgangp

# cover1 모델 함수
ddm=get_diffusion()

# cover2 모델 함수
solver=get_stargan()

# cover3 모델 함수
wgangp=get_wgangp()


# 이미지 저장 함수---------------------------------------------------------------------
def display(images, n=1, size=(8, 8), cmap="gray_r", as_type="float32", save_to=None):
    """
    Displays n random images from each one of the supplied arrays.
    """
    if images.max() > 1.0:
        images = images / 255.0
    elif images.min() < 0.0:
        images = (images + 1.0) / 2.0

    plt.figure(figsize=size)
    for i in range(n):
        _ = plt.subplot(1, n, i + 1)
        plt.imshow(images[i].astype(as_type), cmap=cmap)
        plt.axis("off")

    if save_to:
        plt.savefig(save_to)
        print(f"\nSaved to {save_to}")







app = Flask(__name__)


@app.route('/')
def generate():
    return render_template('index.html')



@app.route('/pokemon', methods=['GET', 'POST'])
def generate_cover1():

    result_1=None
    result_2=None
    result_3=None


    if request.method == 'POST':


        generated_images = ddm.generate(num_images=1, diffusion_steps=10, initial_noise = None).numpy()
        display(generated_images,save_to='static/result_img/cover1/result_1.jpg')        
        result_1='result_img/cover1/result_1.jpg'

        generated_images = ddm.generate(num_images=1, diffusion_steps=10, initial_noise = None).numpy()
        display(generated_images,save_to='static/result_img/cover1/result_2.jpg')        
        result_2='result_img/cover1/result_2.jpg'

        generated_images = ddm.generate(num_images=1, diffusion_steps=10, initial_noise = None).numpy()
        display(generated_images,save_to='static/result_img/cover1/result_3.jpg')        
        result_3='result_img/cover1/result_3.jpg'


    return render_template('cover1.html',result_1=result_1,result_2=result_2,result_3=result_3)





@app.route('/stargan', methods=['GET', 'POST'])
def generate_cover2():
    from PIL import Image
    from torchvision import transforms as T
    import torch

    result_1=None
    result_2=None
    result_3=None

    if request.method == 'POST':
        file = request.files['image']
        file.save('static/result_img/cover2/result_1.jpg')

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        image_size = 256

        # 불러온 이미지가 Torch 객체로 변환될 수 있도록 하기
        transform = []
        transform.append(T.Resize(image_size))
        transform.append(T.ToTensor())
        transform.append(T.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)))
        transform = T.Compose(transform)

        img_path = "static/result_img/cover2/result_1.jpg"
        image = Image.open(img_path)

        # Torch의 첫 번째 차원은 배치(batch) 크기
        # image = image.rotate(-90)
        image = transform(image).unsqueeze(0).to(device)

        # 이미지를 금발로
        # [Black_Hair, Blond_Hair, Brown_Hair, Male, Young]
        c_trg = [[0, 1, 0, 0, 0]]
        c_trg = torch.FloatTensor(c_trg).to(device)
        output = solver.G(image, c_trg)
        # 이미지 데이터 처리
        img_data = solver.denorm(output.data.cpu()).squeeze(0).permute(1, 2, 0)
        img_data = img_data.numpy()

        # [0, 1] 범위의 데이터를 [0, 255] 범위로 변환
        img_data = (255 * img_data).astype(np.uint8)

        # Numpy 배열을 PIL Image 객체로 변환
        img = Image.fromarray(img_data)

        # 이미지 저장
        img.save('static/result_img/cover2/result_2.jpg')


        # 이미지를 어리게
        # [Black_Hair, Blond_Hair, Brown_Hair, Male, Young]
        c_trg = [[0, 0, 0, 0, 1]]
        c_trg = torch.FloatTensor(c_trg).to(device)
        output = solver.G(image, c_trg)
         # 이미지 데이터 처리
        img_data = solver.denorm(output.data.cpu()).squeeze(0).permute(1, 2, 0)
        img_data = img_data.numpy()

        # [0, 1] 범위의 데이터를 [0, 255] 범위로 변환
        img_data = (255 * img_data).astype(np.uint8)

        # Numpy 배열을 PIL Image 객체로 변환
        img = Image.fromarray(img_data)

        # 이미지 저장
        img.save('static/result_img/cover2/result_3.jpg')




        result_1='result_img/cover2/result_1.jpg'
        result_2='result_img/cover2/result_2.jpg'
        result_3='result_img/cover2/result_3.jpg'
        



    return render_template('cover2.html',result_1=result_1,result_2=result_2,result_3=result_3)


@app.route('/wgan', methods=['GET', 'POST'])
def generate_cover3():

    result_1=None
    result_2=None
    result_3=None


    if request.method == 'POST':

        Z_DIM = 128
        z_sample = np.random.normal(size=(1, Z_DIM))
        imgs = wgangp.generator.predict(z_sample)
        display(imgs, cmap=None,save_to='static/result_img/cover3/result_1.jpg')

        z_sample = np.random.normal(size=(1, Z_DIM))
        imgs = wgangp.generator.predict(z_sample)
        display(imgs, cmap=None,save_to='static/result_img/cover3/result_2.jpg')

        z_sample = np.random.normal(size=(1, Z_DIM))
        imgs = wgangp.generator.predict(z_sample)
        display(imgs, cmap=None,save_to='static/result_img/cover3/result_3.jpg')

 
        result_1='result_img/cover3/result_1.jpg'
        result_2='result_img/cover3/result_2.jpg'
        result_3='result_img/cover3/result_3.jpg'


    return render_template('cover3.html',result_1=result_1,result_2=result_2,result_3=result_3)






if __name__ == '__main__':
     app.run(debug=True)


