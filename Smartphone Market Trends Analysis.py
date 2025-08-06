import pandas as pd



df = pd.read_csv(r"D:\Tech Courses\Projects\Project2\phone search.csv")
print(df)

df.info()

print(df.columns.tolist())

print(df.shape)

print(f"Dataset contains {df.shape[0]} Rows and {df.shape[1]} Columns")

print(df.describe())

print(df.isnull().sum())





#-----------------------------------------------------------





# ----- Delete Duplicate Rows -----



df.drop_duplicates(inplace=True)

print(df.duplicated().sum())

print(df.shape)




#-----------------------------------------------------------





# ----- Transform Data Type -----



df['product_price'] = pd.to_numeric(df['product_price'].replace('[\$,]', '', regex=True))

df['product_original_price'] = pd.to_numeric(df['product_original_price'].replace('[\$,]', '', regex=True))

df['product_minimum_offer_price'] = pd.to_numeric(df['product_minimum_offer_price'].replace('[\$,]', '', regex=True))

print(df.dtypes)






#-----------------------------------------------------------


#  ----- Delete useless columns -----



columns_to_drop = ['unit_price', 'unit_count', 'coupon_text', 'delivery',
                   'has_variations', 'product_availability']
df.drop(columns=columns_to_drop, axis=1, inplace=True)


print(df.shape)




#-----------------------------------------------------------




#   ----- Put the rows that have missing data with Mean and Median -----




df.fillna({"product_star_rating":4},inplace=True)
product_star_rating = df["product_star_rating"].mean()
df.fillna({"product_star_rating":product_star_rating},inplace=True)
print(product_star_rating)


df.dropna(subset=['product_price'], inplace=True)

df.dropna(subset=['sales_volume'], inplace=True)


median_original_price = df['product_original_price'].dropna().median()
df['product_original_price'].fillna(median_original_price, inplace=True)


print(df.isnull().sum())

print(df.shape)





#-----------------------------------------------------------



# استخراج اسم البراند من العنوان  -----


def extract_brand(title):
    brands = ['Samsung', 'Motorola', 'Apple', 'Panasonic', 'OnePlus', 'Google', 'Nokia', 'BLU', 'Alcatel', 'VTech', 'AT&T', 'TCL']
    for brand in brands:
        if brand.lower() in title.lower():
            return brand
    return "Other"

df['brand'] = df['product_title'].apply(extract_brand)




#-----------------------------------------------------------




#  تصنيف نوع الهاتف (Mobile / Cordless / Flip)  -----


def classify_type(title):
    title = title.lower()
    if 'flip' in title:
        return 'Flip Phone'
    elif 'cordless' in title or 'landline' in title or 'corded' in title:
        return 'Cordless Phone'
    else:
        return 'Mobile Phone'

df['product_type'] = df['product_title'].apply(classify_type)





#-----------------------------------------------------------




#  تنظيف وتوحيد بيانات sales_volume
# تعويض القيم الغلط أو الناقصة




import numpy as np

def clean_sales_volume(text):
    try:
        if isinstance(text, str):
            if 'K+' in text:
                return float(text.split('K+')[0]) * 1000
            elif '+' in text:
                return float(text.split('+')[0])
            elif any(char.isdigit() for char in text):
                return float(''.join([c for c in text if c.isdigit()]))
        return np.nan
    except:
        return np.nan

df['sales_volume_clean'] = df['sales_volume'].apply(clean_sales_volume)


median_volume = df['sales_volume_clean'].median()
df['sales_volume_clean'].fillna(median_volume, inplace=True)


df.drop(['sales_volume'], axis=1, inplace=True)


print(df.columns)

print(df.shape)



#   Save Clean File

df.to_csv("Smart_Phone_Market_Analysis_Cleaned.csv")