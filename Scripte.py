# pip install instaloader
import instaloader

il = instaloader.Instaloader()
login = "votre email"
pwd = "votre mdp"
account_to_scrap = "le compte don vous voulez dl les stories"
path = "comments"

il.login(user=login, passwd=pwd)
profile = instaloader.Profile.from_username(il.context, username=account_to_scrap)
il.download_stories(userids=[profile.userid], filename_target=path)