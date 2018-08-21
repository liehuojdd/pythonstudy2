import story from './story.mjs';
import webdriver from 'selenium-webdriver'; 

export default class LoginStory extends story{
    constructor(content){
        console.log("constructor");
        super(content);
        this.username;
        this.password;
        this.expected;
        this.actual;
    }

    When(context){
        super.When(context);
        console.log("when");
        const sub = context.substr(context.indexOf('r')+2,4);
        const account = context.substring(context.indexOf('[')+1,context.length-1);
        sub == 'user' ? this.username = account:this.password = account;
        
    }
    
    Then(context){
      console.log("then");
      super.Then(context);
      let driver= new webdriver.Builder().forBrowser("chrome").build();
      const login_url='https://everdoc.github.io/hellojs/quize/login.html';
      driver.get(login_url);
      driver.findElement(webdriver.By.id('name')).sendKeys("username");
      driver.findElement(webdriver.By.id('password')).sendKeys("password");
      driver.findElement(webdriver.By.tagName('button')).click();
      let b= driver.findElement(webdriver.By.id('result'));
      //b.getText().then(console.log);
      b.getText().then(function(text) {
      console.log(text);
      });
    }
    Play(){
        console.log("play");
        super.Play();
    }

}
let given="Given: open login page";
let when1="When: enter user name [admin]";
let when2="When: enter password [taylor2018]";
let then = "Then: [successful!]";

let arrStory=[given,when1,when2,then];
let story1=new LoginStory(arrStory);
story1.Play(); 