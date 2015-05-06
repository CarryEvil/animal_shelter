import time
import GetAnimal
import WebFetcher


def execute():
    bTime = time.time()
    data = WebFetcher.FetchWebPage('http://data.coa.gov.tw/Service/OpenData/AnimalOpenData.aspx')
    GetAnimal.HandleAnimal(data)
    print (time.time() - bTime), ' seconds.'

if __name__ == "__main__":
    execute()
