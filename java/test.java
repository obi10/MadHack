public class test {

	

	public static void main(String[] args) {


		class Animal {
			//atributos
			String tipo;
			int num_patas;
			String habitat;

			//constructor
			Animal(String tipo, int num_patas, String habitat) {
				this.tipo = tipo;
				this.num_patas = num_patas;
				this.habitat = habitat;
			}

			//metodos
			public void comer () {
				System.out.println("Estoy comiendo en " + this.habitat);
			}

		}



		int n1 = 10;
		double n2 = 4;
		char caracter = 'e';
		String palabra = "oracle";

		Animal perro = new Animal("mamifero", 4, "casa");


		System.out.println("El valor de numero_entero es: " + n1);
		System.out.println("Yo amo " + palabra);


		System.out.println("El modulo es " + (n1 % n2));

		animal1.comer();









				



	}

}