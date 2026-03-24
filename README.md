### ![logo](logo_readme.png)

### 📝 Description
Not a real application of the national messenger Max, the application is just a dummy, without unnecessary functions and other things, it creates the appearance of having it on your phone.

### 🖼️ Screenshotes
<img src="https://github.com/d3l1f3r/Fake_Max_app/blob/main/1.jpg" width="50%" /> <img src="https://github.com/d3l1f3r/Fake_Max_app/blob/main/2.jpg" width="50%" />


### 🛠️ Tools
| Tools | Usage |
| :--- | :--- |
| **Python-3.11** | Main Programming language |
| **kivy** | Python library for GUI |
| **buildozer** | Buildozer is a tool for turning Python applications into binary packages |

### 🚀 Installing
```git clone https://github.com/d3l1f3r/Fake_Max_app.git```

```cd Fake_Max_app/```

```python3.11 -m venv venv-buildozer```

```source venv-buildozer/bin/activate```

```pip install --upgrade pip setuptools wheel "cython==0.29.37" buildozer```

```buildozer init```

```buildozer -v android debug deploy run```