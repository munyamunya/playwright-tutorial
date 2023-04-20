# CodespacesでPythonを使ったPlaywrightによるE2Eテスト（リモートブラウザの確認）

このガイドでは、リモートデバッグを使用して、Python用のPlaywrightライブラリを使ったE2Eテストを実行し、Codespaces環境でリモートマシンで開いたブラウザに接続してローカルでブラウザの動作を確認する方法を説明します。

## ステップ1: ポートフォワーディングの設定

1. Codespacesのターミナルで、リモートブラウザインスタンスが起動できるように、環境変数を設定します。
   export PLAYWRIGHT_BROWSERS_PATH=0

2. Visual Studio Codeの左側のメニューから、リモートエクスプローラーを開きます。

3. "Forwarded Ports" セクションを展開し、"Forward a Port" ボタンをクリックします。

4. ポート番号 "9222" を入力し、Enterキーを押します。これにより、9222ポートでリモートブラウザに接続できるようになります。


## ステップ2: テストスクリプトの更新
test_e2e.pyファイルを開いて、ブラウザの起動方法を更新し、launch()メソッドにheadless=Falseおよびslow_mo=1000オプションを追加します。さらに、executablePathオプションを追加し、リモートブラウザインスタンスに接続できるようにします。

browser = p.chromium.launch(headless=False, slow_mo=1000, executablePath="http://localhost:9222")

## ステップ3: テストの実行
Visual Studio Codeのデバッグ機能を使って、テストスクリプトを実行します。左サイドバーのデバッグアイコンをクリックし、デバッグ設定を選択または作成し、再生ボタンをクリックしてデバッグを開始します。