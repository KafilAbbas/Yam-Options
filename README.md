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
       

  


[Django.js]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
