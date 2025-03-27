from pymongo import MongoClient
from datetime import datetime

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client.local  # 'local' 데이터베이스 사용

def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
    ]
    db.books.insert_many(books)



    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": datetime(2023, 4, 12, 8, 0)},
        {"user_id": 1, "action": "view", "timestamp": datetime(2023, 4, 12, 9, 0)},
        {"user_id": 2, "action": "purchase", "timestamp": datetime(2023, 4, 12, 10, 0)},
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()

if __name__ == "__main__":
    insert_data()


from pymongo import MongoClient
from datetime import datetime

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client.local  # 'local' 데이터베이스 사용

# 문제 1: 특정 장르의 책 찾기
def find_books_by_genre(genre):
    books = db.books.find({"genre": genre}, {"title": 1, "author": 1, "_id": 0})
    return list(books)

# 문제 2: 감독별 평균 영화 평점 계산
def avg_rating_by_director():
    pipeline = [
        {"$group": {"_id": "$director", "avg_rating": {"$avg": "$rating"}}},
        {"$sort": {"avg_rating": -1}}
    ]
    directors = db.movies.aggregate(pipeline)
    return list(directors)

# 문제 3: 특정 사용자의 최근 행동 조회
def recent_user_actions(user_id, limit=5):
    actions = db.user_actions.find({"user_id": user_id}).sort("timestamp", -1).limit(limit)
    return list(actions)

# 문제 4: 출판 연도별 책의 수 계산
def count_books_by_year():
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    book_counts = db.books.aggregate(pipeline)
    return list(book_counts)

# 문제 5: 특정 사용자의 행동 유형 업데이트
def update_user_actions(user_id, before_date):
    result = db.user_actions.update_many(
        {"user_id": user_id, "action": "view", "timestamp": {"$lt": before_date}},
        {"$set": {"action": "seen"}}
    )
    return result.modified_count  # 업데이트된 문서 수 반환

# 실행 코드
if __name__ == "__main__":
    print("📚 Fantasy 장르의 책 찾기:")
    print(find_books_by_genre("fantasy"))

    print("\n🎬 감독별 평균 영화 평점:")
    print(avg_rating_by_director())

    print("\n🕵️‍♂️ 사용자 1의 최근 행동:")
    print(recent_user_actions(1))

    print("\n📅 출판 연도별 책 개수:")
    print(count_books_by_year())

    print("\n🔄 사용자 1의 'view' 행동을 'seen'으로 변경:")
    updated_count = update_user_actions(1, datetime(2023, 4, 13))
    print(f"업데이트된 문서 수: {updated_count}")
