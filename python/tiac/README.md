南海云课堂的回归测试脚本  
  
## 测试环境
- `Python 3`，例如 https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe
- 放置 `HTMLTestRunner.py` 到 Python 安装目录的 Lib 目录下
    
- 官网下载 Chrome 浏览器
- 官网下载 `chromedriver.exe`，并放置到 Python 安装目录的 Scripts 目录下。注意官网上 Chrome 浏览器版本匹配说明
- 安装 tesseract，用来 OCR 识别验证码，例如 https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe。 默认安装选项即可，不需要勾选额外的资源包（下载慢）。
    - 环境变量 `Path` 增加：`C:\Program Files (x86)\Tesseract-OCR`
    - 新增系统变量 `TESSDATA_PREFIX`，值为 `C:\Program Files (x86)\Tesseract-OCR`
    - 验证：`tesseract -v` 和 `tesseract --list-langs`

- 安装用到的 Python 库  
    ```
    pip install selenium
    pip install Pillow
    pip install pytesseract
    pip install pypiwin32
    pip install zmail
    pip install BeautifulReport
    ```
## 执行命令
修改 `config.py` 里的配置后  
```
py beautifulReport.py
```

## 注意
- 要加上 `chrome_options.add_argument('--force-device-scale-factor=1')` 强制 chrome 按 100% 缩放。否则系统不是 100% 缩放时，截取验证码图片区域时会错位
- config.py 临时文件 xxx/a.png，xxx 路径需要有写入权限
