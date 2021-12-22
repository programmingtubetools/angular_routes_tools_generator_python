tools = []
routes = []
filename = input('Enter File Name to Load: ')
ComponentName = input('Component Name: ')
with open(f'{filename}.txt') as f:
    for line in f:
        link = f"{'-'.join(line.lower().strip().split())}"
        tool = '{\n' + f"\ttool: '{line.strip()}',\n\tlink: '{link}'" + "\n}"
        tools.append(tool)

        route = "{ " + f"path: '{link}', component: {ComponentName}, data: " +  "{ " + f"title: '{line.strip()}', subTitle: ''" + " } }"
        routes.append(route)

def write(filename, data):
    with open(filename, 'w') as f:
        f.write(',\n'.join(data))

write('tools.txt', tools)
write('routes.txt', routes)
