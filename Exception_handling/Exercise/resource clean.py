try:
    f=open("sample.txt","w")
    f.write("Hello Python")
except Exception:
    print("error while writing file")
finally:
    f.close()
    print("file closed successfully")
    