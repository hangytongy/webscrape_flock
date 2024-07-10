import requests
from bs4 import BeautifulSoup
import json

def scrape_flock_docs():
    urls = ['https://docs.flock.io','https://docs.flock.io/what-is-flock/the-centralisation-problem','https://docs.flock.io/what-is-flock/architectural-breakdown/smart-contract-design/transaction-lifecycle-proposers-and-voters',
           'https://docs.flock.io/what-is-flock/architectural-breakdown/general-flow','https://docs.flock.io/what-is-flock/architectural-breakdown/voting-process','https://docs.flock.io/flock-product/ai-arena/pre-requisites','https://docs.flock.io/flock-product/ai-arena/pre-requisites/wsl-installation',
           'https://docs.flock.io/flock-product/ai-arena/delegator-guide','https://docs.flock.io/flock-product/ai-arena/training-node-guide','https://docs.flock.io/flock-product/ai-arena/validator-guide',
           'https://docs.flock.io/flock-product/ai-co-creation-platform','https://docs.flock.io/flock-product/ai-co-creation-platform/rag',
           'https://docs.flock.io/flock-product/ai-co-creation-platform/architecture-flow','https://docs.flock.io/flock-product/ai-co-creation-platform/function-breakdown','https://docs.flock.io/flock-product/ai-co-creation-platform/contribution-mechanism',
           'https://docs.flock.io/flock-product/ai-co-creation-platform/roadmap','https://docs.flock.io/flock-product/fl-alliance','https://docs.flock.io/flock-product/fl-alliance/client-deepdown','https://docs.flock.io/flock-product/fl-alliance/client-flow',
           'https://docs.flock.io/flock-product/fl-alliance/functionality','https://docs.flock.io/ai-co-creation-platform/getting-started-manual-creation','https://docs.flock.io/ai-co-creation-platform/guideline-manual','https://docs.flock.io/ai-co-creation-platform/model-api-guide',
           'https://docs.flock.io/ai-co-creation-platform/create-a-discord-bot-with-model-api','https://docs.flock.io/partner-integrations/running-flock-node-on-akash-network',
           'https://docs.flock.io/useful-information/glossary']
    data = []
    
    for url in urls:    
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find relevant elements on the page (adjust according to the structure of the website)
            descriptions = soup.find_all('p',class_='max-w-3xl w-full mx-auto decoration-primary/6 page-api-block:ml-0')

            
            for description in descriptions:
                description = description.text.strip()
                if description != "":
                    item = {'description' : description}
                    data.append(item)
                else:
                    pass

            
        else:
            print(f"Failed to retrieve page: {response.status_code}, url : {url}")
    
    if data != []:
        return data, True
    
    else:
        return None, False
    
# Function to save data in JSONL format
def save_to_jsonl(data, filename='flock_docs.jsonl'):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f)
            f.write('\n')
            
if __name__ == '__main__':
    # Scrape data
    scraped_data, boolean = scrape_flock_docs()
    if boolean:
        # Save data to JSONL file
        save_to_jsonl(scraped_data)
        print(f"Scraped data saved to 'flock_docs.jsonl'")
    else:
        print("Scraping failed, check the website URL or your network connection.")