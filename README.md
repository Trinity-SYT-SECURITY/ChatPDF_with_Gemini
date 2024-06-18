install git

`sudo apt install git`

Download project

`git clone https://github.com/Trinity-SYT-SECURITY/ChatPDF_with_Gemini.git`

Go to the bottom of the file directory

`cd ChatPDF_with_Gemini`

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

+ 請修改 `.env` 檔案內容，加入你的gemini api

`mousepad .env`

+ 寫入這一行 ->
```
GOOGLE_API_KEY = <your-api-key-here>
```
Run the Streamlit app:

`streamlit run app.py`

![image](https://github.com/Trinity-SYT-SECURITY/gemini_chatpdf/assets/96654161/e6a97b43-ada4-4994-9137-7704e8396905)

Ask the question

```
What is the outline of the content of this document?

What is the title of this paper?

What technology does XXXX use?

....

```


[公司內部技術分享-資安大會延伸內容.pdf](https://github.com/user-attachments/files/15883656/-.pdf)

