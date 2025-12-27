import asyncio
from playwright.async_api import async_playwright, Browser, Page
from mcp.server.fastmcp import FastMCP

browser: Browser = None # type: ignore
page: Page = None # type: ignore
playwright_instance = None

mcp = FastMCP("playwright-mcp-server")

async def _ensure_browser():
    """ Ensure browser and page are initialized"""
    global browser, page, playwright_instance
    
    if browser is None or page is None:
        playwright_instance = await async_playwright().start()
        browser = await playwright_instance.chromium.launch(headless=False)
        page = await browser.new_page()
        
@mcp.tool()
async def navigate(url: str) -> str:
    "Navigate to the given URL"
    
    try:
        await _ensure_browser()
        await page.goto(url, wait_until="domcontentloaded")
        title = await page.title()
        return f"Navigated to: {url}\n Page title: {title}"
    except Exception as e:
        return f"Error navigating to {url}: {e}"
    
@mcp.tool()
async def browser_close() -> str:
    "Closing the browser on the page"
    
    global browser, page, playwright_instance  # Add this line
    
    try:
        if browser:  # Check if browser exists before closing
            await browser.close()
            # Reset the global variables
            browser = None # type: ignore
            page = None    # type: ignore
            if playwright_instance:
                await playwright_instance.stop()
                playwright_instance = None
            return "Closed the browser"
        else:
            return "Browser is already closed"
    except Exception as e:
        return f"Error closing browser: {e}"
    

@mcp.tool()
async def click(selector: str) -> str:
    "Click an element on the page"
    
    try:
        await _ensure_browser()
        await page.click(selector)
        return f"Clicked the element : {selector}"
    except Exception as e:
        return f"Error clicking element {selector}: {e}"

@mcp.tool()
async def get_page_title() -> str:
    """Get the current page title."""
    try:
        await _ensure_browser()
        title = await page.title()
        return f"Page title: {title}"
    except Exception as e:
        return f"Error getting page title: {e}"    

if __name__ == "__main__":
    try:
        mcp.run()
    finally:
        if browser:
            asyncio.run(browser.close())
        if playwright_instance:
            asyncio.run(playwright_instance.stop())
        print("Playwright MCP Server is running and resources are cleaned up.")