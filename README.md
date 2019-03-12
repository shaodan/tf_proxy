# tf_proxy

FLASK_ENV=development FLASK_APP=server.py flask run --host=0.0.0.0 --port=3000

curl -XPOST 'http://localhost:3000/tf' -H "Content-Type: application/json" --data '{"hello":"world"}'
