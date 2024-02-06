from apify_client import ApifyClient
import json

apify_api_token = "ask gal"
client = ApifyClient(apify_api_token)

run_input = {
    "startUrls": [
        { "url":"https://www.mako.co.il/news-military?page=1"}
        #url's
        ],
    "crawlerType": "playwright:firefox",
    "includeUrlGlobs": [],
    "excludeUrlGlobs": [],
    "ignoreCanonicalUrl": False,
    "maxCrawlDepth": 1,
    "maxCrawlPages": 5, #limit
    "initialConcurrency": 0,
    "maxConcurrency": 100,
    "initialCookies": [],
    "proxyConfiguration": { "useApifyProxy": True },
    "maxSessionRotations": 10,
    "maxRequestRetries": 5,
    "requestTimeoutSecs": 10,
    "dynamicContentWaitSecs": 10,
    "maxScrollHeightPixels": 5000,
    "removeElementsCssSelector": """nav, footer, script, style, noscript, svg,
[role=\"alert\"],
[role=\"banner\"],
[role=\"dialog\"],
[role=\"alertdialog\"],
[role=\"region\"][aria-label*=\"skip\" i],
[aria-modal=\"true\"]""",
    "removeCookieWarnings": True,
    "clickElementsCssSelector": "[aria-expanded=\"false\"]",
    "htmlTransformer": "readableText",
    "readableTextCharThreshold": 100,
    "aggressivePrune": False,
    "debugMode": False,
    "debugLog": False,
    "saveHtml": False,
    "saveMarkdown": False,
    "saveFiles": False,
    "saveScreenshots": False,
    "maxResults": 9999999,
}

run = client.actor("aYG0l9s7dbB7j3gbS").call(run_input=run_input)

items_list = []

items = client.dataset(run["defaultDatasetId"]).iterate_items()
for item in items:
    url = item.get("url")
    if not url.startswith("https://www.mako.co.il/news-military?page=1"):
        items_list.append(item)

with open('scraped_data.json', 'w', encoding='utf-8') as f:
    json.dump(items_list, f, ensure_ascii=False, indent=4)

print("done!")
