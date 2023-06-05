types = ('.gif', '.jpeg', '.jpg', '.png', '.pdf', '.txt', '.zip')
results = ('image/gif', 'image/jpeg', 'image/jpeg', 'image/png', 'application/pdf', 'text/plain', 'application/zip')
n = 0
file_name = str(input('File name: ')).strip().lower()
for i in range(len(types)):
    if types[i] in file_name[-5:]:
        print(results[i])
        n += 1
if n == 0:
    print('application/octet-stream')