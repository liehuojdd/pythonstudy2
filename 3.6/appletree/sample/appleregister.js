const {Builder, By, Key, until} = require('selenium-webdriver');

var str="enter user name [admin]";
//var regx = "\[.*\]";
//var regx =new RegExp("/[.*/]");
//console.log(a.match(regx));
//var str = "aaabbbcccaaabbbccc";
//var res = str.match(/aaa/);
//console.log(res);

//var res = str.match(/\[.*\]/);
var res = str.match(/\[(.*?)\]/);
console.log(res[1]);

let driver = new Builder().forBrowser('chrome').build();
const actions = driver.actions({async: true});
const mouse = actions.mouse();

driver.get('https://appleid.apple.com/account#!&page=create');
//let country=driver.findElement(By.id('countryOptions'));
//driver.executeAsyncScript("window.scrollTo(100,1000);");
let country=driver.findElement(By.css('.select-country'));
let option=country.findElement(By.xpath("//option[@value='ASM']"));
//option.click();
//driver.executeScript("alert('a');");
//window.scrollTo(100,1000);
//js="document.documentElement.scrollTop=100000";
let news=driver.findElement(By.id('news'));
news.click();
let result=news.isSelected();

//console.log(result);
//let label=driver.findElement(By.css('.label-small .tk-caption'));
//console.log(label.getText());

