import sys
from db import create_db
from crawl import get_links, crawl_pages
from models import Articles, Category


def run():

    cat = Category.create(name='sport')
    for i in get_links():
        art = Articles.create(url=i, category=cat)
        print(art.id)


def show_stats():

    art = Articles.select().count()
    cat = Category.select().count()
    isc = Articles.select().where(Articles.is_completed==True).count()
    print(f"Articles: {art}\tcategory: {cat}\tis_completed: {isc}")


if __name__ == "__main__":
    if sys.argv[1] == 'create_tables':
        create_db()

    elif sys.argv[1] == 'run':    
        run()

    elif sys.argv[1] == 'stats':
        show_stats()   

    elif sys.argv[1] == 'pages':
        articles = Articles.select().where(Articles.is_completed==False)
        for article in articles:
            print(article)
            data = crawl_pages(article.url)
            print(data)
            article.title = data['title'] 
            article.body = data['body'] 
            article.is_completed = True 
            article.save()
