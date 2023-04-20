from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # ブラウザを起動
    browser = p.chromium.launch()

    # 新しいブラウザコンテキストを作成
    context = browser.new_context()

    # 新しいページを作成
    page = context.new_page()

    # URLに移動
    page.goto("https://www.wikipedia.org/")

    # 入力フィールドにテキストを入力
    page.fill("input[type='search']", "Python")

    # 検索ボタンをクリック
    page.click("button[type='submit']")

    # ブラウザを閉じる
    browser.close()