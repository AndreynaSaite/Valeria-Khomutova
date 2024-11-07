import subprocess

def get_git_objects():
    command = ['git', 'rev-list', '--objects', '--all']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return []

    print(result.stdout.splitlines())
    print("commit with file")
    return result.stdout.splitlines()

def print_object_contents(objects):
    for obj in objects:
        if obj.strip():
            parts = obj.split(' ', 1)
            if len(parts) == 2:
                sha, name = parts
                try:
                    command = ['git', 'cat-file', '-p', sha]
                    result = subprocess.run(command, capture_output=True, text=True)
                    print(result)
                    if result.returncode == 0:
                        print(f"Object: {sha} (Name: {name})")
                        print(result.stdout)
                    else:
                        print(f"Ошибка при получении содержимого {sha}: {result.stderr}")
                except Exception as e:
                    print(f"ошибка: {e}")
            else:
                print(f"Не удалось распаковать строку: {obj}")

def main():
    objects = get_git_objects()
    if objects:
        print_object_contents(objects)

if __name__ == "__main__":
    main()
