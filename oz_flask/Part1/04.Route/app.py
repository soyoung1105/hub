from flask import Flask

app = Flask(__name__)

# 기본 경로에 대한 라우트
@app.route('/')
def home():
    return 'Hello, this is the home page!'

# 다른 경로에 대한 라우트
# 127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'This is the about page.'

# 127.0.0.1:5000/project
@app.route('/project')
def project():
    return 'The project page'

# 동적인 URL 파라미터 사용
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# URL에 변수 및 타입 지정
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'
## API END POINT 생성 ##
# CRUD: Create(POST), Read(GET), Update(UPDATE), Delete(DELETE) -> REST API
# GET: 데이터를 요청할 때
# POST: CREATE. 데이터를 생성할 때
from flask import jsonify
@app.route("/api/v1/feeds", methods=['GET'])
def get_all_feeds():
    # DB에서 불러온다.
    data = {
        'status': 'success',
        'feed': {
            "feed1": "data",
            "feed2": "data2"
        }
    }
    # python -> dict -> json
    return jsonify(data)
# 다양한 HTTP 메소드 지원
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        return 'POST method.'
    else:
        return 'GET method.'