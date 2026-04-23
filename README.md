# Islands Wrapper

This project serves as a wrapper for [The Islands](https://islands.smp.uq.edu.au/login.php), an online simulation website
designed for experimental analysis. While the site is designed for point and click operation, this project utilizes python's
request package to send http requests to automate processes required for experimental design and data collection.

## Getting Started


1) Clone the repository. 
2) Create a `.env` file. Inside the .env file the format should look like:
```dotenv
login=#email
password=#password
```

`login` should be the email that is used when logging into islands, and `password` the corresponding password.

3) Initialize IslandsAPI.
The main way to interact with this project is through IslandsAPI. 
It can called as follows:
```python
from api.API import IslandsAPI
api = IslandsAPI()
```

For more information on using the islands api see one of the following notebooks:

* [Islander Recruitment](./recruitment.ipynb)