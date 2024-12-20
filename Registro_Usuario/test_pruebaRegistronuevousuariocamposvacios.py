# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPruebaRegistronuevousuariocamposvacios():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pruebaRegistronuevousuariocamposvacios(self):
    self.driver.get("https://buggy.justtestit.org/")
    self.driver.set_window_size(1072, 816)
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.ID, "firstName").click()
    self.driver.find_element(By.ID, "firstName").send_keys("Nombre1")
    self.driver.find_element(By.ID, "lastName").click()
    self.driver.find_element(By.ID, "lastName").send_keys("Nombre2")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Contraseña1*")
    self.driver.find_element(By.ID, "confirmPassword").click()
    self.driver.find_element(By.ID, "confirmPassword").send_keys("Contraseña1*")
    elements = self.driver.find_elements(By.XPATH, "//input[@id=\'username\' and contains(@class, \'ng-invalid\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".img-fluid")
    assert len(elements) > 0
  
