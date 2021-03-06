from model.config import *
import matplotlib.pyplot as plt
import pandas as pd


conf = LSTM_Config()

# step 1: Get dataset (csv)
data = pd.read_csv(conf['data_file_path'], encoding='gbk')

# step 2: Select Feature
price = data['price'].values
mid_price = data['mid_price'].values
Avg_price = data['VW_Avg_sale_price'].values

plt.figure(figsize=(200, 15))
plt.plot(price)
plt.plot(mid_price)
plt.plot(Avg_price)
plt.legend(['deal_price', 'mid_price', 'Avg_price'], loc='upper right')
plt.title('deal price & mid_price & average_price')
plt.xlabel('time')
plt.ylabel('price')
plt.show()