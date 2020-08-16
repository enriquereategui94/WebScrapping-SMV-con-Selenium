from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.smv.gob.pe/Frm_EVCP?data=5A959494701B26421F184C081CACF55BFA328E8EBC")

xpath1 = '//select[@name = "ctl00$MainContent$cboDenominacionSocial"]'
# Selecciona la empresa
select1 = Select(driver.find_element_by_xpath(xpath1)) 
select1.select_by_value('38036')
wait = WebDriverWait(driver, 10)

#Cambiar el valor "0001" para cambiar al Fondo
nFondo = "0001"
xpathFondo = '//option[@value = ' + nFondo + ']'
element = wait.until(EC.presence_of_element_located((By.XPATH, xpathFondo )))

#Selecciona el fondo
xpath2 = '//select[@name = "ctl00$MainContent$cboFondo"]'
select2 = Select(driver.find_element_by_xpath(xpath2))
select2.select_by_value('0001')
print(driver.find_element_by_xpath(xpathFondo).text)

#Selecciona fecha inicio
xpath3 = '//input[@name = "ctl00$MainContent$txtFechDesde"]'
select3 = driver.find_element_by_xpath(xpath3)
select3.clear()
FI = input('Ingrese la fecha en formato "dd/mm/aaaa":')
#FI = "01/08/2020"
select3.send_keys(FI)

#Selecciona fecha final
xpath4 = '//input[@name = "ctl00$MainContent$txtFechHasta"]'
select4 = driver.find_element_by_xpath(xpath4)
select4.clear()
FF = input('Ingrese la fecha en formato "dd/mm/aaaa":')
#FF = "14/08/2020"
select4.send_keys(FF)

#Click buscar
xpathBuscar = '//input[@name = "ctl00$MainContent$btnBuscar"]'
selectBuscar = driver.find_element_by_xpath(xpathBuscar)
selectBuscar.click()

#Seleccionar valores iniciales
xpathTabla = '//table[@id = "MainContent_grdEVCP_grdDetalle_0"]'
element2 = wait.until(EC.presence_of_element_located((By.XPATH, xpathTabla)))
selectFechaI = driver.find_element_by_xpath(xpathTabla + '/tbody/tr[1]/td[1]').text
selectCuotaI = driver.find_element_by_xpath(xpathTabla + '/tbody/tr[1]/td[4]').text
print('Valor cuota el',selectFechaI,'es',selectCuotaI)

#Seleccionar valores finales
selectFechaF = driver.find_element_by_xpath(xpathTabla + '/tbody/tr[last()]/td[1]').text
selectCuotaF = driver.find_element_by_xpath(xpathTabla + '/tbody/tr[last()]/td[4]').text
print('Valor cuota el',selectFechaF,'es',selectCuotaF)

#Variación
var = round((float(selectCuotaF) -float(selectCuotaI))/float(selectCuotaI)*100,2)
print('Variación:', str(var) + '%')

time.sleep(5)
driver.quit()