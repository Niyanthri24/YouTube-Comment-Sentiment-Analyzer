from youtube_comment_downloader import YoutubeCommentDownloader

def get_comments(video_url, max_comments=20):
    downloader = YoutubeCommentDownloader()
    generator = downloader.get_comments_from_url(video_url)

    comments = []
    for count, comment in enumerate(generator):
        if count >= max_comments:
            break
        comments.append(comment['text'])
    
    return comments
