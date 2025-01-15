import os
import subprocess
from app.database import Database

class GitHubManager:
    def __init__(self, db):
        self.db = db

    def add_repo(self, url):
        repo_name = url.split("/")[-1].replace(".git", "")
        clone_path = os.path.join("cloned_repos", repo_name)

        # Clone repository
        if not os.path.exists(clone_path):
            subprocess.run(["git", "clone", url, clone_path])
            self.db.insert_repo(repo_name, url, clone_path)
            print(f"Repository {repo_name} succesfully clonned.")
        else:
            print(f"Repository {repo_name} already exist.")

    def list_repos(self):
        repos = self.db.fetch_all()
        print("Repositori List:")
        for repo in repos:
            print(f"[{repo[0]}] {repo[1]} - {repo[2]} (Path: {repo[3]})")

    def remove_repo(self, repo_id):
        repos = self.db.fetch_all()
        for repo in repos:
            if repo[0] == int(repo_id):
                subprocess.run(["rm", "-rf", repo[3]])
                self.db.delete_repo(repo_id)
                print(f"Repository {repo[1]} Succesfully deleted.")
                return
        print("ID Repository not found.")

    def update_all_repos(self):
        repos = self.db.fetch_all()
        for repo in repos:
            subprocess.run(["git", "-C", repo[3], "pull"])
            print(f"Repository {repo[1]} updated.")
