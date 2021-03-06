from database import Database
from models.blog import Blog

__author__ = "Francis Divine"

Database.initialize()

blog = Blog(author='Guei',
            title='Sample title',
            description='Sample description')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
