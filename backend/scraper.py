import asyncio
import random
import time
from playwright.async_api import async_playwright
from faker import Faker  # faker helps us scrape data more easily

fake = Faker()


def get_random_user_agent():
    return fake.user_agent()


def random_delay():
    time.sleep(random.uniform(1, 3))


def get_random_proxy():
    proxies = ["http://proxy1.com", "http://proxy2.com", "http://proxy3.com"]
    return random.choice(proxies)


async def search_for_product(page, product_name):
    await page.fill('input[placeholder="Search"]', product_name)
    await page.press('input[placeholder="Search"]', "Enter")
    await page.wait_for_selector(".search-results")
    random_delay()


async def scrape_product_page(page, url):
    await page.goto(url, timeout=60000)
    await page.wait_for_selector("body", timeout=10000)
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    random_delay()
    content = await page.content()
    return content


async def scrape_with_browser(url, product_name):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=get_random_user_agent(),
            http_credentials={"username": "user", "password": "pass"}
            if get_random_proxy()
            else None,
        )
        page = await context.new_page()
        await search_for_product(page, product_name)
        await page.wait_for_selector(".product-card")
        top_shoes = await page.query_selector_all(".product-card")
        products_data = []
        for shoe in top_shoes[:10]:
            shoe_link = await shoe.query_selector("a")
            shoe_url = await shoe_link.get_attribute("href")
            product_data = await scrape_product_page(page, shoe_url)
            products_data.append(product_data)
            random_delay()
        await browser.close()
        return products_data


async def main():
    product_name = "Nike Dunk Low"
    url = f"https://stockx.com/search?s={product_name}"
    products_data = await scrape_with_browser(url, product_name)
    print(products_data[:500])


asyncio.run(main())
