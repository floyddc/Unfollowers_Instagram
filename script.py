import pyfiglet

def get_non_reciprocal_followers(following_file, followers_file, output_file):
    # Leggi gli username dai file
    with open(following_file, 'r') as f:
        following = set(line.strip() for line in f)
    with open(followers_file, 'r') as f:
        followers = set(line.strip() for line in f)

    # Trova gli username che non hanno ricambiato il follow
    non_reciprocal = following - followers

    # Scrivi gli username dei non ricambiati su un file
    with open(output_file, 'w') as file:
        for username in sorted(non_reciprocal):
            file.write(username + '\n')

if __name__ == "__main__":
    print(pyfiglet.figlet_format("Unfollowers Instagram"))

    # Nome dei file di output
    followers_file = "followers.txt"
    following_file = "following.txt"
    output_file = "UNFOLLOWERS.txt"

    # Trova e salva gli username non ricambiati
    get_non_reciprocal_followers(following_file, followers_file, output_file)

    print("Follower and following loaded from ", followers_file, "and", following_file)
    print("Accounts that don't follow you back saved on ", output_file)