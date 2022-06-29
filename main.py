import pandas as pd

print("hello world")

data = {
    'age': list(range(10, 20)),
    'height': list(range(50, 60))
}

df = pd.DataFrame(data, index=["p{}".format(idx) for idx in range(10)])

print(df)