import sys

from imagebattle import app, db

if __name__ == '__main__':
    db.create_all()

    if len(sys.argv) > 1 and sys.argv[1] == "init":
        from imagebattle.models import Image
        if not Image.query.all():
            db.session.add(Image("http://www.pacificislandbooks.com/crab.jpg"))
            db.session.add(Image("http://ichef.bbci.co.uk/naturelibrary/images/ic/credit/640x395/h/he/hermit_crab/hermit_crab_1.jpg"))
            db.session.add(Image("http://www.howdoeslooklike.com/wp-content/uploads/2013/03/crab-1.jpg"))
            db.session.add(Image("https://tvrecappersanonymous.files.wordpress.com/2010/06/grotesque-forward-walking-spanner-crab1.jpg"))
            db.session.add(Image("http://www.chesapeakebay.net/images/field_guide/Hermit_Crab_page_image.jpg"))
            db.session.commit()
            print("Loaded {} images.".format(len(Image.query.all())))

    app.run(debug=True)
