import os
import feedparser
import html2text
from datetime import datetime

# Blogger RSS 피드 URL
BLOG_FEED_URL = "https://bugeun.blogspot.com/feeds/posts/default?alt=rss"

# 마크다운 파일 저장 경로
POSTS_DIR = r"C:\Users\choib\OneDrive\문서\GitHub\bugeun.github.io\_posts"

# 디렉터리 확인 및 생성
os.makedirs(POSTS_DIR, exist_ok=True)

# RSS 데이터 가져오기
feed = feedparser.parse(BLOG_FEED_URL)

# HTML -> Markdown 변환기 초기화
converter = html2text.HTML2Text()
converter.ignore_links = False  # 링크 유지

# 블로그 글 파싱 및 Markdown 저장
for entry in feed.entries:
    title = entry.title

    # 날짜 변환 (RFC 2822 형식 → YYYY-MM-DD)
    date_string = entry.published  # 예: "Wed, 05 Feb 2025 04:14:00 +0000"
    date_object = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")
    date = date_object.date()

    content_html = entry.content[0].value if "content" in entry else entry.summary
    content_md = converter.handle(content_html)

    # 파일 이름 정리
    safe_title = title.replace(" ", "-").replace("/", "-").replace("?", "").replace(":", "").lower()
    filename = f"{date}-{safe_title}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    # Jekyll Markdown 파일 작성
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"date: {date}\n")
        f.write(f"categories: blogger\n")
        f.write(f"---\n\n")
        f.write(content_md)

    print(f"✅ {filename} 저장 완료!")

print("\n🎉 모든 블로그 글을 Markdown으로 변환 완료!")
