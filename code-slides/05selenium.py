from selenium.webdriver import Firefox
#!
driver = Firefox()
driver.get('https://github.com')
#!
search_box = driver.find_element_by_name('q')
search_box.send_keys('txtorcon')
search_box.submit()
#!
found_repos = driver.find_elements_by_class_name(
    'repo-list-name'
)
assert len(found_repos) >= 1
repo_names = [repo.text for repo in found_repos]
assert 'meejah/txtorcon' in repo_names
