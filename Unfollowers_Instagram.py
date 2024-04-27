import instaloader
from tqdm import tqdm

def get_followers(username, password):
    # Inizializza un'istanza di Instaloader
    loader = instaloader.Instaloader()

    try:
        # Autenticazione
        loader.context.log("Login...")
        loader.context.login(username, password)
        loader.context.log("Login done! Looking for your followers...")

        # Ottieni il profilo dell'utente fornito
        profile = instaloader.Profile.from_username(loader.context, username)

        # Ottieni la lista dei follower
        followers = []
        with tqdm(desc="Download follower", unit="users", leave=False) as pbar:
            for follower in profile.get_followers():
                followers.append(follower.username)
                pbar.update(1)

        return followers

    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
        return []
    except instaloader.exceptions.QueryReturnedNotFoundException:
        print("Profile does not exist or it's private.")
        return []
    except instaloader.exceptions.BadCredentialsException:
        print("Wrong credentials.")
        return []

def get_following(username, password):
    # Inizializza un'istanza di Instaloader
    loader = instaloader.Instaloader()

    try:
        # Autenticazione
        loader.context.log("Login...")
        loader.context.login(username, password)
        loader.context.log("Login done! Looking for your following...")

        # Ottieni il profilo dell'utente fornito
        profile = instaloader.Profile.from_username(loader.context, username)

        # Ottieni la lista dei profili seguiti
        following = []
        with tqdm(desc="Download following", unit="users", leave=False) as pbar:
            for followee in profile.get_followees():
                following.append(followee.username)
                pbar.update(1)

        return following

    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
        return []
    except instaloader.exceptions.QueryReturnedNotFoundException:
        print("Profile does not exist or it's private.")
        return []
    except instaloader.exceptions.BadCredentialsException:
        print("Wrong credentials.")
        return []

def get_non_reciprocal_followers(following, followers, output_file):
    # Trova gli username che non hanno ricambiato il follow
    non_reciprocal = following - followers

    # Scrivi gli username dei non ricambiati su un file
    with open(output_file, 'w') as file:
        for username in sorted(non_reciprocal):
            file.write(username + '\n')

if __name__ == "__main__":
    username = input("Insert your Instagram username: ")
    password = input("Insert your Instagram password: ")

    # Ottieni i follower
    followers = set(get_followers(username, password))

    # Ottieni i profili seguiti
    following = set(get_following(username, password))

    # Nome dei file di output
    followers_file = "followers.txt"
    following_file = "following.txt"
    output_file = "UNFOLLOWERS.txt"

    # Salva i follower in un file di testo
    with open(followers_file, 'w') as file:
        with tqdm(desc="Saving followers", total=len(followers), unit="users", leave=False) as pbar:
            for follower in sorted(followers):
                file.write(follower + '\n')
                pbar.update(1)

    # Salva i profili seguiti in un file di testo
    with open(following_file, 'w') as file:
        with tqdm(desc="Saving following", total=len(following), unit="user", leave=False) as pbar:
            for followee in sorted(following):
                file.write(followee + '\n')
                pbar.update(1)

    # Trova e salva gli username non ricambiati
    get_non_reciprocal_followers(following, followers, output_file)

    print("Follower and following saved on ", followers_file, "and", following_file)
    print("Accounts that don't follow you back saved on ", output_file)
