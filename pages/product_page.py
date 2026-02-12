from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.apparel_link = page.get_by_role("link", name="Apparel & accessories")
        self.tshirts_link = page.get_by_role("link", name="T-shirts")
        self.sort_dropdown = page.locator("#sort")
        self.cart_buttons = page.locator(".productcart")

    def go_to_tshirts(self):
        self.apparel_link.hover()
        self.tshirts_link.click()

    def add_two_most_expensive_to_cart(self):
        self.sort_dropdown.select_option(label="Price High > Low")
        self.page.wait_for_load_state("networkidle")

        # Check if there are at least 2 products available
        available_products = self.page.locator(".col-md-3.col-sm-6.col-xs-12").filter(
            has=self.page.locator(".productcart")
        )

        count = available_products.count()
        
        # If there are less than 2, fail the test with a message
        assert count >= 2, f"HIBA: Legalább 2 raktáron lévő pólót vártam, de csak {count} darabot találtam!"

        # Add the two most expensive products to the cart
        for i in range(2):
            product = available_products.nth(i).locator(".productcart")
            product.click()
            
            # Handle redirect to product page by returning to list if necessary
            if "product_id" in self.page.url:
                self.page.locator(".cart").click()
                
                if i == 0:
                    self.navigate("https://automationteststore.com/index.php?rt=product/category&path=68_70")
                    self.sort_dropdown.select_option(label="Price High > Low")
                    self.page.wait_for_load_state("networkidle")
                    
        print(f"Sikeresen kosárba tettem a 2 legdrágábbat a(z) {count} elérhetőből.")