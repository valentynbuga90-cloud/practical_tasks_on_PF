import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import pytz
from bs4 import BeautifulSoup
import tqdm
import emoji
import tabulate



try:
    response = requests.get("https://httpbin.org/get")
    print("\n[requests] Статус-код:", response.status_code)
except Exception as e:
    print("[requests] Помилка:", e)


try:
    arr = np.array([1, 2, 3, 4])
    print("\n[numpy] Масив:", arr, "Сума:", arr.sum())
except Exception as e:
    print("[numpy] Помилка:", e)


try:
    df = pd.DataFrame({"Name": ["Alex", "Nika"], "Age": [21, 20]})
    print("\n[pandas] DataFrame:\n", df)
except Exception as e:
    print("[pandas] Помилка:", e)


try:
    fake = Faker()
    print("\n[faker] Випадкове ім'я:", fake.name())
except Exception as e:
    print("[faker] Помилка:", e)


try:
    print("\n[emoji] Приклад:", emoji.emojize("Hello world :smile:"))
except Exception as e:
    print("[emoji] Помилка:", e)

