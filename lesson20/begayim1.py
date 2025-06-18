import datetime
import json

def add_posts():
    posts = []

    while True:
        try:
            while True:
                name = input("Title of the post: ").strip()
                if name:
                    break
                else:
                    print("Empty title! Try again!")

            while True:
                description = input("Description of the post: ").strip()
                if description:
                    break
                else:
                    print("Empty description! Try again!")

            while True:
                tags = input("Hashtag of the post: ").strip().split()

                if not tags:
                    print("Tags are empty! Try again!")
                    continue

                for tag in tags:
                    if not tag.startswith('#'):
                        print(f"Incorrect hashtag '{tag}'! Try again!")
                        break
                else:
                    break

            while True:
                date = input("Enter the date of the post (format - YYYY-MM-DD): ").strip()
                try:
                    datetime.datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Incorrect format! Try again!")

            while True:
                music = input("Enter title of the music: ").strip()
                if music:
                    break
                else:
                    print("Empty music! Try again!")

            while True:
                try:
                    likes = int(input("Enter number of likes: ").strip())
                    break
                except ValueError:
                    print("Likes must be a number! Try again!")

            comments = []
            print("Enter comments (type 'токтоо' to finish):")
            while True:
                comment = input("- ").strip()
                if comment.lower() == "токтоо":
                    break
                if comment:
                    comments.append(comment)
                else:
                    print("Empty comment skipped!")

            post = {
                "name": name,
                "description": description,
                "tags": tags,
                "date_published": date,
                "music": music,
                "likes": likes,
                "comments": comments
            }

            posts.append(post)

            continue_adding = input("Do you want to add another post? (yes/no): ").strip().lower()
            if continue_adding != 'yes':
                break

        except Exception as e:
            print(f"Unexpected error: {e}. Try again.")

    try:
        with open('posts.json', 'w') as file:
            json.dump(posts, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving posts to file: {e}")


if __name__ == "__main__":
    add_posts()