from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # ブラウザを起動
    browser = p.chromium.launch()

    # 新しいブラウザコンテキストを作成
    context = browser.new_context()

    # 新しいページを作成
    page = context.new_page()

    # URLに移動（この例では適切なセレクトボックスがあるページを探してください）
    page.goto("https://example.com/select_dropdown")

    # セレクトボックスのオプションを選択
    page.select_option("select[name='example_select']", "value_to_select")

    # ブラウザを閉じる
    browser.close()
