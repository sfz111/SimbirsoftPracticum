import allure

@allure.title("Кейс: Работа с полями и формами")
def test_form_filling(driver, form_page):
    form_page.open(url='https://practice-automation.com/form-fields/')

    form_page.input_name(name='Владимир')
    form_page.input_password(password='123')

    form_page.select_checkbox_milk()
    form_page.select_checkbox_coffee()

    form_page.select_yellow_radio_btn()

    form_page.select_in_dropdown(value='yes')

    form_page.input_email(email='VladimirSkufin@example.com')
    form_page.input_message()

    form_page.click_submit()

    expected_text = 'Message received!'
    actual_text = form_page.get_alert_text()
    assert actual_text == expected_text, f"Ожидаемый текст в алерте: {expected_text}. Фактический текст: {actual_text}"










