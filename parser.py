import os
import feedparser
import requests
from bs4 import BeautifulSoup
import html2text
from datetime import datetime

# 티스토리 블로그 카테고리 페이지 기본 URL
T_BLOG_URL = "https://bugeun1007.tistory.com/category/Posts"
PAGE_PARAM = "?page="

# 마크다운 파일 저장 경로

T_POSTS_DIR = r"C:\Users\choib\OneDrive\문서\GitHub\bugeun.github.io\_posts\Tistory"

os.makedirs(T_POSTS_DIR, exist_ok=True)

# User-Agent 설정 (크롤링 차단 방지)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# HTML -> Markdown 변환기
converter = html2text.HTML2Text()
converter.ignore_links = False  # 링크 유지


# ✅ 2. Tistory 크롤링 (모든 페이지)
print(f"\n🌐 티스토리 블로그 크롤링 시작!")

page = 1  # 첫 번째 페이지부터 시작
while True:
    url = T_BLOG_URL + PAGE_PARAM + str(page)
    print(f"📄 페이지 {page} 크롤링 중: {url}")

    # 페이지 요청
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ 요청 실패 (HTTP {response.status_code})")
        break  # 더 이상 페이지가 없음

    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 현재 페이지에 글이 없으면 종료
    if not soup.find("div", class_="list_content") and not soup.find("div", class_="entryProtected"):
        print(f"✅ 페이지 {page}에 게시글이 없음. 크롤링 종료!")
        break

    # ✅ 보호된 글 파싱 (entryProtected)
    for entry in soup.find_all("div", class_="entryProtected"):
        title_tag = entry.find("a")
        date_tag = entry.find("p", class_="date")

        if title_tag and date_tag:
            title = title_tag.text.strip()
            post_url = "https://bugeun1007.tistory.com" + title_tag["href"]

            # 날짜 변환
            date_text = date_tag.text.strip().split(" 보호글")[0]
            date_object = datetime.strptime(date_text, "%Y. %m. %d. %H:%M")
            post_date = date_object.date()

            # 개별 글 HTML 가져오기
            post_response = requests.get(post_url, headers=HEADERS)
            post_soup = BeautifulSoup(post_response.text, "html.parser")

            # 본문 추출
            content_div = post_soup.find("div", class_="tt_article_useless_p_margin")
            content_html = str(content_div) if content_div else "<p>본문을 찾을 수 없습니다.</p>"

            # HTML -> Markdown 변환
            content_md = converter.handle(post_url)

            # 파일 저장
            safe_title = title.replace(" ", "-").replace("/", "-").replace("?", "").replace(":", "").lower()
            filename = f"{post_date}-{safe_title}.md"
            filepath = os.path.join(T_POSTS_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {post_date}\n")
                f.write(f"categories: Articles,Papers\n")
                f.write(f"---\n\n")
                f.write(content_md)

            print(f"✅ {filename} 저장 완료!")

    # ✅ 일반 글 파싱 (list_content)
    for entry in soup.find_all("div", class_="list_content"):
        title_tag = entry.find("a", class_="item")
        info_content = entry.find("div", class_="info_content")

        if title_tag and info_content:
            title = info_content.find("strong").text.strip()
            post_url = "https://bugeun1007.tistory.com" + title_tag["href"]

            # 날짜 추출 및 변환
            raw_text = info_content.text.strip()
            date_text = raw_text.split("|")[-1].strip()
            date_object = datetime.strptime(date_text, "%Y. %m. %d. %H:%M")
            post_date = date_object.date()

            # 개별 글 HTML 가져오기
            post_response = requests.get(post_url, headers=HEADERS)
            post_soup = BeautifulSoup(post_response.text, "html.parser")

            # 본문 추출
            content_div = post_soup.find("div", class_="tt_article_useless_p_margin")
            content_html = str(content_div) if content_div else "<p>본문을 찾을 수 없습니다.</p>"

            # HTML -> Markdown 변환
            content_md = converter.handle(content_html)

            # 파일 저장
            safe_title = title.replace(" ", "-").replace("/", "-").replace("?", "").replace(":", "").lower()
            filename = f"{post_date}-{safe_title}.md"
            filepath = os.path.join(T_POSTS_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {post_date}\n")
                f.write(f"categories: Blog\n")
                f.write(f"---\n\n")
                f.write(content_md)

            print(f"✅ {filename} 저장 완료!")

    # 다음 페이지로 이동
    page += 1


    # ✅ 일반 코딩 글 파싱 (list_content)

while True:
    T_BLOG_URL = "https://bugeun1007.tistory.com/category/Coding"
    url = T_BLOG_URL + PAGE_PARAM + str(page)
    print(f"📄 페이지 {page} 크롤링 중: {url}")

    # 페이지 요청
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ 요청 실패 (HTTP {response.status_code})")
        break  # 더 이상 페이지가 없음
    

    # 마크다운 파일 저장 경로
    T_POSTS_DIR = r"C:\Users\choib\OneDrive\문서\GitHub\bugeun.github.io\_posts\Coding"
    os.makedirs(T_POSTS_DIR, exist_ok=True)

    # User-Agent 설정 (크롤링 차단 방지)
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    # HTML -> Markdown 변환기
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # 링크 유지


    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 현재 페이지에 글이 없으면 종료
    if not soup.find("div", class_="list_content") and not soup.find("div", class_="entryProtected"):
        print(f"✅ 페이지 {page}에 게시글이 없음. 크롤링 종료!")
        break

    for entry in soup.find_all("div", class_="list_content"):
        title_tag = entry.find("a", class_="item")
        info_content = entry.find("div", class_="info_content")

        if title_tag and info_content:
            title = info_content.find("strong").text.strip()
            post_url = "https://bugeun1007.tistory.com" + title_tag["href"]

            # 날짜 추출 및 변환
            raw_text = info_content.text.strip()
            date_text = raw_text.split("|")[-1].strip()
            date_object = datetime.strptime(date_text, "%Y. %m. %d. %H:%M")
            post_date = date_object.date()

            # 개별 글 HTML 가져오기
            post_response = requests.get(post_url, headers=HEADERS)
            post_soup = BeautifulSoup(post_response.text, "html.parser")

            # 본문 추출
            content_div = post_soup.find("div", class_="tt_article_useless_p_margin")
            content_html = str(content_div) if content_div else "<p>본문을 찾을 수 없습니다.</p>"

            # HTML -> Markdown 변환
            content_md = converter.handle(content_html)

            # 파일 저장
            safe_title = title.replace(" ", "-").replace("/", "-").replace("?", "").replace(":", "").lower()
            filename = f"{post_date}-{safe_title}.md"
            filepath = os.path.join(T_POSTS_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {post_date}\n")
                f.write(f"categories: Coding\n")
                f.write(f"---\n\n")
                f.write(content_md)

            print(f"✅ {filename} 저장 완료!")

    # 다음 페이지로 이동
    page += 1

print("\n🎉 모든 Blogger & Tistory 글을 Markdown으로 변환 완료!")
