import requests

country = input('Enter a country: ')

url = f"https://disease.sh/v3/covid-19/countries/{country}"
response = requests.get(url)

if response.status_code == 200:
    cases = response.json()['cases']
    cases = f'{cases:_.2f}'
    cases = cases.replace('.' ,  ',').replace('_' ,  '.')
    print(f'Covid cases in {country}: {cases}')
else:
    print('Error when searching by country.')