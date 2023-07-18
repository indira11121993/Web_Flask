from flask import Flask

from server import AdvertisementViews


app = Flask('server')

app.add_url_rule('/advt/', methods=['POST'], view_func=AdvertisementViews.as_view('create_advt'))
app.add_url_rule('/advt/<int:advt_id>', methods=['GET', 'PATCH', 'DELETE'], view_func=AdvertisementViews.as_view('get_advt'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)