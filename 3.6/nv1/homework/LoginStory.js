import Story from "./Story";
const {Builder, By, Key, until} = require('selenium-webdriver');
const { expect } = require('chai')

class LoginStory extends Story {
    constructor(){
        this.username="";
        this.password="";
        this.expected="";
        this.actual="";
    }
    Given(context) {
        super.Given(context);
    }
    When(context){
        super.When(context);
        this.username=context.match(/name \[(.*?)\]/)[1];
        this.password=context.match(/password \[(.*?)\]/)[1];
    }
    Then(context){
        super.Then(context);
        this.expected=context.match(/\[(.*?)\]/)[1];

        let driver = new Builder().forBrowser('chrome').build();
        driver.get('https://everdoc.github.io/hellojs/quize/login.html');
        driver.findElement(By.id('name')).sendKeys(this.username,Key.RETURN);
        driver.findElement(By.id('password')).sendKeys(this.password,Key.RETURN);
        driver.findElement(By.css('.ui .button')).click();
        driver.sleep(2000);
        this.actual=driver.findElement(By.id('result')).getText();

        if(this.actual.indexOf(this.expected)>0){
            Console.log("The case is PASS");
        }else{
            Console.log("The case is FAIL");
        }
        expect(this.actual.indexOf(this.expected)>0,"The case is FAIL")
    }
    Play(){
        super.Play();
    }
}

let given="Given: open login page";
let when1="When: enter user name [admin]";
let when2="When: enter password [taylor2018]";
let then = "Then: [successful!]";

let arrStory=[given,when1,when2,then];
let loginStory=LoginStory(arrStory);
loginStory.Play();