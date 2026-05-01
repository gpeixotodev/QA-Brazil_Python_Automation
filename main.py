import data
import helpers

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Conectado ao servidor Urban Routes')
        else:
            print('Não foi possível conectar ao Urban Routes.')

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_comfort_icon()
        assert self.page.is_comfort_active()

    def test_fill_phone_number(self):
        print("função criada para definir o numero de telefone")
        pass

    def test_fill_card(self):
        print("função criada para definir o preenchimento de cartao")
        pass

    def test_comment_for_driver(self):
        print("função criada para definir o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        print("função criada para definir as mantas e lençois")
        pass

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2
        for _ in range(numbers_of_ice_creams):
            print("função criada para adicionar a quantidade de sorvetes")
        pass

    def test_car_search_model_appears(self):
        print("função criada para definir o modelo do carro")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
