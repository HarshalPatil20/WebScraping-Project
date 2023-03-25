from autoscraper import AutoScraper

url = "https://www.cardekho.com/"




wanted_list = ["The most searched cars","Latest Cars","Upcoming Cars","Electric Cars"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)

scraper.save('carcategories')