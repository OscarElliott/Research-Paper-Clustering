import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def read_dataset(file_path):
    # Read dataset from xlsx into Pandas dataframe
    df = pd.read_excel(file_path)
    return df

def get_abstract(doi_url):
    # Initialize the browser
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navigate to the DOI URL
    driver.get(doi_url)
    time.sleep(5)  # Wait for the page to load
    abstract_text = None

    # Attempt to extract abstract text only if abstract_text is not already populated
    try:
        abstract = driver.find_element(By.CSS_SELECTOR, '#abss0002')
        abstract_p = abstract.find_element(By.TAG_NAME, 'p')
        abstract_text = abstract_p.text
    except Exception:
        pass

    if not abstract_text:
        try:
            abstract = driver.find_element(By.CSS_SELECTOR, '.html-p')  # This works as it finds the first html-p element which should always be the abstract
            abstract_text = abstract.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, '.article-section__content')
            abstract_p = abstract_div.find_element(By.TAG_NAME, 'p')
            abstract_text = abstract_p.text
        except Exception:
            pass
    
    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, '.hlFld-Abstract')
            abstract_p = abstract_div.find_element(By.TAG_NAME, 'p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, '.c-article-section__content')
            abstract_p = abstract_div.find_element(By.TAG_NAME, 'p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, 'div.abstract-text')
            abstract_div = abstract_div.find_element(By.TAG_NAME, 'div')
            abstract_div = abstract_div.find_element(By.TAG_NAME, 'div')
            abstract_text = abstract_div.find_element(By.TAG_NAME, 'p').text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, 'div.abstract-text')
            abstract_div = abstract_div.find_element(By.TAG_NAME, 'div')
            abstract_div = abstract_div.find_element(By.TAG_NAME, 'div')
            abstract_text = abstract_div.find_element(By.TAG_NAME, 'div').text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, 'div.abstract-text')
            abstract_div = abstract_div.find_element(By.TAG_NAME, 'div')
            abstract_div = abstract_div.find_element(By.TAG_NAME, 'div')
            abstract_text = abstract_div.find_element(By.TAG_NAME, 'span').text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.CSS_SELECTOR, '#page-content > div:nth-child(3) > div.article-content > div.article-text.wd-jnl-art-abstract.cf')
            abstract_p = abstract_div.find_element(By.TAG_NAME, 'p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_div = driver.find_element(By.XPATH, '//*[@id="pb-page-content"]/div/main/article/div[2]/div[3]/div/div[2]/section[2]/div/div[1]')
            abstract_text = abstract_div.text
            abstract_div = driver.find_element(By.XPATH, '//*[@id="pb-page-content"]/div/main/article/div[2]/div[3]/div/div[2]/section[2]/div/div[2]')
            abstract_text += abstract_div.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract = driver.find_element(By.CSS_SELECTOR, '.articleBody_abstractText')
            abstract_text = abstract.text
        except Exception:
            pass
        
    if not abstract_text:
        try:
            abstract_p = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/article/div[6]/div[2]/div/p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_p = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div[2]/article/div[5]/div[2]/div[2]/div/p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_p = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/article/div[6]/div/div/p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_p = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/article/div[5]/div[2]/div[2]/div/p')
            abstract_text = abstract_p.text             
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract_outer_div = driver.find_element(By.CSS_SELECTOR, '.abstract.author')
            abstract_div = abstract_outer_div.find_element(By.TAG_NAME, 'div')
            abstract_p = abstract_div.find_element(By.TAG_NAME, 'p')
            abstract_text = abstract_p.text             
        except Exception:
            pass

    if not abstract_text:
        try:
            abstract = driver.find_element(By.CSS_SELECTOR, '.capsule__text')
            abstract_p = abstract.find_element(By.TAG_NAME, 'p')
            abstract_text = abstract_p.text
        except Exception:
            pass

    
    
    if not abstract_text:
        try:
            abstract = driver.find_element(By.CSS_SELECTOR, '#abstract')
            abstract_div = abstract.find_element(By.TAG_NAME, 'div')
            abstract_text = abstract_div.text
        except Exception:
            pass


    # If abstract_text is still None, print an error message
    if not abstract_text:
        print(f"Error: Unable to find the abstract on {doi_url}")

    driver.quit()
    return abstract_text



def main():
    input_file = 'data/raw/Green Energy Papers Database.xlsx'
    output_file = 'data/processed/abstracts.csv'

    df = read_dataset(input_file)

    results = []

    #Iterate through each row and extract abstracts
    for index, row in df.iterrows():
        title = row['Name']
        doi_url = row['DOI'] 
        abstract_text = get_abstract(doi_url)

        results.append({'Title': title, 'DOI': doi_url, 'Abstract': abstract_text})

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()