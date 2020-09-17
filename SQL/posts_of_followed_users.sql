SELECT * FROM follows
    JOIN posts
        ON posts.author_id = follows.followed_id
    WHERE follower_id = 1
    ORDER BY posts.timestamp DESC;