from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # ブラウザを起動
    browser = p.chromium.launch()

    # 新しいブラウザコンテキストを作成
    context = browser.new_context()

    # 新しいページを作成
    page = context.new_page()

    # URLに移動（この例では適切なチェックボックスとラジオボタンがあるページを探してください）
    page.goto("https://example.com/checkboxes_and_radiobuttons")

    # チェックボックスを選択
    page.check("input[type='checkbox'][name='example_checkbox']")

    # ラジオボタンを選択
    page.check("input[type='radio'][name='example_radiobutton']")

    # ブラウザを閉じる
    browser.close()
