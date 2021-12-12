```bash
$ curl https://www.sahamyab.com/guest/twiter/list?v=0.1
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

```bash
$ curl -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1
{"errorCode":"0000","errorTitle":"ثبت موفق","success":true,"hasMore":true,"items":[{"id":"233243525","sendTime":"2021-02-13T12:58:11Z","sendTimePersian":"1399/11/25 16:28","senderName":"سهام دار توانا","senderUsername":"1350sa","senderProfileImage":"default","content":"#وهنر این سهم هیچ ترسی نداره 
...سهمی که هر روز بالای هشتاد میل خریدار داره آیا ترس داره ؟؟؟ امروز آخ
```

```bash
$ sudo apt install jq
```

```bash
curl -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 15231    0 15231    0     0  23396      0 --:--:-- --:--:-- --:--:-- 23396
{
  "errorCode": "0000",
  "errorTitle": "ثبت موفق",
  "success": true,
  "hasMore": true,
  "items": [
    {
      "id": "233242523",
      "sendTime": "2021-02-13T12:51:31Z",
      "sendTimePersian": "1399/11/25 16:21",
      "senderName": "علی گودرزی",
      "senderUsername": "hamfekran123",
      "senderProfileImage": "3d0ab382-ecae-46b1-9a09-fa45c317edc0",
      "content": "#نهال پیغامش اومد فردا باز میشه در سایت  بورس کالا ...فردا باز میشه",
      "type": "twit",
      "mediaContentType": "application/pdf",
      "fileUid": "d2d9b505-ad5e-4b4a-b159-b666abf7dc7f",
      "scoredPostDate": "1613220768343",
      "finalPullDatePersian": ""
    },
    ....
```

```bash
$ curl -s -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items'
[
  {
    "id": "233244469",
    "sendTime": "2021-02-13T13:04:18Z",
    "sendTimePersian": "1399/11/25 16:34",
    "senderName": "همایون",
    "senderUsername": "bors1212",
    "senderProfileImage": "default",
    "content": "#پالایش (حمایت و مقاومت مهم پالایشی یکم کجاست؟\nحمایت مهم بر روی قیمت ۵۱.۴۰۰ ریال و مقاومت مهم این سهم بر روی قیمت ۱۰۰.۰۰۰ ریال می‌باشد.\n\nپالایشی یکم\n \nهر چند که تابلو پالایشی یکم در روز سه شنبه و روز‌های معاملاتی هفته جاری، تقریبا نشان دهنده آغاز یک روند صعودی بوده است، اما به نظر می‌رسد که باز هم باید منتظر ماند و دید که سهامداران بعد از رسیدن این سهم به قیمت ۱۰ هزار تومان چه واکنشی را از خود نشان می‌دهند. آیا باز هم عرضه‌ها افزایش خواهد یافت و یا اینکه این بار با قدرت پالایشی یکم از ده هزار تومان عبور خواهد کرد و روند صعودی جدیدی دوباره آغاز خواهد شد.)\nدوستان به سلامتی و قدرت مقاومت ۱۰۰۰۰۰ را پشت سر گذاشته و با امید به خدا اهداف بالاتر را طلب می کنیم تا چند روز آینده خیالتون از این سهم راحت باشه.",
    "type": "twit",
    "scoredPostDate": "1613221521540",
    "finalPullDatePersian": ""
  },
  ....
```

```bash

```

```bash
$ curl -s -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items[] | [.id, .sendTime, .sendTimePersian, .senderName, .senderUsername, .type, .content] | join(",") ' 

$ date +%s

$ curl -s -H "User-Agent:Chrome/81.0" https://www.sahamyab.com/guest/twiter/list?v=0.1 | jq '.items[] | [.id, .sendTime, .sendTimePersian, .senderName, .senderUsername, .type, .content] | join(",") ' > stage/$(date +%s).csv

$ ls -lh stage


```

