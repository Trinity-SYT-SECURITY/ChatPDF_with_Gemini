Download project

`https://github.com/Trinity-SYT-SECURITY/ChatPDF_with_Gemini.git`

Give the file permissions

`sudo chmod 777 *`

Update your ubuntu

`sudo apt update && sudo apt upgrade`

Other step pls follow the steps below:

`https://docs.google.com/document/d/1Kr9Ibjy0QqzTTGsnnxp-BgmdIxQLY5CZzuxAEgv6Ui0/edit?usp=sharing`

Install the required Python packages:

`pip install -r requirements.txt`

Download the mousepad(more easy to edit your profile)

`sudo apt install mousepad`

Set up your Google API key from `https://makersuite.google.com/app/apikey` by creating a `.env` file in the root directory of the project with the following contents:

+ 當前根目錄下

`mousepad .env`

+ 寫入這一行 ->
```
GOOGLE_API_KEY = <your-api-key-here>
```
Run the Streamlit app:

`streamlit run app.py`

![image](https://github.com/Trinity-SYT-SECURITY/gemini_chatpdf/assets/96654161/e6a97b43-ada4-4994-9137-7704e8396905)


future work(開發進行中)
----
Set Telegram Bot

+ 參考 : https://z3388638.medium.com/telegram-bot-1-%E6%87%B6%E5%BE%97%E8%87%AA%E5%B7%B1%E5%81%9A%E7%9A%84%E4%BA%8B%E5%B0%B1%E4%BA%A4%E7%B5%A6%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%90%A7-c59004dc6c7b

-> Go to TG find BotFather then chat with it

![image](https://github.com/Trinity-SYT-SECURITY/gemini_chatpdf/assets/96654161/552a4903-36cb-422e-8cac-6561f02f82eb)

+ Input /newbot then follow the step
  
-> When you finish setting up, you will see the following information

![image](https://github.com/Trinity-SYT-SECURITY/gemini_chatpdf/assets/96654161/10c19f6f-fb18-40ca-b301-736566806a0a)

+ 當前根目錄下
`mousepad .env`
+ 新增這一行 ->
```
TELEGRAM_TOKEN = <your_telegram_token_here>
```
