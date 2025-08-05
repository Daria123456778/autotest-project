def assert_text_in_element(element, expected_text: str):
    actual_text = element.text
    assert expected_text in actual_text, (
        f'Ожидалось, что "{expected_text}" будет в "{actual_text}"'
    )

def assert_texts_in_elements(elements, expected_text: str):
    """
    Проверяет, что expected_text содержится в каждом из переданных элементов.
    """
    for idx, element in enumerate(elements):
        actual_text = element.text
        assert expected_text in actual_text, (
            f'В элементе #{idx+1} текст "{expected_text}" не найден. Факт: "{actual_text}"'
        )

def assert_elements_count(elements, min_count: int):
    assert len(elements) >= min_count, (
        f'Ожидалось не менее {min_count} элементов, найдено: {len(elements)}'
    )

def assert_in_list(lst, value):
    assert value in lst, f'"{value}" не найден в списке: {lst}'

def assert_url_contains(driver, fragment: str):
    url = driver.current_url
    assert fragment in url, f'В url "{url}" не найдено "{fragment}"'

def assert_attribute_value(element, attribute: str, expected_value):
    actual = element.get_attribute(attribute)
    assert expected_value == actual, (
        f'Ожидал "{expected_value}" в атрибуте "{attribute}", факт: "{actual}"'
    )
