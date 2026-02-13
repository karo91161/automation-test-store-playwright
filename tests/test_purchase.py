import time
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from pages.product_page import ProductPage
from config import CREATE_ACCOUNT_URL, CART_URL

def test_registration_and_purchase_e2e(page: Page):
    timestamp = int(time.time())
    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "email": f"testuser{timestamp}@example.com",
        "address": "Street 1",
        "city": "London",
        "region": "Greater London",
        "postcode": "12345",
        "login_name": f"user_{timestamp}",
        "password": "Password123!"
    }

    # Registration
    reg_page = RegistrationPage(page)
    reg_page.navigate(CREATE_ACCOUNT_URL)
    reg_page.fill_registration_form(user_data)

    expect(page.locator(".maintext")).to_contain_text("Your Account Has Been Created!")
    print(f"\nSikeresen regisztrált felhasználó: {user_data['login_name']}")
    
    # Select the two most expensive t-shirts and add to cart
    product_page = ProductPage(page)
    product_page.go_to_tshirts()
    product_page.add_two_most_expensive_to_cart()
    print("\nKiválasztottuk a két legdrágább pólót és hozzáadtuk a kosárhoz.")

    # Proceed to checkout and confirm the order
    reg_page.navigate(CART_URL)
    page.locator("#cart_checkout1").click()
    page.get_by_role("button", name="Confirm Order").click()
    print("\nRendelés megerősítése megtörtént.")

    expect(page.locator(".maintext")).to_contain_text("Your Order Has Been Processed!")
    print("\nRendelés sikeresen leadva!")