var {setWorldConstructor} = require('cucumber');
var seleniumWebdriver = require('selenium-webdriver');
var _global;

function CustomTest() {

  // Returns a promise that resolves to the element
  this.waitForElement = function(locator) {
    var condition = seleniumWebdriver.until.elementLocated(locator);
    return this.driver.wait(condition)
  }
  this.startBrowser=function(){
    //console.log("startBrowser");
    //console.log("type:"+typeof(global.driver));
    //global.driver=new seleniumWebdriver.Builder().forBrowser('chrome').build();
      if(typeof(global.driver)=="undefined"){
        console.log("start new driver");
        global.driver=new seleniumWebdriver.Builder().forBrowser('chrome').build();
      }
      
  }
}

var buildChromeDriver = function() {
  return new seleniumWebdriver.Builder().forBrowser("chrome").build();
  
};

class DoNothing{

}

class CustomWorld {
  constructor() {
    this.variable = 0
    //this.driver = buildChromeDriver();
    console.log(this.driver);
    
    if(typeof(this.driver) == "undefined"){
      console.log("new driver");
      this.driver=new seleniumWebdriver.Builder()
      .forBrowser('chrome')
      .build();
    }
    /*
    this.driver=new seleniumWebdriver.Builder()
      .forBrowser('chrome')
      .build();
      */
  }

  setTo(number) {
    this.variable = number
  }

  incrementBy(number) {
    this.variable += number
  }
}

setWorldConstructor(CustomTest)