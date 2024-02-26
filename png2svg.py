import cv2
import os
import numpy as np
import tqdm

def main():
    '''主函数'''
    # 定义参数
    img_list = list() 
    # 获取文件列表
    for file in os.listdir(img_dir):
            if os.path.splitext(file)[1].lower() in '.png|.jpg':
                img_list.append(file)
    print('当前总图片数量： %d' % len(img_list))

    # 循环处理图片
    for img_path in tqdm.tqdm(img_list):
        textimg = cv2.imdecode(np.fromfile(os.path.join(img_dir,img_path),dtype=np.uint8),-1)
        textimg = cv2.cvtColor(textimg, cv2.COLOR_RGB2BGR)
        # 提取图形区域
        textimg = cv2.resize(textimg, (640, 640))
        blur = cv2.GaussianBlur(textimg, (3, 3), 0)

        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)               
        contours,hierarchy = cv2.findContours(thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

        epsilon = 10
        h, w, _ = textimg.shape
        code = os.path.splitext(img_path)[0]
        svg_path = './svg/'+code+'.svg'
        with open(svg_path, "w+") as f:
            f.write(f'<svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="{w}.000000pt" height="{h}.000000pt" viewBox="0 0 680.000000 680.000000" preserveAspectRatio="xMidYMid meet">')      
            f.write(f'<g transform="scale(1.00000,1.00000)">')
            for c in contours:
                f.write('<path d="M')
                approx = cv2.approxPolyDP(c,epsilon,False)
                for i in range(len(approx)):
                    x, y = approx[i][0]
                    if i == len(approx)-1:
                        f.write(f"{x} {y}")
                    else:
                        f.write(f"{x} {y} ")
                f.write('"/>')                
            f.write(f'</g>')
            f.write("</svg>")
    print('全部处理结束')
    
if __name__=='main':
    img_dir = 'png图片存放位置'
    main()