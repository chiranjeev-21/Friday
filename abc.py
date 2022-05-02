# import Augmentor
# p = Augmentor.Pipeline(r"D:\yolo\archive\Car_Brand_Logos\Train\hyundai")
# p.zoom(probability=0.3, min_factor=0.7, max_factor=1.6)
# p.flip_top_bottom(probability=0.4)
# p.random_brightness(probability=0.3,min_factor=0.3,max_factor=1.2)
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
# p.sample(500)
import datetime
# import time as tt


# def time():
#     Time = datetime.datetime.now().strftime("%H:%M:%S")
#     print(Time)

# print(time())

tt=datetime.datetime.utcnow()+datetime.timedelta(hours=5.5)
# tt = datetime.datetime.utcnow()+datetime
print(tt)

