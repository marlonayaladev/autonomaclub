
import requests

url = "https://api.apis.net.pe/v2/reniec/dni"
dni = input("->")
  
token = "<apis-token-11834.pIniTDIwrwS2OWonT4L3tTd6O6oSLWTY>"  


params = {
    "numero": dni,
    "token": token
}

try:
    
    response = requests.get(url, params=params)

    
    if response.status_code == 200:
        data = response.json()
        print("Informacion del DNI:")
        print(data["nombres"], data["apellidoPaterno"], data["apellidoMaterno"])

    else:
        print(f"Error {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"error al realizar la solicitud: {e}")
