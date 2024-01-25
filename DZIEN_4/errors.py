try:
    # x=4
    print(x)
except NameError as ne:
    print(f"x nie istnieje: {ne}")
except Exception as exc:
    print(exc)
else:
    y=5
    z=y*x-2
    print(f'WARTOŚĆ z = {z}')
finally:
    k=18
    print(k)

print("ciąg dalszy programu!")

