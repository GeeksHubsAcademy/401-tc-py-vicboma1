<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


	Considere el siguiente problema:

	Se quiere desarrollar un pequeño juego llamado 'koso' que traza crucigramas con números.
    El objetivo es rellenar una pequeña cuadrícula de 9x9 dividida en subcruadrículas de 3x3.
    Se utilizan los números del 1 al 9 partiendo de posiciones ya ubicadas en el tablero.
    La finalidad del juego es poder rellenar todos los huecos y saber si es posible resolver
    el crucigrama.


    Algunas de las restricciones que se deben tener, son las siguientes:

    * No se pueden repetir números en la misma subcuadrícula de 3x3
    * No se pueden repetir números en una misma fila de la cuadrícula 9x9
    * No se pueden repetir números en una misma columna de la cuadrícula 9x9


    Cuadrícula
                     9x9

    | x | x | x || x | x | x || x | x | x |                    
    | x | x | x || x | x | x || x | x | x |
	| x | x | x || x | x | x || x | x | x |
	
	| x | x | x || x | x | x || x | x | x |	
	| x | x | x || x | x | x || x | x | x |
	| x | x | x || x | x | x || x | x | x |
	
	| x | x | x || x | x | x || x | x | x |
	| x | x | x || x | x | x || x | x | x |
	| x | x | x || x | x | x || x | x | x |



    Subcuadrícula 
                     3x3                          

                | x | x | x |                     
                | x | x | x |
                | x | x | x |


    Ejemplo:

        Subcuadrícula 
                        3x3                      Solución 1                   Solución 2        

                    | 0 | 0 | 0 |               | 1 | 2 | 3 |               | 6 | 3 | 8 |                             
                    | 4 | 5 | 0 |               | 4 | 5 | 6 |               | 4 | 5 | 7 |  
                    | 0 | 0 | 0 |               | 8 | 9 | 7 |               | 9 | 2 | 1 |  
    
	   
       Cuadrícula 
                        9x9

        Para una mejor comprensión, se denotan los números iniciales del crucigrama con corchetes en el primer paso.
            
            Paso 1

            | 0 | 0 | 0 || 0 | 0 |[9]||[7]| 0 | 0 |                    
            |[4]|[5]| 0 ||[3]| 0 | 0 || 0 |[8]| 0 |
	        | 0 | 0 | 0 ||[4]| 0 |[8]|| 0 | 0 | 0 |
	
	        |[1]| 0 | 0 || 0 | 0 | 0 || 0 | 0 |[6]|	
	        |[8]| 0 | 0 || 0 | 0 | 0 || 0 |[7]|[1]|
	        | 0 | 0 |[3 || 0 | 0 |[6]||[9]| 0 | 0 |
	
	        | 0 | 0 | 0 || 0 |[3]|[7]||[6]| 0 | 0 |
	        | 0 | 0 |[9]|| 0 | 0 | 0 ||[3]| 0 | 0 |
	        | 0 |[8]| 0 || 0 |[5]| 0 || 0 |[1]| 0 |

            Paso 2

            | 6 | 3 | 8 || 0 | 0 | 9 || 7 | 0 | 0 |                    
            | 4 | 5 | 0 || 3 | 0 | 0 || 0 | 8 | 0 |
	        | 9 | 0 | 0 || 4 | 0 | 8 || 0 | 0 | 0 |
	
	        | 1 | 0 | 0 || 0 | 0 | 0 || 0 | 0 | 6 |	
	        | 8 | 0 | 0 || 0 | 0 | 0 || 0 | 7 | 1 |
	        | 7 | 0 | 3 || 0 | 0 | 6 || 9 | 0 | 0 |
	
	        | 2 | 0 | 0 || 0 | 3 | 7 || 6 | 0 | 0 |
	        | 5 | 0 | 9 || 0 | 0 | 0 || 3 | 0 | 0 |
	        | 2 | 8 | 0 || 0 | 5 | 0 || 0 | 1 | 0 |

            Paso 3

            | 6 | 3 | 8 || 0 | 1 | 9 || 7 | 0 | 0 |                    
            | 4 | 5 | 0 || 3 | 6 | 0 || 0 | 8 | 0 |
	        | 9 | 0 | 0 || 4 | 7 | 8 || 0 | 0 | 0 |
	
	        | 1 | 0 | 0 || 0 | 4 | 0 || 0 | 0 | 6 |	
	        | 8 | 0 | 0 || 0 | 9 | 0 || 0 | 7 | 1 |
	        | 7 | 0 | 3 || 0 | 8 | 6 || 9 | 0 | 0 |
	
	        | 2 | 0 | 0 || 0 | 3 | 7 || 6 | 0 | 0 |
	        | 5 | 0 | 9 || 0 | 6 | 0 || 3 | 0 | 0 |
	        | 2 | 8 | 0 || 0 | 5 | 0 || 0 | 1 | 0 |


            Paso X

            ...


            Resolución

            | 6 | 3 | 8 || 5 | 1 | 9 || 7 | 2 | 4 |                    
            | 4 | 5 | 7 || 3 | 6 | 2 || 1 | 8 | 9 |
	        | 9 | 2 | 1 || 4 | 7 | 8 || 5 | 6 | 3 |
	
	        | 1 | 9 | 2 || 7 | 4 | 5 || 8 | 3 | 6 |	
	        | 8 | 6 | 5 || 2 | 9 | 3 || 4 | 7 | 1 |
	        | 7 | 4 | 3 || 1 | 8 | 6 || 9 | 5 | 2 |
	
	        | 2 | 1 | 4 || 8 | 3 | 7 || 6 | 9 | 5 |
	        | 5 | 7 | 9 || 2 | 6 | 1 || 3 | 4 | 8 |
	        | 2 | 8 | 6 || 9 | 5 | 4 || 2 | 1 | 7 |


    Ouput = true

    
    Notas:
    * El algoritmo debe de ser óptimo.
    * No se contemplan cuadrículas que no sean 9x9.
    * Las posiciones vacías se denotan con un 0.
    * El input de entrada es una Array bidimensional.


    En la carpeta 'src/kata.py' se encuentra el fichero con la 
    definición de nuestro método vacío.
    En la carpeta 'tests/kata_test.py' se encuentra el fichero 
    con la suite de test.
    
    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.

	tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [  4%]
	tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [  8%]
	tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 12%]
	tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 16%]
	tests/test_kata.py::Test_kata::test_apply_13 PASSED                      [ 20%]
	tests/test_kata.py::Test_kata::test_apply_14 PASSED                      [ 25%]
	tests/test_kata.py::Test_kata::test_apply_15 PASSED                      [ 29%]
	tests/test_kata.py::Test_kata::test_apply_16 PASSED                      [ 33%]
	tests/test_kata.py::Test_kata::test_apply_17 PASSED                      [ 37%]
	tests/test_kata.py::Test_kata::test_apply_18 PASSED                      [ 41%]
	tests/test_kata.py::Test_kata::test_apply_19 PASSED                      [ 45%]
	tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 50%]
	tests/test_kata.py::Test_kata::test_apply_20 PASSED                      [ 54%]
	tests/test_kata.py::Test_kata::test_apply_21 PASSED                      [ 58%]
	tests/test_kata.py::Test_kata::test_apply_22 PASSED                      [ 62%]
	tests/test_kata.py::Test_kata::test_apply_23 PASSED                      [ 66%]
	tests/test_kata.py::Test_kata::test_apply_24 PASSED                      [ 70%]
	tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 75%]
	tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 79%]
	tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 83%]
	tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 87%]
	tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 91%]
	tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 95%]
	tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]

    Process finished with exit code 0



## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
