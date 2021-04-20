package hk.cloudcall.seleniumtest;

import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.net.MalformedURLException;
import java.net.URL;

@SpringBootApplication
public class SeleniumTestApplication {

    public static void main(String[] args) throws Exception {
        //SpringApplication.run(SeleniumTestApplication.class, args);

        // Selenium Grid 的地址
        URL hubUrl = new URL("http://192.168.1.70:4444/wd/hub");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("headless");       // headless mode
        options.addArguments("disable-gpu");

        // 在 Java 里， Options 派生于 MutableCapabilities 可以用 options 直接启动。Python 不行
        //WebDriver driver = new RemoteWebDriver(hubUrl,options);

        // 或者转换为 DesiredCapabilities 启动
        DesiredCapabilities capabilities = DesiredCapabilities.chrome();
        capabilities.setCapability(ChromeOptions.CAPABILITY, options);
        WebDriver driver = new RemoteWebDriver(hubUrl,capabilities);

        driver.get("https://www.baidu.com");

        System.out.println(driver.getTitle());

        //强制等待3秒
        Thread.sleep(3000);

        driver.quit();
        System.out.println("done");
    }

}
