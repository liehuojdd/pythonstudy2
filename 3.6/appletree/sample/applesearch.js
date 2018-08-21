const {Builder, By, Key, until} = require('selenium-webdriver');

let driver = new Builder().forBrowser('chrome').build();
driver.get('https://support.apple.com/');
driver.findElement(By.css('.ac-gn-link-search')).click();
driver.sleep(4000);
let searchbox=driver.findElement(By.id('ac-gn-searchform-input'));
searchbox.sendKeys('apple id',Key.ENTER);
//driver.sendKeys(Key.PAGE_DOWN);
