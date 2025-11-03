import sys  #pour interagir avec le systeme
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget   #des composant graphiques
from PyQt5.QtCore import Qt # pour des constantes comme lalignement du texte par exemple

#une classe pour l application principale
class RestaurantApp(QWidget):
    def __init__(self):
        super().__init__() # Appele le constructeur de la classe mere
        self.init_ui() #initialiser l interface utilisateur
#Configuration de la fenetre
    def init_ui(self):
        self.setWindowTitle("Dalia s Restaurant ")  # titre pour la fentre
        self.resize(1000, 800) # taille pour la fenetre

    # style pour la fenetre couleur / bouton / taille/ ecriture
        self.setStyleSheet(""" 
            QWidget { 
                background-color: #fff3e0;   
               color: #4e342e;   
               font-family: 'Segoe UI', sans-serif;  
               font-size: 20px; 
                font-weight: bold; 
            } 
            QLabel { 
                color: #d84315;  
               font-weight: bold; 
            } 
            QPushButton { 
                background-color: #ff7043;   
               color: white; 
                border-radius: 10px; 
                padding: 12px; 
                font-size: 20px; 
                font-weight: bold; 
                border: none; 
                margin: 5px; 
            } 
            QPushButton:hover {  
                background-color: #ff5722;  
           } 
            QListWidget { 
                background-color: #ffccbc;  
               border: 2px solid #ff7043;  
               border-radius: 8px; /* Coins arrondis pour un look moderne */
                padding: 5px; 
            } 
            QListWidget::item { 
                padding: 8px; 
                margin: 2px; 
            } 
            QListWidget::item:selected { 
                background-color: #ff8a65; /* Couleur saumon clair pour l element selectionne */ 
                color: white; 
                font-weight: bold; 
            } 
            QLabel#title { 
                font-size: 22px; 
                text-transform: uppercase; /* on met tout en majuscule */
                margin-bottom: 10px; 
            } 
            QLabel#total { 
                font-size: 18px; 
                color: #bf360c; 
            } 
        """)
        # j ai utiliser les "::"  dans la partie css pour styliser des parties internes  d un widget
        # par contre la "#"  pour Un widget specifique



        #  layout vertical pour organiser les widgets les uns sous les autres
        main_layout = QVBoxLayout()

        # Titre
        self.title_label = QLabel("Restaurant Dalia's Menu") # titre principal
        self.title_label.setObjectName("title") #j l donner un "id" pour le personnaliser dans le style
        self.title_label.setAlignment(Qt.AlignCenter) # pour centrer le titre
        main_layout.addWidget(self.title_label)# pour ajouterr le titre au layout principal

        # Liste des categories
        self.categories = {
            "Entrées": ["Salade César - 9€", "Soupe - 6€ ", "Bruschetta - 8€ ", "Carpaccio de bœuf - 9€"],
            "Plats Principaux": ["Steak Frites - 18€", "Poulet Rôti - 12€", "Saumon Grillé - 24€"],
            "Pizzas": ["Margherita - 10€", "Reine (Jambon, Champignons) - 12€", "Quatre Fromages - 14€",
                       "Calzone - 11€"],
            "Burgers": ["Cheeseburger - 15€", "Chicken Burger - 10€", "Vegan Burger - 12€",
                        "Double Bacon Burger - 15€"],
            "Desserts": ["Tarte aux Pommes - 10€", "Mousse au Chocolat - 8€", "Tiramisu - 9€", "Crème Brûlée - 7€"],
            "Boissons": ["Coca-Cola - 4€", "Eau Minérale - 2€", "Jus d'Orange Frais - 5€", "Smoothie aux Fruits - 6€",
                         "Café - 4€"]
        }
        # remarque : les prix  je les ai fixes a peu pres

        # partie  "menu"
        self.menu_list = QListWidget() # liste pour afficher les choix
        self.menu_list.addItems([item for category in self.categories.values() for item in category]) # j ajouter tous les plats
        self.menu_list.itemClicked.connect(self.add_to_cart) # quand on clique sur un plat on l ajoute au panier
        main_layout.addWidget(self.menu_list) # pour ajouter cette liste au layout principal

        # partie panier
        cart_layout = QVBoxLayout() #un autre layout vertical pour organiser le panier
        cart_label = QLabel("Panier :") # titre pour indiquer la partie du panier
        cart_layout.addWidget(cart_label) #ajoute le label "Panier :" au layout vertical du panier

        self.cart_list = QListWidget()  # une autre liste pour afficher les items du panier
        cart_layout.addWidget(self.cart_list)

        self.total_label = QLabel("Total : 0€") # label pour afficher le total
        self.total_label.setObjectName("total") #j l donner un "id" pour  personnaliser dans le style
        cart_layout.addWidget(self.total_label)

        main_layout.addLayout(cart_layout) # pour ajouter la section panier au layout principal


        # Bouton pour valider la commande
        self.validate_button = QPushButton("Valider la commande") # bouton avec texte
        self.validate_button.clicked.connect(self.validate_order) # quand on clique on valide la commande
        main_layout.addWidget(self.validate_button) # pour ajouter le bouton au layout principal

        #  pour applique le layout principal a la fenetre.
        self.setLayout(main_layout)

# fonction pour ajouter les plats quand on click
    def add_to_cart(self, item):
        self.cart_list.addItem(item.text())

        # Mise a jour du total
        price = int(item.text().split('-')[-1].strip().replace('€', '')) # pour extrait le prix
        current_total = int(self.total_label.text().split(':')[-1].strip().replace('€', '')) #total actuel
        new_total = current_total + price #  pour calculer le nouveau total
        self.total_label.setText(f"Total : {new_total}€") # pour met a jour l affichage

# fonction pour la validation de la commande
    def validate_order(self):
        items = [self.cart_list.item(i).text() for i in range(self.cart_list.count())] #  quand on valide on recupere les items du panier
        if items: # pour verifier si le panier contient des elements
            order_details = "\n".join(items) # pour cree une chaine contenant tous les items du panier / separes par des sauts de ligne
            print(f"Commande validée :\n{order_details}\nTotal : {self.total_label.text()}")  #  pour afficher les details de la commande et le total dans la console
        else:  # si le panier est vide
            print("Votre panier est vide.") # il va afficher ce message " Votre panier est vide"

        #  pour lancer l application


app = QApplication(sys.argv) # j ai cree une instance de l application
window = RestaurantApp() #  instancie ma classe principal
window.show()  # pour afficher la fenetre
sys.exit(app.exec_()) # pour demarrer l application
