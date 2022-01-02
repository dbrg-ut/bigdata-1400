# Source : https://gist.github.com/aialenti/cfd4e213ebf2ef6e20b195c8fb45382c
import pandas as pd
from tqdm import tqdm,trange
import csv
import random
import string
import datetime
from faker import Faker

faker = Faker()

random.seed(1999)

PRODUCT_NUMBERS=10_000
TOTAL_SALES = 1_000_000

letters = string.ascii_lowercase
letters_upper = string.ascii_uppercase
for _i in range(0, 10):
    letters += letters

for _i in range(0, 10):
    letters += letters_upper


def random_string():
    return faker.text().replace("\n","")


print(f"Products between 1 and {PRODUCT_NUMBERS}")
product_ids = [x for x in range(1, PRODUCT_NUMBERS+1)]
dates = []

# for i in range(1000):

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2021, 10, 30)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days


seller_ids = [x for x in range(1, 1001)]

#   Generate products
products = []
for p in  trange(1,len(product_ids)+1):
    products.append([p, f"product_{p:0>6}".format(p), random.randint(1, 150), "|".join(faker.words(random.randint(0,4)))])
#   Save dataframe
df = pd.DataFrame(products)
df.columns = ["product_id", "product_name", "price", "labels"]
df.to_csv("products.csv", index=False)
del df
del products

#   Generate sellers
sellers = [[0, faker.name(), 250000]]
for s in trange(1,len(seller_ids)+1):
    sellers.append([s, faker.name(), random.randint(12000, 2000000)])
#   Save dataframe
df = pd.DataFrame(sellers)
df.columns = ["seller_id", "seller_name", "daily_target"]
df.to_csv("sellers.csv", index=False)

#   Generate sales

df_array = [["order_id", "product_id", "seller_id", "date", "num_pieces_sold", "comment"]]
with open('sales.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(df_array)

order_id = 0
for i in trange(TOTAL_SALES):
    df_array = []

    order_id += 1
    random_number_of_days = random.randrange(days_between_dates)
    random_date= (start_date + datetime.timedelta(days=random_number_of_days)).isoformat()
    df_array.append(
        [order_id, random.choice(product_ids), random.choice(seller_ids), random_date,
            random.randint(1, 100), random_string()])

    with open('sales.csv', 'a', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(df_array)

sellers_df=pd.read_csv("sellers.csv",header=0)
sellers_df.to_parquet("sellers.parquet")

products_df=pd.read_csv("products.csv",header=0)
products_df.to_parquet("products.parquet")

sales_df=pd.read_csv("sales.csv",header=0)
sales_df.to_parquet("sales.parquet")

print("Done")
