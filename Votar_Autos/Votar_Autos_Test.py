import time
from selenium import webdriver
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


#Variables Globales
USER = "Pruebas_testing1@gmail.com"
PASSWORD = "Pruebaselenium1."

class TestCarVote:
    def __init__(self):
        # Inicializa el navegador con configuración común
        self.server = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument("--headless")
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=self.server, options=self.options)


    def login(self):
        try:
            self.driver.get("https://buggy.justtestit.org/")
            Wait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login"))
            ).send_keys(USER)
            Wait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            ).send_keys(PASSWORD)
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
            ).click()
        except Exception as e:
            print(f"Login failed: {e}")


    def try_vote(self):
        print("")
        print("################# |Inicio de prueba intentar votar sin autenticarse| #################")
        try:
            self.driver.get("https://buggy.justtestit.org/")
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/my-app/div/main/my-home/div/div[3]/div")
                )
            ).click()  
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/my-app/div/main/my-overall/div/div/table/tbody/tr[1]/td[1]/a/img")
                )
            ).click()  
            try:
                Wait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/div/button")
                    )
                ).click()
                print("Prueba fallida: se puede votar sin registrarse")
            except Exception:
                print("Prueba satisfactoria: no se puede votar sin registrarse")
        except Exception as e:
            print(f"Error durante la prueba de voto: {e}")
        print("################# |Final de prueba intentar votar sin autenticarse| #################")


    def only_one_vote(self):
        print("")
        print("################# |Inicio de prueba intentar votar mas de una vez| #################")
        try:
        # Paso 1: Iniciar sesión
            self.login()

            # Paso 2: Navegar al listado de autos
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/my-app/div/main/my-home/div/div[3]/div")
                )
            ).click()

            # Paso 3: Seleccionar un auto
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-overall/div/div/table/tbody/tr[2]/td[1]/a/img"))
            ).click()

            # Paso 4: Realizar un voto inicial
            try:
                Wait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/div/button"))
                ).click()
                print("Voto inicial realizado con éxito.")
            except Exception:
                print("Error: No se pudo realizar el voto inicial.")
                return
            
            time.sleep(5)
            # Paso 5: Intentar votar nuevamente
            try:
                Wait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/div/button"))
                ).click()
                print("Prueba fallida: El sistema permitió votar más de una vez por el mismo auto.")
            except Exception:
                print("Prueba satisfactoria: El sistema no permite votar más de una vez por el mismo auto.")
        except Exception as e:
            print(f"Error durante la prueba: {e}")

        print("################# |Final de prueba intentar votar mas de una vez| #################")


    def vote_comment(self):
        print("")
        print("################# |Inicio de prueba verificar si puedes comentar al votar| #################")
        try:
        # Paso 1: Iniciar sesión
            self.login()

            # Paso 2: Navegar al listado de autos
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/my-app/div/main/my-home/div/div[3]/div")
                )
            ).click()

            # Paso 3: Seleccionar un auto
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-overall/div/div/table/tbody/tr[3]/td[1]/a/img"))
            ).click()

            # Paso 4: Dejar un comentario
            try:
                comment_box = Wait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='comment']"))
                )
                comment_box.send_keys("Este es un comentario de prueba.")
                print("Comentario ingresado exitosamente.")
            except Exception:
                print("Error: No se pudo ingresar el comentario.")
                return

            # Paso 5: Realizar el voto
            try:
                vote_button = Wait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/div/button"))
                )
                vote_button.click()
                print("Voto realizado con éxito.")
            except Exception:
                print("Error: No se pudo realizar el voto.")
                return

            # Paso 6: Validar que el comentario se registró (opcional, depende del sitio)
            try:
                confirmation_message = Wait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/p"))
                )
                if confirmation_message:
                    print("Prueba exitosa: El comentario fue registrado junto con el voto.")
            except Exception:
                print("Prueba fallida: No se confirmó el registro del comentario.")

        except Exception as e:
            print(f"Error durante la prueba: {e}")


        print("################# |Final de prueba verificar si puedes comentar al votar| #################")


    def vote_count_increment(self):
        print("")
        print("################# |Inicio de prueba verificar si incrementa el contador de votar al votar| #################")
        try:
            # Paso 1: Iniciar sesión
            self.login()

            # Paso 2: Navegar al listado de autos
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/my-app/div/main/my-home/div/div[3]/div")
                )
            ).click()

            # Paso 3: Seleccionar un auto
            Wait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-overall/div/div/table/tbody/tr[4]/td[1]/a/img"))
            ).click()

            # Paso 4: Obtener contador actual de votos
            try:
                initial_vote_count = int(
                    Wait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[1]/h4/strong"))
                    ).text
                )
                print(f"Contador inicial de votos: {initial_vote_count}")
            except Exception:
                print("Error: No se pudo obtener el contador de votos inicial.")
                return

            # Paso 5: Realizar el voto
            try:
                Wait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[2]/div/button"))
                ).click()
                print("Voto realizado con éxito.")
            except Exception:
                print("Error: No se pudo realizar el voto.")
                return

            # Paso 6: Verificar que el contador incrementó
            time.sleep(8)  # Esperar a que se actualice el contador (ajustar según sea necesario)
            try:
                updated_vote_count = int(
                    Wait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/my-app/div/main/my-model/div/div[1]/div[3]/div[2]/div[1]/h4/strong"))
                    ).text
                )
                print(f"Contador actualizado de votos: {updated_vote_count}")
                if int(updated_vote_count) == int(initial_vote_count) + 1:
                    print("Prueba exitosa: El contador incrementó correctamente.")
                else:
                    print("Prueba fallida: El contador no incrementó como se esperaba.")
            except Exception:
                print("Error: No se pudo obtener el contador de votos actualizado.")

        except Exception as e:
            print(f"Error durante la prueba: {e}")

        print("################# |Final de prueba verificar si incrementa el contador de votar al votar| #################")


    def cerrar(self):
        time.sleep(3)  # Para observar resultados antes de cerrar
        self.driver.quit()


# Ejecución de pruebas
if __name__ == "__main__":
    test = TestCarVote()
    test.try_vote()
    test.only_one_vote()
    test.vote_comment()
    test.vote_count_increment()
    test.cerrar()