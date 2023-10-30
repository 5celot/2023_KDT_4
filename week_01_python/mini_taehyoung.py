# -----------------------------------------------
# 클래스명: 기프티콘 선물하기,사용하기
# 클래스 속성   : 발급사
# 인스턴스 속성 :  회사명,상품종류,제품명,가격,일련번호,유효기간       
# 기능메서드    : 선물하기
# 클래스메서드  : 총 기프티콘수, 기프티콘 정보보기, 사용하기
# -----------------------------------------------

# 무작위 일련번호 생성위해 random모듈 임포트
import random



class gifticon:
    # 기프티콘 발급사
    __PUBLISHER='cacao'

    # 히스토리 데이터 생성
    SERIAL_DATA={}

    
    # 생성자 메서드-------------------------------------------------------------------
    def __init__(self,_company,_productType,_productName,_price,_expiryDate):
        self.__company=_company
        self.__productType=_productType
        self.__productName=_productName
        self.__price=_price
        self.__expiryDate=_expiryDate

        
        # 히스토리 파일 없을 시 생성
        dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
        filename=dirpath+'gifticon.txt'
        with open(filename, mode='a',encoding='utf-8') as fp:
            fp.write(f'\n') 


        # 일련번호 생성
        while True:
            _serial=f'{random.randint(1,100_000_000):0>9}'
            with open(filename, mode='r',encoding='utf-8') as fp:
                data=fp.read()

            
            if _serial not in gifticon.SERIAL_DATA and data.find(_serial)==-1 :
                gifticon.SERIAL_DATA[_serial]=[self.__company,self.__productType,self.__productName,self.__price,self.__expiryDate]
                item=_serial,gifticon.__PUBLISHER,self.__company,self.__productType,self.__productName,self.__price,''.join([i for i in self.__expiryDate if i.isdigit()])
                
                # 히스토리 파일에 각 아이템 데이터 저장
                with open(filename, mode='a',encoding='utf-8') as fp:
                    fp.write(f'{item}\n')  
                break

        self.__serial=_serial



        

    # get/set 메서드----------------------------------------------------------
    @property
    def company(self):
        return self.__company
    @property
    def product_type(self):
        return self.__productType
    @property
    def product_name(self):
        return self.__productName
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,new_price):
        new_price=self.__price
        return new_price
    @property
    def serial(self):
        return self.__serial
    @property
    def expiryDate(self):
        return self.__expiryDate
    

    
    # 기능 메서드-------------------------------------------------------------
    # 해당 아이템 선물하기
    def present(self,number):
        dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
        filename=dirpath+f'gifticon{number}.txt'
        with open(filename, mode='a',encoding='utf-8') as fp:
            fp.write(f'{self.__serial}\n')


    #클래스 메서드 ----------------------------------------------------------
    # 발급된 총 기프트콘 수
    @classmethod
    def getGiftCount(cls):
            # 히스토리 데이터 읽기
        dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
        filename=dirpath+'gifticon.txt'
        with open(filename, mode='r',encoding='utf-8') as fp:
            hisData=fp.read()
            count=hisData.count('(')
        print(f'발급된 총 기프티콘 수 : {count}')


    # 일련번호로 기프티콘 정보보기
    @classmethod
    def printInfo(cls,serialNum):
        # 히스토리 데이터 읽기
        dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
        filename=dirpath+'gifticon.txt'
        with open(filename, mode='r',encoding='utf-8') as fp:
            hisData=None          
            
            # 한줄씩 불러옴
            for i in fp:
                if serialNum in i.strip():
                    hisData=i.strip()[1:-1]
                    hisData=hisData.replace("'",'').split(', ')
                    break
            print(f'{hisData}')  

    

    # 기프티콘 사용하기
    @classmethod
    def useGifticon(cls,number,serialNum):
        
        # 히스토리 데이터 읽기
        dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
        filename=dirpath+'gifticon.txt'
        with open(filename, mode='r',encoding='utf-8') as fp:
            hisData=fp.read()       
        
        
        # 사용자 데이터 읽기
        dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
        filename=dirpath+f'gifticon{number}.txt'
        with open(filename, mode='r',encoding='utf-8') as fp:
            data=fp.read()

        
            # 히스토리와 사용자 데이터 비교 후 둘다 있으면 사용
            if data.find(serialNum) != -1 and hisData.find(serialNum)!=-1: 
                data = data.replace(serialNum, '')

                with open(filename, mode='w', encoding='utf-8') as fp:
                    fp.write(data)
                
                # 유효기간 확인
                dirpath='D:\\EXAM_4PYTHON\\DAY_10\\'
                filename=dirpath+'gifticon.txt'
                with open(filename, mode='r',encoding='utf-8') as fp:
                    hisData=None
                    # 한줄씩 비교
                    for i in fp:
                        if serialNum in i.strip():
                            hisData=i.strip()[1:-1]
                            hisData=hisData.replace("'",'').split(', ')
                            break
                hisData=int(hisData[-1])

                if hisData>=20230707:        
                    print('해당 기프티콘을 사용했습니다.')
                else:
                    print('해당 기프티콘은 만료되었습니다.')
            else:
                
                print('해당 기프티콘이 없습니다.')
    
    


      

    
# 함수 사용 -------------------------------------------------------

# 기프티콘 생성과 선물
# item1=gifticon('교촌','치킨','황금올리브',23000,'2023년07월06일')
# item2=gifticon('코카콜라','음료','코카콜라',2000,'2024년07월06일')
# item3=gifticon('펩시','음료','코카콜라',2000,'2023년12월06일')
# item4=gifticon('삼천리','자전거','svv-1000',200000,'2025년08월03일')
# item5=gifticon('애플','전자기기','에어팟',150000,'2027년05월16일')
# item6=gifticon('삼성','전자기기','갤럭시s',1000000,'2024년12월25일')

# item1.present('010-1111-1111')
# item2.present('010-1111-2222')
# item3.present('010-1111-3333')
# item5.present('010-1111-4444')
# item4.present('010-1111-2222')
# item6.present('010-1111-2222')

# # 기프티콘 정보
gifticon.printInfo('009914001')

# # 총 발행횟수
# gifticon.getGiftCount()

# 기프티콘
# # 기프티콘 사용
gifticon.useGifticon('010-1111-2222','009914001')


