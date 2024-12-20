# 短期目標
## 1. Base段階
この段階では、[feature.md](https://github.com/moqumo/lib4circle/blob/main/docs/features.md)で定義した
[minimum](https://github.com/moqumo/lib4circle/issues?q=is%3Aissue+is%3Aopen+label%3Aminimum)(最低限の機能)を実装する。   
UI部分のデザインに関してはこだわらず、ユーザーによる入力ができること自体を目標とする。
### フロント側（Svelte）
- ISBN入力のコンポーネント
- 貸出ボタン -> 貸出リクエスト -> 貸出完了画面
- 返却ボタン -> 返却リクエスト -> 返却完了画面
- 登録ボタン -> 登録リクエスト -> 登録完了画面
### サーバー側（Python）
- jsonを用いた簡易的な書籍管理
  - 貸出リクエスト -> Brrowing -> 完了レスポンス
  - 返却リクエスト -> Return -> 完了レスポンス
  - 登録リクエスト -> Registration -> 完了レスポンス

## 2. UI段階
この段階では、ユーザーが使いやすいUIを作成する。   
サーバー側は、この段階での改善は保留する。

## 3. DB段階
この段階では、jsonを用いた書籍管理からDBを用いた書籍管理へ移行する。   
jsonを用いた書籍管理で浮上した課題などを、解決できるようなDB設計を目指す。
- DB設計の学習
- DB設計
- 実装

# 中期目標
## Deploy段階
この段階では、実装したシステムをデプロイする。

## Auth段階
この段階では、認証システムを導入する。

# 長期目標
## 
