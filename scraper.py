from bs4 import BeautifulSoup as bs
from playwright.sync_api import sync_playwright


def get_citations_needed_count(url_string):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(slow_mo=500)
        page = browser.new_page()
        page.goto(url_string)

        soup = bs(page.content(), 'html.parser')
        citations_result = soup.find_all(title="Wikipedia:Citation needed")
        print(f"There are {len(citations_result)} citations needed!")
        browser.close()
        return len(citations_result)


def get_citations_needed_report(url_string):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(slow_mo=500)
        page = browser.new_page()
        page.goto(url_string)

        soup = bs(page.content(), 'html.parser')
        citations_result = soup.find_all(title="Wikipedia:Citation needed")

        report = "Citation Report:\n\n"

        for citation in citations_result:
            p_parent = citation.parent.parent.parent
            report += p_parent.text + "\n"

        print(report)
        browser.close()
        return report


if __name__ == "__main__":
    get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    print("\n")
    get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")