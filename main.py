from app.database import Database
from app.github_manager import GitHubManager

def main():
    print("=== Clone-Manager ===")
    db = Database("repos.db")
    manager = GitHubManager(db)

    while True:
        print("\nMenu:")
        print("1. Add Repository")
        print("2. See Repository List")
        print("3. Delete Repository")
        print("4. Update All Repository")
        print("5. Quit")
        
        choice = input("Choose Option: ")
        if choice == "1":
            url = input("Enter URL Repository: ")
            manager.add_repo(url)
        elif choice == "2":
            manager.list_repos()
        elif choice == "3":
            repo_id = input("Enter the Repository ID you want to delete: ")
            manager.remove_repo(repo_id)
        elif choice == "4":
            manager.update_all_repos()
        elif choice == "5":
            print("Quit From Program.")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()
