const { Given, When, Then } = require('cucumber')
const { expect } = require('chai')
const {Builder, By, Key, until} = require('selenium-webdriver');

Given('open register page', function() {
  console.log("open register page");
  this.startBrowser();
  driver=global.driver;
  
  //this.driver.get('https://github.com/');
  driver.get("https://appleid.apple.com/account#!&page=create");
  let country=driver.findElement(By.css('.select-country'));
  let option=country.findElement(By.xpath("//option[@value='ASM']"));
  
})

When('fill the nessary register information', function() {
  let news=driver.findElement(By.id('news'));
  news.click();
  let result=news.isSelected();
})

Then('register successful', function() {
  
})