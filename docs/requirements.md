# 機能要件

## 概要
シンプルな計算 API を Azure Functions（Consumption Plan）で実装する。
ブラウザから GET リクエストでアクセスし、結果をプレーンテキストで返す。開発言語は Python 3.11。

## 前提
- デプロイ先リージョン: Azure 東日本 (Japan East)
- プラン: Azure Functions - Consumption Plan
- ランタイム: Python 3.11
- デプロイ方法: 手動デプロイ
- リソースグループ: calc-api-hands-on-test-maenishi
- 認証: 不要（パブリック）

## エンドポイント（機能要件）
1. GET /multiply
   - 機能: クエリ文字列の `A` と `B` を掛け算して結果を返す
2. GET /divide
   - 機能: クエリ文字列の `A` と `B` を割り算して結果を返す

## パラメータ仕様
- 共通
  - パラメータ名: `A`, `B`
  - 取得方法: クエリ文字列（例: `?A=3&B=4`）
  - 型: 整数のみ（負の数含む）
  - 必須: `A` と `B` は共に必須
  - 不正な型・未指定: エラーとして扱う（下記「エラーハンドリング」参照）

## レスポンス仕様
- 正常時
  - HTTP ステータス: 200 OK
  - Content-Type: `text/plain; charset=utf-8`
  - ボディ: 計算結果のプレーンテキスト（例: `12`）
- エラー時
  - 不正入力（未指定・非整数）: 400 Bad Request
  - 0除算: 400 Bad Request（エラーメッセージをプレーンテキストで返す）
  - サーバー内部エラー: 500 Internal Server Error

## エラーメッセージ例
- 未指定/不正な数値:
  - ステータス: 400
  - ボディ: "Invalid input: A and B must be integers."
- 0除算 (divide の場合):
  - ステータス: 400
  - ボディ: "Division by zero is not allowed."

## 入出力の例
- 掛け算
  - リクエスト: `GET /multiply?A=3&B=4`
  - レスポンス (200): ボディ `12`
- 割り算
  - リクエスト: `GET /divide?A=8&B=2`
  - レスポンス (200): ボディ `4`
- 割り算で 0 除算
  - リクエスト: `GET /divide?A=8&B=0`
  - レスポンス (400): ボディ `Division by zero is not allowed.`

## 受け入れ基準（Acceptance Criteria）
- ブラウザで `https://<function-app>/multiply?A=2&B=3` を開くと `6` が表示される
- ブラウザで `https://<function-app>/divide?A=6&B=2` を開くと `3` が表示される
- 不正入力時および 0 除算時に適切な 400 エラーとプレーンテキストの説明が返る

## 実装メモ（開発者向け）
- HTTP メソッド: GET
- 実装言語: Python 3.11
- ロギング: 例外発生時に最低限のログ出力
- テスト: 単体テストで主要ケース（正常系、非整数、未指定、0除算）をカバーすること

