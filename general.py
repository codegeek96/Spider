import os


# Each website is a separate project (is in a new folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        new_file(queue, base_url)
    if not os.path.isfile(crawled):
        new_file(crawled, '')


# Create a new file
def new_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    items = set()
    with open(file_name, 'rt') as file:
        for line in file:
            items.add(line.replace('\n', ''))
    return items


# Iterate through a set, each item will be a new line in the file
def set_to_file(items, file_name):
    delete_file_contents(file_name)
    for link in sorted(items):
        append_to_file(file_name, link)