import * as fs from "fs";
import {NodeHtmlMarkdown} from "node-html-markdown";
import {Browser, Page, PuppeteerWebBaseLoader} from "langchain/document_loaders/web/puppeteer";

console.log('creating loader...')
const loader = new PuppeteerWebBaseLoader("https://brain.overment.com", {
    launchOptions: {
        headless: "new",
    },
    gotoOptions: {
        waitUntil: "domcontentloaded",
    },
    async evaluate(page: Page, browser: Browser) {
        // @ts-ignore
        const result = await page.evaluate(() => document.querySelector('.main').innerHTML);
        return NodeHtmlMarkdown.translate(result);
    },
});

console.log('loader:', loader)
console.log('Loading...')
const docs = await loader.load();
console.log('..loaded:', docs)

docs.forEach((doc) => {
    let i = 1;
    const urlToPlaceholder: { [key: string]: string } = {};

    /*
    doc.pageContent = doc.pageContent.replace(/((http|https):\/\/[^\s]+|\.\/[^\s]+)(?=\))/g, (url) => {
        if (!urlToPlaceholder[url]) {
            const placeholder = `$${i++}`;
            urlToPlaceholder[url] = placeholder;
            doc.metadata[placeholder] = url;
        }
        return urlToPlaceholder[url];
    });
    */
});
console.log(docs.length)

fs.writeFileSync("12_web/docs_tr.json", JSON.stringify(docs, null, 2));