# Проект UI автотестов qa-practice.com  

[![LinkedIn Badge](https://img.shields.io/badge/-@rafaelalykov-blue?style=flat&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/rafaelalykov/) [![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:rafaelalykov@gmail.com)

### Технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
</p>



### Тестируем

* Ввод email, password, тексты
* Нажатие кнопок
* Выбор чекбоксов
* Айфреймы
* Драгндроп
* Окна уведомления
* Открытин новых окон
* Выбор селектов


___

##### Создем файл conftest.py, куда импортируем Selenium и Pytest и создаем фикстуру с вызовом chromedrive.
<p  align="center">
  <code><img width="100%" title="Pycharm" src="images/pycharm_screenshots/pycharm_conftest.png"></code>
</p>

##### Также создем basepage.py, обозначаем класс BasePage для вызова функций.
<p  align="center">
  <code><img width="100%" title="Pycharm" src="images/pycharm_screenshots/pycharm_basepage.png"></code>
</p>

##### Пишем тесты к каждой функциональности сайта и создаем классы в папке pages, для вызова функций поиска, клика и др.
<p  align="center">
  <code><img width="100%" title="Pycharm" src="images/pycharm_screenshots/pycharm_test_alert.png"></code>
  <code><img width="100%" title="Pycharm" src="images/pycharm_screenshots/pycharm_alert.png"></code>
</p>

##### После тестов, результаты можно увидеть в Allure отчете
<p  align="center">
  <code><img width="100%" title="Pycharm" src="images/allure_screenshots/allure_graphs.png"></code>
  <code><img width="100%" title="Pycharm" src="images/allure_screenshots/allure_dashboard.png"></code>
  <code><img width="100%" title="Pycharm" src="images/allure_screenshots/allure_suites_1.png"></code>
  <code><img width="100%" title="Pycharm" src="images/allure_screenshots/allure_suites_2.png"></code>
</p>