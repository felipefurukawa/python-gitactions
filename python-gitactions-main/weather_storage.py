from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

creditials_dict = {
  "type": "service_account",
  "project_id": "optimal-life-382223",
  "private_key_id": "70cb49c79b5ccf3eb5a0ca64da3605159897e090",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC/f+oG0WW6yTr0\nKwMJlimMQK1ypAaDbVrcccdOuUgHJ/WwodIGNUNeHCBLaKI+F3wvTkkRs1ZfaMJ7\nblpo2Aina5EynP+zm406CxfKboDBvlj93Pjd1SfPMXxtSkhw8wZK4de4LmM+ZNvV\noB+W60Kg9zMr4gUUtCHYF5KixBtNb7ylDrI7HnxumZq8d+9P47R1FrIZ2xwF/qY3\nLWKJvlNLUvxf75KL/sOm9ZdQqEynKF0Tfw56x5WXNRGSOkzfcOOk19buWzAHJnpo\nJ4966oayFBKDnv2CsmblhDz4TLC83YMDmM2QNTKwyBk2bt1I1MwfRvXqxab5sTn7\nz0vjcdxtAgMBAAECggEAGNiIzZ+nekeXjYxzFXBVLaxKlMAxVCYBDu74M/+YF82Y\nc/Va4ZFRj0lI61/FBRdY9m5KzrAc+b4G1arosgetf8NWEGIMTwpUlX5Q9OPHctu2\ngiGEbIu2YYyDH07u/TCa1WZd7bifCb5eQ2ZGEvetKmNIUV4+2IPSjE3qqZGWFUK7\nG9yrPYQbrivJIb5wMe+Flt44tTfiLxgCM/uEeTNixtTBVENK1giyHWBrlCAJUJOG\nsHtCygXSj1bQXoDEf8+hPCl0Omw5DYgxVjOydztJX2+MFAAiqzuYeK0wAscDKsHi\nb841niSSE8JOaqjeI3sIDKAqKplV2RiCHba0PHN3JQKBgQD8ljT5qkMXv/NGQte8\nVJdq+ST2mOqgxdfMT1ItwXoZLJFI39RmSo3zJyHKNdTvIr3ZGsL1OjepgOn4ZHUR\nST1e50CeaaJl3CtEg8gkzdvsqvVABWotPdqaa2zq9DV+0D8ABA5WXNKJUjH1IqRD\ngAplqqAcDlEN754/rUf2ZssUCwKBgQDCFmJIiDSvTyLfpNegxUtl7G4G6JR+DR1U\nFIsjTHDJPg1LilLl4rzzXG98ZswYpOBQ+FhJJNhnAlnrd3+YW/C1q7dsbTmLCnVU\nG47QrkTOZGyp3LSwIjZA3MrMOK/W24RQEQN7rRKClOsJlYtKrsXl+B9n4hIDkzsi\nV6gP0InkZwKBgEzCKN8mSrVQ89EKRx1IZ6tugzkdR1AMT4QbJtIY1c4IqS4INzfO\nuEyIO9CDg24YlLEBXPXA92Ffd7qwbJMQOsI4bH63g06JFe0ATzZACPFnEpieDKIr\nBd+ffb348LjU+BA9K047bw+kFuJz4I9SvdYfgACGqUMe6mxXcGME4fn5AoGBAJCl\n9AvQj0tUdE4vYZDtWXsV0Q6PChRDm+cNBIGDN8+T0n7JEW1JJb9N1bzmNBft0Uwn\nOk0RC8MBqphl0A9x/hy3ZJWHdcpdOgI8I5z9NESJ7b5Owc8/QCXpJ686VDqSEbNG\nas0iuNffOqhC7rPzO4Rf/rACeaB2eyzmHVfj+NDjAoGBANjSdyNivIJl0MYvSle/\nQ4SXR1NXOcKTisQ7D5rs9L41mN4AZweITrpUoRkTRr3f150LVg063zgziKooezAd\nRev4bThmVL8vxUH/CXlme09Oi8i1uZPBHzrdS2XJ/+xm27DkgpI/gLtYzyYZpDP9\nO8wEez6oXqK3HP8kV8/ikEE9\n-----END PRIVATE KEY-----\n",
  "client_email": "974241466144-compute@developer.gserviceaccount.com",
  "client_id": "117774023410893166868",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/974241466144-compute%40developer.gserviceaccount.com"
}

try:
  res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
  
  print(info)

  credentials = service_account.Credentials.from_service_account_info(creditials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('weather_ffc')
  blob = bucket.blob('weather_info.txt')

  blob.upload_from_string(info + '\n')

  print('File uploaded')

  print("Finished.")
except Exception as ex:
  print(ex) 