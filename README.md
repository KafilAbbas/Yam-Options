
## About The Project

Live option chain and analysis.
#### Features
* Contain live option chain data of NSE and MCX exchanges indices mainly NIFTY, BANKNIFTY, FINNIFTY, MIDCPNIFTY, CRUDEOIL and NATURALGAS.
* Provide live option chain data of current and near expiries
* Live stradle premium chart for option scalpers

#### External Api
* Shoonya Api

### Built With
This website is made with Django rest-framework as backend and React as frontend 
* [![Django][Django.js]][Django-url]
* [![React][React.js]][React-url]

## Getting Started
### Prerequisites
#### For backend

* Shoonya Api
  ```sh
  pip install requests
  ```
   ```sh
  pip install websocket_client
  ```
    ```sh
  pip install ./Requirement/NorenRestApiPy-0.0.22-py2.py3-none-any.whl
  ```
     ```sh
  pip install pandas
  ```
     ```sh
  pip install pyyaml
  ``` 
* Writing CSV
  1. xlwings
  ```sh
  pip install xlwings
  ```
  2. xlsxwriter
  ```sh
  pip install xlsxwriter
  ```
* Downloading files
  1. wget
  ```sh
  pip install wget
  ```
  2. zipfile
  ```sh
  pip install zipfile
  ```

#### For Frontend
  ```sh
  npm install 
  ```

### Installation

1. Change the ip at your ip in reactapp/src/components/option_chain.js on line 8 and 329
2. Change the ip at your ip in reactapp/src/components/stradle.js on line 5 and 57
3. Add you ip in allowed hosts in djangoproj/djangoproj/setting.py 
4. Run the file Dataextractor in djangoproj/djangoproj/py_prog in background
5. Run the file NSE_HISTO.py and MCX_HISTO.py present in py_prog in background
6. Run the file stradleNFO.py and stradleMCX.py present in py_prog in background
7. Run server
  ```sh
  python manage.py runserver 0.0.0.0:8000 
  ```
8. Run Frontend server
```sh
  npm start 
  ```
9. Acess it using url as
```sh
  http://yout_ip_addr:port/
  ```
## Usage
#### url http://yamoptions.in:3000/
This application is used for live option chain data analysis of NSE mainly nifty, banknifty, finnifty, midcapnifty and MCX mainly crude oil and natural gas each having two expiries. On the basis of live data such as Last traded prices, volume and open interest, change in open interest one can analyse the market mood and behavior and live straddle chart can help to get trades at the right time entry for option scalping.   

[Django.js]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
