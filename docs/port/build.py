print('hello world')

top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()

index = open('./content/index.html').read()
blog = open('./content/blog.html').read()
contact = open('./content/contact.html').read()
projects = open('./content/projects.html').read()



open('./docs/index.html', 'w+').write(top + index + bottom)
open('./docs/blog.html', 'w+').write(top + blog + bottom)
open('./docs/contact.html', 'w+').write(top + contact + bottom)
open('./docs/proje.html', 'w+').write(top + projects + bottom)
