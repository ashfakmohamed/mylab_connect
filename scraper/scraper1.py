import requests
from bs4 import BeautifulSoup
import csv

def scrape_shoes():
    with open("shoes_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Image Link", "Shoe Name", "Price"])


    for i in range(1, 5):  
        url = f"https://us.princesspolly.com/collections/shoes?page={i}"
    

        response = requests.get(url)
    
    
        if response.status_code != 200:
            print(f"Failed to retrieve page {i}")
            continue
    
        soup = BeautifulSoup(response.content, "html.parser")

    
        with open("shoes_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            for item in soup.find_all("div", class_="product-tile"):
   
                image_tag = item.find("img", class_="product-tile__image")
                img1 = image_tag.attrs
                for j in img1:
                    if j == 'src':
                        image_link = img1[j]

           
                name_tag = item.find("a", class_="product-tile__name product-tile__name--full")
                shoe_name = name_tag.get_text(strip=True) if name_tag else "No name"

            
                price_tag = item.find("span", class_="product-tile__price")
                price = price_tag.get_text(strip=True) if price_tag else "No price"

     
                writer.writerow([image_link, shoe_name, price])
                print(shoe_name)
                print(price)
                print(image_link)


if __name__ == '__main__':
    scrape_shoes()

