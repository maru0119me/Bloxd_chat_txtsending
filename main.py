import requests

# APIエンドポイントURL
url = 'https://api.bloxd.io/send_message'  # ここは実際のURLに置き換えてください

# ヘッダー（必要に応じてAPIキーなどを追加）
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'  # 必要に応じて
}

# メッセージデータ
data = {
    'recipient': 'recipient_id_or_username',  # 宛先のIDまたはユーザー名
    'message': 'Hello, this is a test message!'  # 送信するメッセージ
}

# リクエストを送信
response = requests.post(url, json=data, headers=headers)

# レスポンスの確認
if response.status_code == 200:
    print('Message sent successfully!')
    print('Response:', response.json())
else:
    print('Failed to send message')
    print('Status code:', response.status_code)
    print('Response:', response.text)
