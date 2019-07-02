
assert abs(-42) == -42, "Should be absolute value of a number"
assert self.is_element_present('create_class_button', timeout=30), "No create class button"
assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

"Wrong text, got" + actual_result + ", something wrong"

https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

"Let's count together! {}, then goes {}, and then {}".format("one", "two", "three")

catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", "Wrong language, got" + catalog_text + "instead of 'Каталог'" 


name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")
# Вывод: 'Hello, Eric. You are 74.'

def test_input_text(expected_result, actual_result):
	assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}" 




s = 'My Name is Julia'
if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print('Substring found at index {}'.format(index))

assert "login" in browser.current_url, # сообщение об ошибке





assert some_value in fulltext, f"expected {some_value} to be substring of {fulltext}" 


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected {substring} to be substring of {full_string}"












