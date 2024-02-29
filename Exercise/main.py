import pandas as pd
import receiptPdf

df = pd.read_csv('articles.csv', dtype={'id': str})


class Articles:

    def __init__(self, item_id):
        self.item_id = item_id
        self.item_name = df.loc[df['id'] == self.item_id, 'name'].squeeze()
        self.item_price = df.loc[df['id'] == self.item_id, 'price'].squeeze()

    def buy(self):
        stock_check = df.loc[df['id'] == self.item_id, 'in stock'].squeeze()
        if stock_check > 0:
            df.loc[df['id'] == self.item_id, 'in stock'] = df.loc[df['id'] == self.item_id, 'in stock'] - 1
            df.to_csv('articles.csv', index=False)
            return True
        else:
            return False


class Receipt:
    def __init__(self, article_object):
        self.article = article_object

    def generate(self):
        print(self.article.item_id, self.article.item_name, self.article.item_price)
        receiptPdf.generate(self.article.item_id, self.article.item_name, self.article.item_price)


print(df)
item_id = input("Please Enter your Item Id.")
article = Articles(item_id)

if article.buy():
    bought_receipt = Receipt(article)
    bought_receipt.generate()
else:
    print("Item is Out of Stock!")
