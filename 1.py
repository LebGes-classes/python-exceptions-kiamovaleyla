class ProductCard:
    """
    Класс карточки товара.

    Attributes:
        id (int): Уникальный идентификатор товара
        name (str): Название товара
        quantity (str): Количество товара
        condition (str): Состояние товара (новое/б/у)
        supplier (str): Поставщик
        manufacturer (str): Производитель
        cost (str): Цена
        location (str): Местоположение на складе
        weight (str): Вес в кг
        brand (str): Бренд
        date_of_manufacture (str): Дата изготовления
        expiration_date (str): Срок годности
        status (str): Статус товара
    """

    def __init__(self, name, quantity, condition, supplier,
                 manufacturer, cost, location, weight,
                 brand, date_of_manufacture, expiration_date):
        """
        Инициализация карточки товара.
        """
        self.id = id(self)
        self.name = name
        self.quantity = quantity
        self.condition = condition
        self.supplier = supplier
        self.manufacturer = manufacturer
        self.cost = cost
        self.location = location
        self.weight = weight
        self.brand = brand
        self.date_of_manufacture = date_of_manufacture
        self.expiration_date = expiration_date
        self.status = "на складе"

    # Геттеры
    def get_name(self):
        """Получить название товара."""
        return self.name

    def get_quantity(self):
        """Получить количество товара."""
        return self.quantity

    def get_condition(self):
        """Получить состояние товара."""
        return self.condition

    def get_supplier(self):
        """Получить поставщика."""
        return self.supplier

    def get_manufacturer(self):
        """Получить производителя."""
        return self.manufacturer

    def get_cost(self):
        """Получить цену товара."""
        return self.cost

    def get_location(self):
        """Получить местоположение товара."""
        return self.location

    def get_weight(self):
        """Получить вес товара."""
        return self.weight

    def get_brand(self):
        """Получить бренд товара."""
        return self.brand

    def get_date_of_manufacture(self):
        """Получить дату изготовления."""
        return self.date_of_manufacture

    def get_expiration_date(self):
        """Получить срок годности."""
        return self.expiration_date

    def get_status(self):
        """Получить статус товара."""
        return self.status

    # Сеттеры
    def set_name(self, name):
        """
        Установить название товара.

        Args:
            name (str): Новое название
        """
        self.name = name

    def set_quantity(self, quantity):
        """
        Установить количество товара.

        Args:
            quantity (str): Новое количество
        """
        self.quantity = quantity

    def set_condition(self, condition):
        """
        Установить состояние товара.

        Args:
            condition (str): Новое состояние
        """
        self.condition = condition

    def set_supplier(self, supplier):
        """
        Установить поставщика.

        Args:
            supplier (str): Новый поставщик
        """
        self.supplier = supplier

    def set_manufacturer(self, manufacturer):
        """
        Установить производителя.

        Args:
            manufacturer (str): Новый производитель
        """
        self.manufacturer = manufacturer

    def set_cost(self, cost):
        """
        Установить цену товара.

        Args:
            cost (str): Новая цена
        """
        self.cost = cost

    def set_location(self, location):
        """
        Установить местоположение товара.

        Args:
            location (str): Новое местоположение
        """
        self.location = location

    def set_weight(self, weight):
        """
        Установить вес товара.

        Args:
            weight (str): Новый вес
        """
        self.weight = weight

    def set_brand(self, brand):
        """
        Установить бренд товара.

        Args:
            brand (str): Новый бренд
        """
        self.brand = brand

    def set_date_of_manufacture(self, date):
        """
        Установить дату изготовления.

        Args:
            date (str): Новая дата изготовления
        """
        self.date_of_manufacture = date

    def set_expiration_date(self, date):
        """
        Установить срок годности.

        Args:
            date (str): Новый срок годности
        """
        self.expiration_date = date

    def set_status(self, status):
        """
        Установить статус товара.

        Args:
            status (str): Новый статус
        """
        self.status = status

    def show_info(self):
        """
        Показать информацию о товаре.
        """
        print(f"\n--- Товар #{self.id} ---")
        print(f"Название: {self.name}")
        print(f"Количество: {self.quantity}")
        print(f"Состояние: {self.condition}")
        print(f"Поставщик: {self.supplier}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Цена: {self.cost} руб.")
        print(f"Место: {self.location}")
        print(f"Вес: {self.weight} кг")
        print(f"Бренд: {self.brand}")
        print(f"Дата изготовления: {self.date_of_manufacture}")
        print(f"Срок годности: {self.expiration_date}")
        print(f"Статус: {self.status}")

    def write_off(self):
        """
        Списание товара.
        """
        if self.status != "на складе":
            raise Exception(f"Нельзя списать! Статус: {self.status}")

        self.status = "списано"
        return True


def create_card():
    """
    Создание новой карточки товара.
    """
    name = input("Название: ")
    quantity = input("Количество: ")
    condition = input("Состояние (новое/б/у): ")
    supplier = input("Поставщик: ")
    manufacturer = input("Производитель: ")
    cost = input("Цена: ")
    location = input("Местоположение: ")
    weight = input("Вес (кг): ")
    brand = input("Бренд: ")
    date = input("Дата изготовления: ")
    exp_date = input("Срок годности: ")

    return ProductCard(
        name, quantity, condition, supplier,
        manufacturer, cost, location, weight,
        brand, date, exp_date
    )


def edit_card(card):
    """
    Редактирование карточки товара.

    Args:
        card (ProductCard): Объект карточки для редактирования
    """
    print("\n(Enter - оставить без изменений)")

    name = input(f"Название [{card.get_name()}]: ")
    if name:
        card.set_name(name)

    quantity = input(f"Количество [{card.get_quantity()}]: ")
    if quantity:
        card.set_quantity(quantity)

    cost = input(f"Цена [{card.get_cost()}]: ")
    if cost:
        card.set_cost(cost)

    location = input(f"Местоположение [{card.get_location()}]: ")
    if location:
        card.set_location(location)

    print("Карточка обновлена!")


def main():
    """Главное меню программы."""
    products = []

    while True:
        print("\nМЕНЮ УПРАВЛЕНИЯ ТОВАРАМИ")
        print("1. Создать карточку")
        print("2. Показать все товары")
        print("3. Найти товар по ID")
        print("4. Редактировать товар")
        print("5. Списать товар")
        print("6. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            product = create_card()
            products.append(product)
            print(f"Товар создан! ID: {product.id}")

        elif choice == "2":
            if not products:
                print("Список товаров пуст")
            else:
                for product in products:
                    product.show_info()

        elif choice == "3":
            try:
                search_id = int(input("Введите ID товара: "))
                found = False
                for product in products:
                    if product.id == search_id:
                        product.show_info()
                        found = True
                        break
                if not found:
                    print("Товар не найден")
            except ValueError:
                print("Ошибка ввода ID")

        elif choice == "4":
            try:
                edit_id = int(input("Введите ID товара: "))
                found = False
                for product in products:
                    if product.id == edit_id:
                        edit_card(product) # Вызов функцию редактирования
                        found = True
                        break

                if not found:
                    print("Товар не найден")
            except ValueError:
                print("Ошибка ввода ID")

        elif choice == "5":
            try:
                write_id = int(input("Введите ID товара: "))
                found = False
                for product in products:
                    if product.id == write_id:
                        try:
                            product.write_off()
                            print("Товар списан!")
                            product.show_info()
                        except Exception as e:
                            print(f"Ошибка: {e}")
                        found = True
                        break

                if not found:
                    print("Товар не найден")
            except ValueError:
                print("Ошибка ввода ID")

        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")


main()

