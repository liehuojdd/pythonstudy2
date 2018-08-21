const { Given, When, Then } = require('cucumber')
const { expect } = require('chai')
const {Builder, By, Key, until} = require('selenium-webdriver');

Given('open support page', function() {
  console.log("open support page");
  this.startBrowser();
  //console.log("type:"+typeof(global.driver));
  //console.log("type:"+typeof(null));
  //console.log("type:"+typeof(undefined));
  
  //this.startBrowser();
  this.driver=global.driver;
  //driver.get('https://support.apple.com/');
  this.driver.get('https://support.apple.com/');
  
})

When('enter keyword {string}', function(searchword) {
  console.log("enter keyword");
  
  this.driver.findElement(By.css('.ac-gn-link-search')).click();
  this.driver.sleep(4000);
  let searchbox=this.driver.findElement(By.id('ac-gn-searchform-input'));
  searchbox.sendKeys(searchword,Key.ENTER);
  
})

Then('result search out', function() {

})