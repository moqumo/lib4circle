# 機能
minimum: 最低限実装する機能   
enhance: 最低限が完成してから追加していく機能
## 貸出機能
### 1. 本を探す
以下のパターンで本を探す
- サークル室の本棚にある本のISBNを入力する。(minimum)
  - （最終的にバーコード読み取りで行う。(enhance)）
- 登録された本の一覧から探す。(enhance) <- 現地にいることの証明として、この機能はない方がよいかも
### 2. 本を選択 -> 貸出申請
もしその本が登録されていて、未貸出であれば、貸出す。(minimum)
貸出期間を入力。(enhance)

## 返却機能
### 1. 本を読み取る
- 返却する本のISBNを入力する。(minimum)
  - （最終的にバーコード読み取りで行う。(enhance)）
### 2. 本を返却する
- 返却処理をし、貸出可能な状態にする。(mininum)

## 登録機能
### 1. 本を読み取る
- 登録する本のISBNを入力する。(minimum)
  - （最終的にバーコード読み取りで行う。(enhance)）
- もしAPI側で登録されていないISBNの場合
  - 書籍情報（タイトル、著者、出版社）を手打ちしてもらう(enhance)
- もし既に登録されている場合
  - 二冊目の場合であるなら、登録冊数を増やす。
### 2. 貸出期間の設定 (enhance)
- デフォルトは2週間とするが、ユーザーのオプションで設定できるようにする。
### 3. 登録 (minimum)
  
## ユーザー登録
### 1. 認証サービスを使って認証する。
### 2. ユーザー名（ハンドルネーム＆本名）

# セキュリティ
## 懸念されること
- 返却していないのにも関わらず、返却されてしまう。
  - 少なくともサークル室にいることを何らかの方法で確かめる必要あり。(enhance)
