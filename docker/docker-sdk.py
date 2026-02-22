#  python3 -m pip install docker --break-system-packages
# sudo apt install python3-xyz
# python3 -m pip install --upgrade pip

import docker

# Connexion au daemon Docker local
client = docker.from_env()

# Lancer un conteneur Nginx en arrière-plan
container = client.containers.run("nginx", name="maco", detach=True)

# Renommer le conteneur
container.rename("makrelle")
print(f"Le conteneur a été renommé en : {container.name}")

# Lister les conteneurs en cours
print("\nConteneurs en cours d'exécution :")
for c in client.containers.list():
    print(f"- {c.name} ({c.status})")

# Télécharger l'image Redis
redis_image = client.images.pull("redis")
print(f"\nImage Redis téléchargée : {redis_image.tags}")