# VocaLeague

## 概要
* Windows OSでの稼働を想定
* `vocaleague.bat start` で起動

## .env
* BOT_TOKEN
* POSTGRES_USER
* POSTGRES_PASSWORD
* POSTGRES_DB

## コマンド
* `/start` : チャンネル接続
* `/vq [思考秒数=10] [連続回数=1]` : ゲーム開始
* `/point [ユーザーメンション] : 現在の所持ポイントの確認
* `/join` ゲームへのユーザー登録（問題に正解すれば、自動的に登録される）
